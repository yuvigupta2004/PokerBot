from Player import Player
from Move import Move
from Game import Game
from Card import Card

class Table:
    def __init__(self, listofplayes : list[Player]):
        self.players : list[Player] = listofplayes
        self.pot : int = 0
        self.community_cards : list[Card] = []
        self.dealer_position : int = 0
        self.current_bet : int = 0
        self.minimum_raise : int = 0
        self.numberofhands : int = 0
        self.games : list[Game] = []
        
        
    def new_hand(self):
        self.pot = 0
        self.numberofhands += 1
        self.community_cards = []
        self.current_bet = 0
        self.minimum_raise = 0
        # Rotate dealer position
        self.dealer_position = (self.dealer_position + 1) % len(self.players)
    
    
    def deal_community_cards(self, stage):
        if stage == "flop":
            self.community_cards.extend(self.draw_cards(3))
        elif stage == "turn" or stage == "river":
            self.community_cards.extend(self.draw_cards(1))
    
    def do_move_from_player(self, player: Player):
        movebyplayer : Move = player.make_move(self)
        self.pot += movebyplayer.amount
        if movebyplayer.amount > self.current_bet:
            self.minimum_raise = movebyplayer.amount - self.current_bet
            self.current_bet = movebyplayer.amount

    
