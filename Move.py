from Player import Player

class Move:
    def __init__(self):
        self.player = None  # Player making the move
        self.action = None  # e.g., "fold", "call", "raise"
        self.amount = 0     # Amount associated with the action, if applicable