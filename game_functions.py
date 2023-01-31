import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_events(settings, screen, ship, bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

            if event.key == pygame.K_SPACE:
                fire_bullet(bullets, screen, settings, ship)
            ship.current_movement.append(event.key)

        elif event.type == pygame.KEYUP:
            ship.current_movement.remove(event.key)


def update_screen(screen, settings, ship, aliens, bullets):
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)

    # Draw() on a group draws each element inside the group
    aliens.draw(screen)

    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Make the most recently drawn screen visible
    pygame.display.flip()


def fire_bullet(bullets, screen, settings, ship):
    if len(bullets) <= settings.bullet_number or \
            settings.bullet_number <= 0:
        # Create new bullet and add it to bullets group
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
        # print(len(bullets))


def update_bullets(bullets, aliens):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet position
    # This calls update for every sprite in the group
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))
    check_bullet_collisions(aliens, bullets)


def check_bullet_collisions(aliens, bullets):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def restart_if_needed(aliens, bullets, screen, settings, ship):
    if len(aliens) == 0:
        bullets.empty()
        # Create the fleet of aliens
        create_fleet(settings, screen, aliens, ship)


def create_fleet(settings, screen, aliens, ship):
    """Create full fleet of aliens"""
    # TODO: Put aliens in fleet class
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(alien_width, settings)
    number_rows = get_number_rows(settings, ship, alien)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        create_row(aliens, number_aliens_x, row_number, screen,
                   settings)


def create_row(aliens, number_aliens_x, row_number, screen, settings):
    for alien_number in range(number_aliens_x):
        create_alien(alien_number, aliens, screen, settings,
                     row_number)


def create_alien(alien_number, aliens, screen, settings, row_number):
    # Create an alien and place it in the row
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    # TODO: Improve this calculation so the row is centered
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height *
                    row_number)
    aliens.add(alien)


def get_number_aliens_x(alien_width, settings):
    # We use an alien's width as margin for each side
    available_space_x = settings.screen_width - 2 * alien_width
    # We use an alien's width as separation
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(settings, ship, alien):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (settings.screen_height -
                         (3 * alien.rect.height) - ship.rect.height)
    number_rows = int(available_space_y / (2 * alien.rect.height))
    return number_rows


def update_aliens(settings, stats, screen, ship, aliens, bullets):
    """Check if the fleet is at an edge,
    and then update the positions of all aliens in the fleet"""
    check_fleet_edges(settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)


def ship_hit(settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien"""
    # Decrement ships_left
    stats.ships_left -= 1

    # Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center ship
    create_fleet(settings, screen, aliens, ship)
    ship.center_ship()

    # Pause
    sleep(0.5)


def change_fleet_direction(settings, aliens):
    """Drop entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break
