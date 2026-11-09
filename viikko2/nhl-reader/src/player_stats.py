class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
        self.players.sort(key=lambda player: player.points, reverse=True)


    def top_players(self, country):
        result = self.players

        result = [player for player in result if player.nationality == country]

        return result
