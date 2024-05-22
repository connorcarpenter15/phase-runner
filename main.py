import pygame
import time

from pygame.constants import K_RSHIFT
from modules.levels import BACKGROUND_COLOR, Level_01, Level_02, Level_03
from modules.player import Player
from modules.screens import (
    draw_menu_screen,
    draw_title_screen,
    draw_help_screen,
    draw_game_over_screen,
    draw_level_complete_screen,
)
from modules.draw import draw_bordered_rounded_rect
import sys

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

TEXT_COLOR = (179, 222, 243)
BAR_COLOR = (67, 222, 243)

TITLE_FONT_SIZE = 64
INSTRUCTION_FONT_SIZE = 24

FONT_PATH = "./fonts/JetBrainsMonoNerdFont-Regular.ttf"

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


"""Main Program"""
pygame.init()
pygame.font.init()

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

current_screen = "title"
current_level_no = 0

completed_levels = []


# ---------- Main Loop -----------
def input_loop():
    game = False
    global current_level_no
    global current_screen
    global completed_levels

    pygame.mixer.music.load("./sounds/music.mp3")
    pygame.mixer.music.play(-1)

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))

    while not game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if current_screen == "title" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    current_screen = "menu"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if current_screen == "menu" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_level_no = 0
                    game = True
                elif event.key == pygame.K_2:
                    current_level_no = 1
                    if current_level_no in completed_levels:
                        game = True
                elif event.key == pygame.K_3:
                    current_level_no = 2
                    if current_level_no in completed_levels:
                        game = True
                elif event.key == pygame.K_h:
                    current_screen = "help"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if (
                current_screen == "help"
                or current_screen == "game_over"
                or current_screen == "level_complete"
            ) and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    current_screen = "menu"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        if current_screen == "title":
            draw_title_screen(screen)
        elif current_screen == "menu":
            draw_menu_screen(screen, completed_levels)
        elif current_screen == "help":
            draw_help_screen(screen)
        elif current_screen == "game_over":
            draw_game_over_screen(screen)
        elif current_screen == "level_complete":
            draw_level_complete_screen(screen, current_level_no)

        pygame.display.flip()

        clock.tick(60)

    # Set the current level
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 0
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    result = game_loop(
        player,
        active_sprite_list,
        current_level,
        current_level_no,
        screen,
        clock,
    )

    if result:
        current_screen = "level_complete"
        completed_levels.append(current_level_no + 1)
    else:
        current_screen = "game_over"

    input_loop()


def game_loop(
    player,
    active_sprite_list,
    current_level,
    current_level_no,
    screen,
    clock,
):
    # load game music
    pygame.mixer.music.stop()
    pygame.mixer.music.load("./sounds/game_music.mp3")
    pygame.mixer.music.play(-1)

    # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.phase()
                if event.key == pygame.K_SPACE:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    player.unphase()

        # Update phase energy
        if player.phase_status:
            player.phase_energy -= 0.5

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # move world at constant pace
        if screen.get_rect().right == current_level.portal.rect.right:
            player.rect.x += 5
        else:
            current_level.shift_world(-5)

        # stop moving player after start of level
        if player.rect.x > 400:
            player.change_x = 0

        # check if player dies
        if player.rect.right < -1:
            # game over
            game_over_sound = pygame.mixer.Sound("./sounds/game_over.mp3")
            game_over_sound.play()

            return False

        # check if player hits portal
        if player.rect.x + player.rect.width >= current_level.portal.rect.centerx:
            player.enter_portal()

            portal_sound = pygame.mixer.Sound("./sounds/portal.mp3")
            portal_sound.play()

            if player.rect.y > 10000:
                return True

        # draw obstacles and player
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # draw phase bar
        bar_width = 300
        bar_height = 30
        bar_position = (SCREEN_WIDTH - bar_width - 20, 20)

        current_bar_width = (player.phase_energy / 100) * bar_width
        draw_bordered_rounded_rect(
            screen,
            (bar_position[0], bar_position[1], bar_width, bar_height),
            BACKGROUND_COLOR,
            BAR_COLOR,
            5,
            5,
        )

        if current_bar_width > 0:
            pygame.draw.rect(
                screen,
                BAR_COLOR,
                (
                    bar_position[0] + 1,
                    bar_position[1] + 1,
                    current_bar_width - 2,
                    bar_height - 2,
                ),
            )

        # Draw Level number
        level_text = pygame.font.Font(FONT_PATH, INSTRUCTION_FONT_SIZE).render(
            "LEVEL " + str(current_level_no + 1), True, TEXT_COLOR
        )
        level_text_rect = level_text.get_rect(center=(100, 50))
        screen.blit(level_text, level_text_rect)

        # Limit to 60 frames per second
        clock.tick(60)

        pygame.display.flip()


if __name__ == "__main__":
    input_loop()
    pygame.quit()
