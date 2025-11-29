from Player import Player

class Table:
    def __init__(self, listofplayes : list[Player]):
        self.players = listofplayes
        self.pot = 0
        self.community_cards = []
        self.dealer_position = 0
        self.current_bet = 0
        self.minimum_raise = 0
        
    def new_hand(self):
        self.pot = 0
        self.community_cards = []
        self.current_bet = 0
        self.minimum_raise = 0
        # Rotate dealer position
        self.dealer_position = (self.dealer_position + 1) % len(self.players)
    
    