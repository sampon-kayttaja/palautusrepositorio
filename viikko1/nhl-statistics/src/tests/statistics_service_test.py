import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_finds_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_returns_none_for_missing_player(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]
        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("XXX"), [])

    def test_top_sorted_by_points_by_default(self):
        names = [p.name for p in self.stats.top(2)]
        self.assertEqual(names, ["Gretzky", "Lemieux"])

    def test_top_sorted_by_goals(self):
        names = [p.name for p in self.stats.top(2, SortBy.GOALS)]
        self.assertEqual(names, ["Lemieux", "Yzerman"])

    def test_top_sorted_by_assists(self):
        names = [p.name for p in self.stats.top(2, SortBy.ASSISTS)]
        self.assertEqual(names, ["Gretzky", "Yzerman"])

    def test_top_returns_correct_amount(self):
        self.assertEqual(len(self.stats.top(2)), 2)