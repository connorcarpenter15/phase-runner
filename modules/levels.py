import pygame
from modules.platforms import Platform, Wall, Portal

# Global constants

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BACKGROUND_COLOR = (18, 15, 40)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Level:
    """This is a generic super-class used to define a level.
    Create a child class for each level with level-specific
    info."""

    def __init__(self, player):
        """Constructor. Pass in a handle to player. Needed for when moving
        platforms collide with the player."""
        self.platform_list = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

        self.portal = Portal()
        self.portal_list = pygame.sprite.Group()
        self.portal_list.add(self.portal)

        self.player = player
        self.status = False

        # How far this world has been scrolled left/right
        self.world_shift = 0

    # Update everythign on this level
    def update(self):
        """Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.wall_list.update()
        self.portal_list.update()

    def draw(self, screen):
        """Draw everything on this level."""

        # Draw the background
        screen.fill(BACKGROUND_COLOR)

        background_image = pygame.image.load("./images/bg_image.png")
        screen.blit(background_image, [0, 0])

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.wall_list.draw(screen)
        self.enemy_list.draw(screen)
        self.portal_list.draw(screen)

    def shift_world(self, shift_x):
        """When the user moves left/right and we need to scroll
        everything:"""

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for wall in self.wall_list:
            wall.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for portal in self.portal_list:
            portal.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """Definition for level 1."""

    def __init__(self, player):
        """Create level 1."""

        # Call the parent constructor
        super().__init__(player)

        # Array with width, height, x, and y of platform
        platforms = [
            [210, 70, 1000, 500],
            [200, 50, 1300, 400],
            [210, 70, 1500, 500],
            [210, 70, 1620, 280],
            [150, 70, 1950, 150],
            [300, 50, 2000, 500],
            [200, 60, 2300, 200],
            [200, 60, 2600, 350],
        ]

        walls = [
            [30, 220, 1590, 280],
            [40, 325, 2300, 260],
            [30, 100, 2470, 140],
            [30, 95, 2670, 490],
            [40, 135, 3100, 450],
        ]

        self.portal.rect.x = 4000
        self.portal.player = player

        # Go through the array above and add platforms
        for platform in platforms:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for wall in walls:
            block = Wall(wall[0], wall[1])
            block.rect.x = wall[2]
            block.rect.y = wall[3]
            block.player = self.player
            self.wall_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """Definition for level 2."""

    def __init__(self, player):
        """Create level 2."""

        # Call the parent constructor
        Level.__init__(self, player)

        # width, height, x, y
        platforms = [
            # player can jump about 150 (starts at 580ish at ground level)
            [210, 30, 1000, 430],
            [210, 30, 1300, 280],
            [210, 30, 1600, 130],  # 430 is the max that the player can jump
            [150, 30, 1900, 250],  # down a lil
            [150, 30, 2100, 100],  # higher smaller one
            [150, 30, 2400, 300],  # down a lil more
            [150, 30, 2550, 450],  # down a lil more
            [500, 30, 2700, 300],  # long one (put a wall on top) TODO
            [500, 30, 2900, 200],  # duplicate platform above
        ]

        walls = [
            # width, height, x, y
            # w, h,   x,    y
            [30, 125, 1100, 460],
            [30, 275, 1390, 310],
            [205, 435, 1600, 150],  # fat one
            [30, 305, 1960, 280],
            [30, 455, 2160, 130],  # for higher smaller one
            [30, 100, 2400, 200],  # L shape
            [30, 285, 3500, 300],  # steps begin
            [30, 235, 3600, 350],
            [30, 185, 3700, 400],
            [30, 135, 3800, 450],
        ]

        self.portal.rect.x = 4700
        self.portal.player = player

        # Go through the array above and add platforms
        for platform in platforms:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for wall in walls:
            block = Wall(wall[0], wall[1])
            block.rect.x = wall[2]
            block.rect.y = wall[3]
            block.player = self.player
            self.wall_list.add(block)


class Level_03(Level):
    """Definition for level 3."""

    def __init__(self, player):
        """Create level 3."""

        # Call the parent constructor
        Level.__init__(self, player)

        # width, height, x, y
        platforms = [
            # player can jump about 150 (starts at 580ish at ground level)
            [200, 30, 2000, 430],
            [200, 30, 2230, 300],
            [100, 50, 2500, 150],
            [200, 30, 2750, 400],
            [300, 30, 2800, 100],
        ]

        walls = [
            # width, height, x, y
            # w, h,   x,    y
            [60, 135, 1000, 450],  # steps begin
            [60, 185, 1250, 400],
            [60, 235, 1500, 350],
            [60, 285, 1750, 300],
            [30, 200, 2200, 0],
            [30, 300, 2200, 300],
            [30, 400, 2535, 200],
            [200, 155, 2750, 430],
            [40, 100, 3060, 0],
        ]

        self.portal.rect.x = 4700
        self.portal.player = player

        # Go through the array above and add platforms
        for platform in platforms:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for wall in walls:
            block = Wall(wall[0], wall[1])
            block.rect.x = wall[2]
            block.rect.y = wall[3]
            block.player = self.player
            self.wall_list.add(block)
