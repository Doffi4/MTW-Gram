"""Protect the boundary conditions shared by the Windows window and settings."""
from pathlib import Path
import re
import unittest


TELEGRAM = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram"


def source(name):
    return (TELEGRAM / "SourceFiles" / name).read_text(encoding="utf-8")


class RequiredLayout(unittest.TestCase):
    def test_compact_width_is_shared_and_uses_the_new_layout(self):
        styles = source("dialogs/dialogs.style")
        compact = int(re.search(r"dialogsCompactWidth: (\d+)px;", styles)[1])
        snap = int(re.search(r"dialogsCompactSnap: (\d+)px;", styles)[1])
        photo = int(re.search(r"defaultDialogRow: DialogRow \{[^}]*photoSize: (\d+)px;", styles)[1])
        self.assertEqual((compact, snap, (compact - photo) // 2), (90, 100, 20))
        self.assertIn("_narrowWidth(controller->dialogsSmallColumnWidth())",
                      source("dialogs/dialogs_widget.cpp"))
        self.assertIn("_narrowWidth(controller->dialogsSmallColumnWidth())",
                      source("dialogs/dialogs_inner_widget.cpp"))
        self.assertIn("newWidth <= st::dialogsCompactSnap", source("mainwidget.cpp"))
        self.assertIn("layout.windowLayout != Window::Adaptive::WindowLayout::OneColumn",
                      source("mainwidget.cpp"))

    def test_caption_is_hidden_only_when_native_or_fullscreen(self):
        self.assertIn("setNativeFrame(isFullScreen());", source("window/main_window.cpp"))
        self.assertIn("oldState().testFlag(Qt::WindowFullScreen)", source("window/main_window.cpp"))

    def test_windows_theme_notifications_reach_follow_system(self):
        self.assertIn("if (const auto dark = Platform::IsDarkMode())",
                      source("platform/win/integration_win.cpp"))
        self.assertIn("&& (*maybeDarkMode != Window::Theme::IsNightMode())",
                      source("core/application.cpp"))

    def test_long_value_reserves_caption_space(self):
        common = source("settings/settings_common.cpp")
        self.assertIn("setPaddingOverride", common)
        self.assertIn("name->resizeToNaturalWidth", common)
        self.assertIn("cardRadius: 20px;", source("settings/settings.style"))
        radio = (TELEGRAM / "lib_ui/ui/widgets/checkbox.cpp").read_text(encoding="utf-8")
        self.assertIn("width() - _st.margin.right() - size.width()", radio)


if __name__ == "__main__":
    unittest.main()
