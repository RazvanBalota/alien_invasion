import sys 

import pygame 

from settings import Settings
from ship import Ship

class AlienInvasion: 
    """Overall class to manage game assets and behavior"""
    def __init__(self): 
        """Init game""" 
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

        self.bg_color = (230, 230, 230)

    def run_game(self): 
        """Start main loop of game""" 
        while True: 
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and filp to the new screen"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()
    
if __name__ == '__main__': 
    ai = AlienInvasion() 
    ai.run_game()