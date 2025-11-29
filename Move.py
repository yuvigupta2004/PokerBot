from Player import Player

class Move:
    def __init__(self, player, action, amount):
        self.player = player  # Player making the move
        self.action = action  # e.g., "fold", "call", "raise", "bet"
        self.amount = amount  # Amount associated with the action, if applicable