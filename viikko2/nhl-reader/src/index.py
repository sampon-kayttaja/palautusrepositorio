from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats
from fill_table import fill_table

def main():
    season = Prompt.ask("Season:", choices=["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"])

    url = "https://studies.cs.helsinki.fi/nhlstats/" + season + "/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    countries = ['USA', 'RUS', 'CHE', 'CZE', 'FRA', 'DEU', 'CAN', 'AUS', 'SWE', 'NOR', 'SVK', 'AUT', 'DNK', 'BLR', 'LVA', 'FIN']
    country = Prompt.ask("Nationality:", choices=countries)

    result = stats.top_players(country)

    table = Table(title="Top Players from " + country + " in " + season)

    Console().print(fill_table(table, result))

if __name__ == "__main__":
    main()
