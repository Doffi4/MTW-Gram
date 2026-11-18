"""Check that the new message presentation preserves existing interaction paths."""
from pathlib import Path
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram/SourceFiles"


def implementation(path, declaration):
    text = (SOURCE / path).read_text(encoding="utf-8")
    return text.split(declaration, 1)[1].split("\n}", 1)[0]


class MessageSurfaces(unittest.TestCase):
    def test_inline_reaction_exits_are_painted_but_not_clickable(self):
        reactions = "history/view/reactions/history_view_reactions.cpp"
        paint = implementation(reactions, "void InlineList::paint(")
        self.assertIn("paintButton(button, true)", paint)
        removal = implementation(reactions, "void InlineList::animateRemoval(")
        self.assertIn("_transitionRepaint", removal)
        hit_test = implementation(reactions, "bool InlineList::getState(")
        self.assertIn("_removing ||", hit_test)
        self.assertIn("for (const auto &button : _buttons)", hit_test)
        self.assertNotIn("_fadingButtons", hit_test)

    def test_attachment_click_consumed_only_when_it_toggles_the_menu(self):
        composer = "history/view/controls/history_view_compose_controls.cpp"
        click = implementation(composer, "ComposeControls::attachRequests() const {")
        self.assertIn("if (!_attachBotsMenu || isEditingMessage())", click)
        self.assertIn("_attachBotsMenu->showAnimated();", click)
        self.assertIn("_attachBotsMenu->hideAnimated();\n\t\t\t}\n\t\t\treturn false;", click)
        self.assertIn("_attachRequests.events()", click)


if __name__ == "__main__":
    unittest.main()
