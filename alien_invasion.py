import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    """Overall class to manage the assets and behaviour of game"""
    def __init__(self):
        pygame.init()
        self.settings  = Settings()
        self.bullets = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        #set the background color
        self.bg_color = (self.settings.bg_color)
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            #watch for keyboard and mouse events
            self._check_events()
            self.ship.update()  
            self.bullets.update()
            self._update_screen()
            
    def _check_events(self): 
        """Respond to keypresses and mouse events."""       
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                
                elif event.type == pygame.K_SPACE:
                     self._fire_bullet()
                    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pygame.K_q:
             sys.exit()
        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
            
        self.ship.blitme()
        #make the most recent drawn screen visible
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
             
        pygame.display.flip()
    
if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
