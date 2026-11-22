"""Guard the settings column and its narrow-window navigation."""
from pathlib import Path
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "refs/tdesktop-7.4.4/Telegram/SourceFiles"


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
        for page in ("GeneralId", "DataStorageId", "ChatId", "AppearanceId",
                     "StickersEmojiId"):
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

    def test_folder_radio_cards_fill_the_available_width(self):
        folders = source("settings/sections/settings_folders.cpp")
        self.assertEqual(folders.count(
            "st::settingsSendTypePadding,\n\t\t\t\tstyle::al_justify"), 2)

    def test_chat_crossfade_runs_in_both_history_paths(self):
        main = source("mainwidget.cpp")
        for function in ("showHistory", "showNewSection"):
            body = main.split(f"void MainWidget::{function}(", 1)[1]
            body = body.split("\n}\n", 1)[0]
            self.assertTrue("wideSettingsExit || crossFadeToChat" in body, function)
            self.assertTrue("Window::SlideDirection::CrossFade" in body, function)

    def test_smooth_wheel_is_opt_in_for_both_history_widgets(self):
        settings = source("settings/sections/settings_chat.cpp")
        self.assertIn(".checked = Core::App().settings().readPref<bool>(", settings)
        self.assertIn("writePref<bool>(Core::kSmoothChatWheelKey, value)", settings)
        for widget in ("history/history_widget.cpp",
                       "history/view/history_view_chat_section.cpp"):
            self.assertIn("setSmoothWheelEnabled(", source(widget))

    def test_smooth_wheel_leaves_touchpad_events_on_the_native_path(self):
        scroll = (SOURCE.parent / "lib_ui/ui/widgets/elastic_scroll.cpp").read_text(
            encoding="utf-8")
        gate = scroll.split("const auto smoothWheel =", 1)[1].split(";", 1)[0]
        for check in ("Qt::NoScrollPhase", "WheelSource::Wheel", "DeviceType::TouchPad",
                      "e->pixelDelta().isNull()", "!anim::Disabled()"):
            self.assertIn(check, gate)


if __name__ == "__main__":
    unittest.main()
