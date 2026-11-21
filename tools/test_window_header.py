"""Check the window strip and the profile capsule interaction in the source."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram/SourceFiles"


class WindowHeader(unittest.TestCase):
    def test_caption_uses_its_own_strip(self):
        source = (ROOT / "window/main_window.cpp").read_text(encoding="utf-8")
        self.assertIn("setTitleStyle(st::mtwWindowTitle);", source)
        self.assertNotIn("setupOverlayTitleControls", source)

    def test_profile_click_and_paint_use_the_same_capsule(self):
        source = (ROOT / "history/view/history_view_top_bar_widget.cpp").read_text(
            encoding="utf-8")
        self.assertIn("path.addRoundedRect(rect, radius, radius);", source)
        self.assertIn("_pressedTitleCapsule = titleCapsuleContains(e->pos());", source)
        self.assertIn("pressedTitleCapsule && titleCapsuleContains(e->pos())", source)

    def test_capsule_measures_the_painted_status(self):
        source = (ROOT / "history/view/history_view_top_bar_widget.cpp").read_text(
            encoding="utf-8")
        action = (ROOT / "history/view/history_view_send_action.cpp").read_text(
            encoding="utf-8")
        self.assertEqual(
            source.count("contentWidth = std::max(contentWidth, paintSubtitle());"),
            3,
        )
        self.assertIn("return _sendAction->paint(", source)
        self.assertIn("animationWidth + seen->text.maxWidth()", source)
        self.assertIn("_sendActionText.maxWidth() + (left ? 0 : animationWidth)", action)

    def test_hide_all_cannot_restart_an_in_progress_removal(self):
        source = (ROOT / "window/notifications_manager_default.cpp").read_text(
            encoding="utf-8")
        self.assertIn("if (std::exchange(_positionsOutdated, false))", source)
        self.assertIn("if (!std::exchange(_removing, true)) {\n\t\thideFast(false);", source)
        self.assertIn("if (!_removing) {\n\t\thideStop();", source)


if __name__ == "__main__":
    unittest.main()
