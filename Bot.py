class Bot extends Player:
    def __init__(self, name, initial_stack=100):
        super().__init__(name, initial_stack)
        self.bot_strategy = "default"

    def make_decision(self, game_state):
        # Implement bot decision-making logic based on game state
        if game_state['current_bet'] > self.stack * 0.5:
            return "fold"
        elif game_state['current_bet'] == 0:
            return "raise"
        else:
            return "call"