class Guild:
    name: str
    players: list

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'

        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        if self.players:
            player = [x for x in self.players if x.name == player_name][0]
            if player:
                player.guild = 'Unaffiliated'
                self.players.remove(player)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        data = f'Guild: {self.name}\n'
        for player in self.players:
            data += f'{player.player_info()}'

        return data
