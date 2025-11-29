from Player import Player
from Move import Move
from Table import Table
from Card import Card
from Deck import Deck

class Game:
    def __init__(self, table : Table):
        self.state = "not_started"
        self.winner : Player = None
        self.moves : list[Move] = []
        self.table = table
        self.community_cards : list[Card] = []
        self.deck = Deck()
    
    def start_game(self, table):
        self.state = "in_progress"
        table.current_game = self
        self.deck.shuffle()
        
        
    def add_move(self, move: Move):
        self.moves.append(move)
        
    def deal_hands(self):
        for player in self.table.players:
            player.hand = self.deck.deal(2)
        
    def end_game(self, winner: Player):
        self.state = "ended"
        self.winner = winner
        self.table.current_game = None
        self.table.numberofgames += 1