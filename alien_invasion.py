import sys
import pygame
from settings import Settings
class AlienInvasion:
    """Overall class to manage the assets and behaviour of game"""
    def __init__(self):
        pygame.init()
        self.settings  = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #set the background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            
            #make the most recent drawn screen visible
            pygame.display.flip()
    
if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
