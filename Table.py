from Player import Player
from Move import Move
from Game import Game
from Card import Card

class Table:
    def __init__(self, listofplayes : list[Player], initial_stacks=100):
        self.players : list[Player] = listofplayes
        for player in self.players:
            player.stack = initial_stacks
        self.numberofgames : int = 0
        self.games : list[Game] = []
        self.current_game : Game = None
        
    def new_game(self):
        game = Game(self)
        self.games.append(game)
        self.current_game = game
        game.start_game(self)
    
    def add_player_stack(self, player: Player, amount: int):
        player.stack += amount
    
    
    

    
