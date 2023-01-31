class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializes de game's settings"""

        # TODO Save settings in a file
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_number = 0

        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def get_screen_size(self):
        return self.screen_width, self.screen_height
