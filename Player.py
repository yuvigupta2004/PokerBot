from Card import Card

class PlayerStats: 
    def __init__(self):
        self.vpip = 0
        self.cbet = 0
        self.foldto3bet = 0
        self.pfr = 0
        self.goestoshowdown = 0
        self.winpercentageatshowdown = 0
        self.hands_played = 0
        self.hands_won = 0
        self.PnL = 0
        self.stack = 0
        
class Player:
    def __init__(self, name):
        self.name = name
        self.stats = PlayerStats()
        self.hand : list[Card, Card] = None  
        self.current_bet = 0 
        self.isactive = True  # Whether the player is still in the current hand
    
        

