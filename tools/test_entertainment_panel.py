"""Guard the content viewport when the composer tabs move to the bottom."""
from pathlib import Path
import unittest


SOURCE = (Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram"
          / "SourceFiles/chat_helpers/tabbed_selector.cpp").read_text(encoding="utf-8")


class EntertainmentPanel(unittest.TestCase):
    def test_full_selector_reserves_space_for_categories_and_tabs(self):
        self.assertIn("return _st.footer + panelInset;", SOURCE)
        self.assertIn("return tabsSliderHeight() + panelInset;", SOURCE)
        self.assertIn("height() - scrollTop() - scrollBottom()", SOURCE)

    def test_slide_cache_excludes_the_fixed_tab_control(self):
        self.assertIn("if (_tabsSlider) {\n\t\t_tabsSlider->hide();", SOURCE)
        self.assertIn("const auto slidingTop = full() ? 0", SOURCE)


if __name__ == "__main__":
    unittest.main()
