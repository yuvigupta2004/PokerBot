from Card import Card

class Deck:
    def __init__(self):
        self.cards : list[Card] = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def deal(self, num_cards: int) -> list[Card]:
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards