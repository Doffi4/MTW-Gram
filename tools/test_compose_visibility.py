"""Check the actual read predicates without launching an account or sending receipts."""
from pathlib import Path
import re
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram/SourceFiles/history"


class ComposeVisibility(unittest.TestCase):
    def test_hidden_message_is_not_read(self):
        for path, top_name, bottom_name in (
            ("history_inner_widget.cpp", "_visibleAreaTop", "_visibleAreaBottom"),
            ("view/history_view_list_widget.cpp", "_visibleTop", "_visibleBottom"),
        ):
            with self.subTest(path=path):
                source = (SOURCE / path).read_text(encoding="utf-8")
                source = re.sub(r"//[^\n]*", "", source)
                predicate = re.search(r"const auto yShown = .*?return (.*?);", source, re.S)[1]
                helper = re.search(r"int \w+::visibleContentBottom\(\) const \{\s*return (.*?);", source, re.S)
                for overlap in (0, 56, 180, 600):
                    values = {top_name: 100, bottom_name: 600, "_bottomOverlap": overlap, "max": max}
                    bottom = eval(helper[1].replace("std::max", "max"), {"__builtins__": {}}, values) if helper else 600
                    for y in (99, 100, 419, 420, 421, 543, 544, 545, 599, 600, 601):
                        values.update(y=y, visibleContentBottom=lambda: bottom)
                        actual = eval(predicate.replace("&&", " and "), {"__builtins__": {}}, values)
                        self.assertEqual(actual, 100 <= y <= max(100, 600 - overlap), (path, overlap, y))


if __name__ == "__main__":
    unittest.main()
