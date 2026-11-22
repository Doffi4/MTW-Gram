"""Check that the topics slide and chat sidebar use one transition."""
from pathlib import Path
import unittest


SOURCE = (Path(__file__).resolve().parents[1] / "refs/tdesktop-7.4.4/Telegram"
          / "SourceFiles/dialogs/dialogs_widget.cpp").read_text(encoding="utf-8")


class ForumTransition(unittest.TestCase):
    def test_both_directions_capture_sidebar_before_changing_layout(self):
        opening = SOURCE.split("void Widget::openChildList(", 1)[1]
        opening, closing = opening.split("void Widget::closeChildList(", 1)
        closing = closing.split("\n}", 1)[0]
        for body, layout_change, direction in (
            (opening, "_childList = std::make_unique", "FromRight"),
            (closing, "_childList = nullptr", "FromLeft"),
        ):
            with self.subTest(direction=direction):
                self.assertLess(body.index("Ui::GrabWidget(this)"),
                                body.index(layout_change))
                self.assertIn("animateChildList(", body)
                self.assertIn(f"Window::SlideDirection::{direction}", body)

    def test_sidebar_blend_uses_the_topic_slide_progress(self):
        body = SOURCE.split("void Widget::animateChildList(", 1)[1]
        body = body.split("\n}", 1)[0]
        self.assertIn("p.setOpacity(animation->progress());", body)
        self.assertIn("animation->paintContents(p);", body)
        self.assertIn("animation->setFinishedCallback", body)


if __name__ == "__main__":
    unittest.main()
