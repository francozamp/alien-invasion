import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to repesent a single alien in a fleet"""

    def __init__(self, settings, screen):
        """Initializes the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load alien image and set its rect attribute
        self.image = pygame.image.load("images/alien.bmp").convert()
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at this current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien right"""
        self.x += (self.settings.alien_speed_factor *
                   self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
