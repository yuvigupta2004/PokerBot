from Player import Player
from Move import Move



class Game:
    def __init__(self):
        self.state = "not_started"
        self.winner : Player = None
        self.moves : list[Move] = []
    
    def start_game(self, table):
        self.state = "in_progress"
        table.new_hand()
        # Additional logic to start the game can be added here
        
    def add_move(self, move: Move):
        self.moves.append(move)
        
    def end_game(self, winner: Player):
        self.state = "ended"
        self.winner = winner
        # Additional logic to end the game can be added here