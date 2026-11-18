"""Check that the painted search header and row offsets share a height."""
from pathlib import Path
import unittest


SOURCE = (Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram"
          / "SourceFiles/dialogs/dialogs_inner_widget.cpp").read_text(encoding="utf-8")


class SearchLayout(unittest.TestCase):
    def test_local_header_pushes_rows_and_hit_testing_together(self):
        header = SOURCE.partition("int InnerWidget::filteredHeaderHeight() const {")[2]
        header = header.split("\n}", 1)[0]
        for condition in ("!_filterResults.empty()", "_searchState.filterChatsList()",
                          "!_openedForum", "!_savedSublists"):
            self.assertIn(condition, header)
        self.assertIn("? st::searchedBarHeight", header)
        offset = SOURCE.partition("int InnerWidget::filteredOffset() const {")[2]
        self.assertIn("+ filteredHeaderHeight()", offset.split("\n}", 1)[0])
        self.assertIn("p.translate(0, headerHeight);", SOURCE)
        self.assertIn("(mouseY >= skip)\n\t\t\t\t? filteredIndex", SOURCE)


if __name__ == "__main__":
    unittest.main()
