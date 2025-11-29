from Player import Player
from Move import Move
from Table import Table
from Card import Card
from Deck import Deck

class Game:
    def __init__(self, table : Table):
        self.winner : Player = None
        self.moves : list[Move] = []
        self.table = table
        self.community_cards : list[Card] = []
        self.deck = Deck()
        self.pot = 0
        
    
    def start_game(self, table):
        table.current_game = self
        self.deck.shuffle()
        self.pot = 0
        self.community_cards = []
        
        for player in self.table.players:
            player.hand = None
            player.current_bet = 0
            player.isactive = True
        
        self.deal_hands()
        self.take_preflopbets()
        
        self.deal_flop()
        self.take_flop()
        
        self.deal_turn()
        self.take_turn()

        self.deal_river()
        self.take_river()
        
        self.winner = self.determine_winner()
        self.end_game()
        
        
    def determine_winner(self) -> Player:
        pass
        
    def add_move(self, move: Move):
        self.moves.append(move)
        
    def deal_hands(self):
        for player in self.table.players:
            player.hand = self.deck.deal(2)
            
    def deal_flop(self):
        self.community_cards.extend(self.deck.deal(3))
    def deal_turn(self):
        self.community_cards.extend(self.deck.deal(1))
    def deal_river(self):
        self.community_cards.extend(self.deck.deal(1))
        
    def take_preflopbets(self):
        pass

    def take_flop(self):
        pass
    
    def take_turn(self):
        pass
    
    def take_river(self):
        pass
    
    
    def end_game(self):
        self.table.current_game = None
        self.table.numberofgames += 1
        self.winner.stack += self.pot