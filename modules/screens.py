import pygame

# constants
TITLE_FONT_SIZE = 64
INSTRUCTION_FONT_SIZE = 24

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

TEXT_COLOR = (179, 222, 243)
FADED_TEXT_COLOR = (89, 111, 122)
BACKGROUND_COLOR = (18, 15, 40)

FONT_PATH = "./fonts/JetBrainsMonoNerdFont-Regular.ttf"


def draw_title_screen(screen):
    # create font
    instruction_font = pygame.font.Font(FONT_PATH, INSTRUCTION_FONT_SIZE)

    # add background image to screen
    background_image = pygame.image.load("./images/title-image.png").convert()
    background_image = pygame.transform.scale(
        background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    screen.blit(background_image, (0, 0))

    # add instruction text to screen
    line = "Press enter to start..."

    instruction_text = instruction_font.render(line, True, TEXT_COLOR)
    instruction_text_border = instruction_font.render(line, True, BACKGROUND_COLOR)

    # border text
    instruction_rect = instruction_text_border.get_rect(center=(501, 580))
    screen.blit(instruction_text, instruction_rect)

    instruction_rect = instruction_text_border.get_rect(center=(499, 580))
    screen.blit(instruction_text, instruction_rect)

    instruction_rect = instruction_text_border.get_rect(center=(500, 579))
    screen.blit(instruction_text, instruction_rect)

    instruction_rect = instruction_text_border.get_rect(center=(500, 581))
    screen.blit(instruction_text, instruction_rect)

    # actual text
    instruction_rect = instruction_text.get_rect(center=(500, 580))
    screen.blit(instruction_text, instruction_rect)

    # update game
    pygame.display.flip()


def draw_menu_screen(screen, completed_levels):
    # draw background
    screen.fill(BACKGROUND_COLOR)

    # load fonts
    title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
    text_font = pygame.font.Font(FONT_PATH, INSTRUCTION_FONT_SIZE)

    # add menu title
    menu_text = title_font.render("Menu", True, TEXT_COLOR)
    menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
    screen.blit(menu_text, menu_rect)

    # add input options
    level_text = text_font.render("Press:", True, TEXT_COLOR)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
    screen.blit(level_text, level_rect)

    level_text = text_font.render("1) Level 1", True, TEXT_COLOR)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2, 250))
    screen.blit(level_text, level_rect)

    LEVEL_2_COLOR = TEXT_COLOR if 1 in completed_levels else FADED_TEXT_COLOR

    level_text = text_font.render("2) Level 2", True, LEVEL_2_COLOR)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2, 300))
    screen.blit(level_text, level_rect)

    LEVEL_3_COLOR = TEXT_COLOR if 2 in completed_levels else FADED_TEXT_COLOR

    level_text = text_font.render("3) Level 3", True, LEVEL_3_COLOR)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2, 350))
    screen.blit(level_text, level_rect)

    level_text = text_font.render("H) Help", True, TEXT_COLOR)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2, 450))
    screen.blit(level_text, level_rect)

    level_text = text_font.render("Q) Quit", True, TEXT_COLOR)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2, 500))
    screen.blit(level_text, level_rect)

    # update game
    pygame.display.flip()


def draw_help_screen(screen):
    # draw background
    screen.fill((18, 15, 40))

    # load fonts
    title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
    text_font = pygame.font.Font(FONT_PATH, INSTRUCTION_FONT_SIZE)

    # add menu title
    help_text = title_font.render("Help", True, TEXT_COLOR)
    help_rect = help_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
    screen.blit(help_text, help_rect)

    # add help text
    help_text = text_font.render(
        "The goal of the game is to reach the end of the level.", True, TEXT_COLOR
    )
    help_rect = help_text.get_rect(center=(SCREEN_WIDTH / 2, 200))
    screen.blit(help_text, help_rect)

    help_text = text_font.render(
        "Avoid hitting walls and platforms by jumping with <space>,", True, TEXT_COLOR
    )
    help_rect = help_text.get_rect(center=(SCREEN_WIDTH / 2, 240))
    screen.blit(help_text, help_rect)

    help_text = text_font.render(
        "or phasing with <shift>.",
        True,
        TEXT_COLOR,
    )
    help_rect = help_text.get_rect(center=(SCREEN_WIDTH / 2, 280))
    screen.blit(help_text, help_rect)

    help_text = text_font.render(
        "You have a limited amount phase energy per level, so use it wisely!",
        True,
        TEXT_COLOR,
    )
    help_rect = help_text.get_rect(center=(SCREEN_WIDTH / 2, 320))
    screen.blit(help_text, help_rect)

    # add input options
    input_text = text_font.render("Press:", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 400))
    screen.blit(input_text, input_rect)

    input_text = text_font.render("M) Menu", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 450))
    screen.blit(input_text, input_rect)

    input_text = text_font.render("Q) Quit", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 500))
    screen.blit(input_text, input_rect)

    pygame.display.flip()


def draw_level_complete_screen(screen, current_level_no):
    # draw background
    screen.fill((18, 15, 40))

    # load fonts
    title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
    text_font = pygame.font.Font(FONT_PATH, INSTRUCTION_FONT_SIZE)

    # add game over title
    level_complete_text = title_font.render(
        f"Level {current_level_no+1} Complete!", True, TEXT_COLOR
    )
    level_complete_rect = level_complete_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
    screen.blit(level_complete_text, level_complete_rect)

    # add input options
    input_text = text_font.render("Press:", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 400))
    screen.blit(input_text, input_rect)

    input_text = text_font.render("M) Menu", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 450))
    screen.blit(input_text, input_rect)

    input_text = text_font.render("Q) Quit", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 500))
    screen.blit(input_text, input_rect)

    # update game
    pygame.display.flip()


def draw_game_over_screen(screen):
    # draw background
    screen.fill((18, 15, 40))

    # load fonts
    title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
    text_font = pygame.font.Font(FONT_PATH, INSTRUCTION_FONT_SIZE)

    # add game over title
    game_over_text = title_font.render("Game Over...", True, TEXT_COLOR)
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
    screen.blit(game_over_text, game_over_rect)

    # add input options
    input_text = text_font.render("Press:", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 400))
    screen.blit(input_text, input_rect)

    input_text = text_font.render("M) Menu", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 450))
    screen.blit(input_text, input_rect)

    input_text = text_font.render("Q) Quit", True, TEXT_COLOR)
    input_rect = input_text.get_rect(center=(SCREEN_WIDTH / 2, 500))
    screen.blit(input_text, input_rect)
