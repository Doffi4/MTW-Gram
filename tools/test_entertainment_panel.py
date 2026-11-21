"""Guard the S13 selector layout and sidebar entrance."""
from pathlib import Path
import unittest


SOURCE_DIR = Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram/SourceFiles"
SOURCE = (SOURCE_DIR / "chat_helpers/tabbed_selector.cpp").read_text(encoding="utf-8")
MAIN = (SOURCE_DIR / "mainwidget.cpp").read_text(encoding="utf-8")


class EntertainmentPanel(unittest.TestCase):
    def test_full_selector_reserves_space_for_categories_and_tabs(self):
        self.assertIn("return _st.footer + panelInset;", SOURCE)
        self.assertIn("return tabsSliderHeight() + panelInset;", SOURCE)
        self.assertIn("height() - scrollTop() - scrollBottom()", SOURCE)

    def test_slide_cache_excludes_the_fixed_tab_control(self):
        self.assertIn("if (_tabsSlider) {\n\t\t_tabsSlider->hide();", SOURCE)
        self.assertIn("const auto slidingTop = full() ? 0", SOURCE)

    def test_sidebar_reveal_reserves_space_without_resizing_selector(self):
        self.assertIn("dynamic_cast<ChatHelpers::TabbedSection*>", MAIN)
        self.assertIn("300,\n\t\t\t\tanim::cubicBezier(0.25, 0.8, 0.25, 1.0)", MAIN)
        self.assertIn("_thirdColumnWidth * _a_tabbedSectionReveal.value(1.)", MAIN)
        self.assertIn("width() - thirdSectionWidth,\n\t\t\t\tthirdSectionTop,\n"
                      "\t\t\t\t_thirdColumnWidth,", MAIN)
        self.assertIn("- dialogsWidth\n\t\t\t- thirdSectionWidth;", MAIN)


    def test_manual_sidebar_show_suppresses_instant_layout_restore(self):
        show = MAIN.split("void MainWidget::showSection(", 1)[1]
        show = show.split("void MainWidget::updateColumnLayout()", 1)[0]
        before_layout, _, _ = show.partition("updateColumnLayout();")
        self.assertIn("QScopedValueRollback(", before_layout)
        self.assertIn("dynamic_cast<ChatHelpers::TabbedMemento*>", before_layout)
        self.assertTrue("&& !_openingTabbedSection" in MAIN)

    def test_composer_click_checks_sidebar_before_popup_visibility(self):
        for file in (
            "history/history_widget.cpp",
            "history/view/controls/history_view_compose_controls.cpp",
        ):
            with self.subTest(file=file):
                source = (SOURCE_DIR / file).read_text(encoding="utf-8")
                click = source.split("::initTabbedSelector() {", 1)[1]
                click = click.split("_tabbedSelectorToggle->addClickHandler", 1)[1]
                click = click.split("});", 1)[0]
                self.assertEqual(click.strip(), "([=] {\n\t\ttoggleTabbedSelectorMode();")


if __name__ == "__main__":
    unittest.main()
