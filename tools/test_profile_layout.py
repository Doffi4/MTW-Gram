"""Exercise the profile's actual layout expressions without opening an account."""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram/SourceFiles"
PROFILE = Path("info/profile")
INFORMATION = Path("settings/sections/settings_information.cpp")
STYLES = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in (
    "info/info.style", "info/profile/info_profile_top_bar.style"))
PADDING = tuple(map(int, re.search(
    r"infoProfileTopBarActionButtonsPadding: margins\((\d+)px, (\d+)px, (\d+)px, (\d+)px\)", STYLES).groups()))


def expression(file, name, values):
    source = (ROOT / file).read_text(encoding="utf-8")
    match = re.search(r"const auto " + name + r" = (.*?);", source, re.S)
    assert match, f"Missing bounded profile layout: {name}"
    text = match[1].replace("std::min", "min").replace("std::max", "max")
    text = text.replace("int(buttons.size())", "count").replace("size.width()", "newWidth")
    text = text.replace("strip->naturalWidth()", "naturalWidth").replace("width()", "newWidth")
    text = text.replace("rect::m::sum::h(padding)", "padding")
    text = re.sub(r"st::(\w+)", lambda m: re.search(
        r"\b" + m[1] + r": (\d+)px;", STYLES)[1], text)
    text = text.replace("{", "[").replace("}", "]").replace("/", "//")
    return eval(text, {"__builtins__": {}, "min": min, "max": max}, values)


class ProfileLayout(unittest.TestCase):
    def test_content_fits_and_is_centered(self):
        for width in (0, 1, 292, 358, 623, 624, 625, 1280, 2560):
            values = {"newWidth": width}
            content = expression(PROFILE / "info_profile_inner_widget.cpp", "contentWidth", values)
            values["contentWidth"] = content
            left = expression(PROFILE / "info_profile_inner_widget.cpp", "contentLeft", values)
            self.assertEqual(content, min(width, 624))
            self.assertLessEqual(abs(left - (width - left - content)), 1)

    def test_edit_form_cards_fit_and_stay_centered(self):
        for width in (0, 1, 292, 358, 623, 624, 625, 1280, 2560):
            values = {"newWidth": width}
            content = expression(INFORMATION, "contentWidth", values)
            values["contentWidth"] = content
            left = expression(INFORMATION, "contentLeft", values)
            self.assertEqual(content, min(width, 624))
            self.assertLessEqual(abs(left - (width - left - content)), 1)

    def test_actions_fit_for_all_button_counts(self):
        for width in (0, 1, 292, 358, 600, 1280, 2560):
            for count in range(6):
                values = {"newWidth": width, "count": count, "padding": PADDING[0] + PADDING[2]}
                actions = expression(PROFILE / "info_profile_top_bar.cpp", "actionsWidth", values)
                self.assertEqual(actions, max(0, min(
                    width - 30, 570, count * 170 + max(count - 1, 0) * 20)))
                values["actionsWidth"] = actions
                left = expression(PROFILE / "info_profile_top_bar.cpp", "actionsLeft", values)
                self.assertLessEqual(abs(left - (width - left - actions)), 1)

    def test_floating_tabs_stay_within_media_width(self):
        for width in (292, 358, 624, 1280):
            for natural in (200, 600, 900):
                actual = expression(PROFILE / "info_profile_widget.cpp", "stripWidth", {
                    "newWidth": width, "naturalWidth": natural})
                self.assertEqual(actual, min(width, natural, 600))


if __name__ == "__main__":
    unittest.main()
