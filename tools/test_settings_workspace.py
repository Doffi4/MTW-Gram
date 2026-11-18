"""Guard the settings column and its narrow-window navigation."""
from pathlib import Path
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram/SourceFiles"


def source(path):
    return (SOURCE / path).read_text(encoding="utf-8")


class SettingsWorkspace(unittest.TestCase):
    def test_settings_stay_in_the_main_window(self):
        self.assertIn("Section::Type::Settings", source("info/info_memento.cpp")
                      .split("Memento::createLayer(", 1)[1].split("\n}", 1)[0])
        self.assertIn("settingsPageValue()", source("mainwidget.cpp"))

    def test_settings_tab_opens_root_in_single_column(self):
        dialog = source("dialogs/dialogs_widget.cpp")
        self.assertIn("? ::Settings::MainId()", dialog)
        self.assertIn(": ::Settings::GeneralId()", dialog)

    def test_sidebar_routes_to_independent_pages(self):
        menu = source("settings/sections/settings_main.cpp").split("CreateSettingsSidebar(", 1)[1]
        for page in ("GeneralId", "DataStorageId", "AppearanceId", "StickersEmojiId"):
            self.assertIn(page + "()", menu)

    def test_sibling_sections_use_crossfade_and_back_keeps_its_direction(self):
        wrap = source("info/info_wrap_widget.cpp").split(
            "void WrapWidget::showNewContent(", 1
        )[1].split("\nvoid WrapWidget::showNewContent(", 1)[0]
        self.assertIn("Way::ClearStack", wrap)
        self.assertIn("SlideDirection::CrossFade", wrap)
        self.assertIn("SlideDirection::FromLeft", wrap)
        self.assertIn("SlideDirection::FromRight", wrap)
        self.assertLess(wrap.index("grabForShowAnimation"), wrap.index("settings && animatingShow()"))

    def test_wide_settings_can_animate_from_an_empty_chat_area(self):
        show = source("mainwidget.cpp").split("void MainWidget::showNewSection(", 1)[1]
        self.assertIn("if (fromBottom || wideSettings)", show)
        self.assertIn("wideSettings && !_mainSection && _history->isHidden()", show)
        self.assertIn("Window::SlideDirection::CrossFade", show)


if __name__ == "__main__":
    unittest.main()
