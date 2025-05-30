from project import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        else:
            return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                removed = self.remove_player("Pall")
                print(f"Type of removed: {type(removed)}")
                return player
        return f"Player {player_name} not found"
