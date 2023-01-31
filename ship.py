import pygame

BOTTOM_SEPARATION = 25


class Ship:

    def __init__(self, screen, settings):
        """Initialize the ship and set its stating position"""
        self.screen = screen  # Screen where the ship will be drawn

        # Load ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp").convert()
        self.rect = self.image.get_rect()  # Image rectangle
        self.screen_rect = screen.get_rect()  # Screen rectangle

        # Start each new ship at the bottom center of the screen.
        self.center_ship()

        self.speed = settings.ship_speed_factor

        self.current_movement = []

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.move_right():
            self.center_x += self.speed

        if self.move_left():
            self.center_x -= self.speed

        if self.move_up():
            self.center_y -= self.speed

        if self.move_down():
            self.center_y += self.speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def move_right(self):
        return pygame.K_RIGHT in self.current_movement \
               and self.rect.right < self.screen_rect.right

    def move_left(self):
        return pygame.K_LEFT in self.current_movement \
               and self.rect.left > self.screen_rect.left

    def move_up(self):
        return pygame.K_UP in self.current_movement \
               and self.rect.top > self.screen_rect.top

    def move_down(self):
        return pygame.K_DOWN in self.current_movement \
               and self.rect.bottom < self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - BOTTOM_SEPARATION

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)