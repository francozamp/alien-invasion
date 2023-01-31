import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    """Initialize game and create screen object"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.get_screen_size())
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics
    stats = GameStats(settings)
    # Make ship
    ship = Ship(screen, settings)
    # Make group to store bullets in
    bullets = Group()  # Groups all bullets
    aliens = Group()
    # Make an alien

    # Start main loop for the game
    while True:
        gf.restart_if_needed(aliens, bullets, screen, settings, ship)
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(screen, settings, ship, aliens, bullets)


run_game()
