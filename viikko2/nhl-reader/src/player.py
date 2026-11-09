class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.team = player_data['team']
        self.nationality = player_data['nationality']
        self.goals = player_data['goals']
        self.assists = player_data['assists']
        self.games = player_data['games']
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name} ({self.team}) - {self.nationality} - Goals: {self.goals}, Assists: {self.assists}, Points: {self.points}"
