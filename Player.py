class Player:
    def __init__(self, name, initial_stack=100):
        self.name = name
        self.stack = initial_stack
        self.vpip = 0
        self.cbet = 0
        self.foldto3bet = 0
        self.pfr = 0
        self.goestoshowdown = 0
        self.winpercentageatshowdown = 0
        self.hands_played = 0
        self.hands_won = 0
        self.PnL = 0
        

