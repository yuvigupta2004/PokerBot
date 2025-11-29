from Player import Player

class Bot(Player):
    def __init__(self, name, initial_stack=100):
        super().__init__(name, initial_stack)
        self.bot_strategy = "default"

    