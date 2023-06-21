class Settings:
    """A class to store all settings of Alien Invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        # Ship settings
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bullet_height =3 
        self.bullet_width = 15
        self.bullet_color = (210, 220, 230)