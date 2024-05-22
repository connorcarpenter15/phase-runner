import pygame

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Platform(pygame.sprite.Sprite):
    """Platform the user can jump on"""

    def __init__(self, width, height):
        """Platform constructor. Assumes constructed with user passing in
        an array of 5 numbers like what's defined at the top of this code.
        """
        super().__init__()

        self.image = pygame.image.load("./images/platform.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()

        self.player = None
        self.rect = self.image.get_rect()


class Wall(pygame.sprite.Sprite):
    """Wall that blocks movement"""

    def __init__(self, width, height):
        """Wall constructor. Assumes constructed with user passing in
        an array of 5 numbers like what's defined at the top of this code.
        """
        super().__init__()

        self.image = pygame.image.load("./images/wall.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()

        self.player = None
        self.rect = self.image.get_rect()


class Portal(pygame.sprite.Sprite):
    "Portal at the end of the level"

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/end-portal.png")
        self.image = pygame.transform.scale(self.image, (200, 250)).convert_alpha()

        self.player = None
        self.rect = self.image.get_rect()
        self.rect.y = 390
