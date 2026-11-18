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


if __name__ == "__main__":
    unittest.main()
