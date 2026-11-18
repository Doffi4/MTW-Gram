"""Guard the shared search layout and navigation when global peers are folded."""
from pathlib import Path
import unittest


SOURCE = (Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram"
          / "SourceFiles/dialogs/dialogs_inner_widget.cpp").read_text(encoding="utf-8")
API_SOURCE = (Path(__file__).resolve().parents[1] / "refs/tdesktop/Telegram"
              / "SourceFiles/api/api_peer_search.cpp").read_text(encoding="utf-8")


class GlobalPeers(unittest.TestCase):
    def test_only_visible_peers_count_toward_layout_and_focus(self):
        self.assertIn("kGlobalPeersPreviewCount = 5", SOURCE)
        self.assertIn("ranges::move(tail, std::back_inserter(_hiddenPeerSearchResults))",
                      SOURCE)
        self.assertIn("_peerSearchResults.erase(tail.begin(), tail.end())", SOURCE)
        self.assertIn("ranges::move(_hiddenPeerSearchResults,", SOURCE)
        self.assertIn("clearMouseSelection(true);\n\t\t\t_peerSearchExpanded", SOURCE)

    def test_expansion_is_bound_to_the_query(self):
        self.assertIn("const auto expanded = (query == _peerSearchQuery)", SOURCE)
        self.assertIn("_peerSearchExpanded = expanded;", SOURCE)
        self.assertIn("_hiddenPeerSearchResults.clear();", SOURCE)

    def test_global_request_can_return_more_than_the_preview(self):
        self.assertRegex(API_SOURCE, r"kGlobalPeersLimit = (?:[6-9]|[1-9][0-9]+)")
        self.assertRegex(API_SOURCE, r"\(_type == Type::WithSponsored\)\s+\? kGlobalPeersLimit")

    def test_removing_a_sponsored_row_refills_the_preview(self):
        removal = SOURCE.split("_sponsoredRemoved.emplace(peer);", 1)[1]
        self.assertIn("updateGlobalPeersPreview();", removal.split("refresh();", 1)[0])


if __name__ == "__main__":
    unittest.main()
