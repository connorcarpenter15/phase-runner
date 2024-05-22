import pygame
from modules.levels import Level

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
GROUND_HEIGHT = SCREEN_HEIGHT - 15


class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """

    # -- Methods
    def __init__(self):
        """Constructor function"""

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        width = 40
        height = 60
        self.image = pygame.image.load("./images/character.png")
        self.image = pygame.transform.scale(self.image, (width, height))

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 10
        self.change_y = 0

        # List of sprites we can bump against
        self.level = Level(self)

        # for phaseing
        self.phase_status = False
        self.phase_energy = 100

        self.end_game = False

    def update(self):
        """Move the player."""
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )

        if not self.phase_status:
            block_hit_list += pygame.sprite.spritecollide(
                self, self.level.wall_list, False
            )

        for block in block_hit_list:
            # if we hit an object, move back to the left
            self.rect.right = block.rect.left

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False
        )

        if not self.phase_status:
            block_hit_list += pygame.sprite.spritecollide(
                self, self.level.wall_list, False
            )

        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """Calculate effect of gravity."""
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.6

        # See if we are on the ground.
        if self.rect.y >= GROUND_HEIGHT - self.rect.height and self.change_y >= 0:
            if not self.end_game:
                self.change_y = 0
                self.rect.y = GROUND_HEIGHT - self.rect.height

    def jump(self):
        """Called when user hits 'jump' button."""

        on_platform = False

        # check if player on top of wall or platform
        for platform in self.level.platform_list:
            if self.rect.bottom == platform.rect.top:
                on_platform = True

        for wall in self.level.wall_list:
            if self.rect.bottom == wall.rect.top:
                on_platform = True

        # If it is ok to jump, set our speed upwards
        if on_platform or self.rect.bottom >= GROUND_HEIGHT:
            self.change_y = -14

            jump_sound = pygame.mixer.Sound("./sounds/jump.mp3")
            jump_sound.play()

    # stop user
    def stop(self):
        """Called when the user lets off the keyboard."""
        self.change_x = 0

    # functionality for phase
    def phase(self):
        # phase if enough energy
        if self.phase_energy >= 0:
            self.phase_status = True

            # play phase sound effect
            phase_sound = pygame.mixer.Sound("./sounds/phase.mp3")
            phase_sound.play()
        else:
            self.phase_status = False

    def unphase(self):
        self.phase_status = False

    def enter_portal(self):
        self.stop()

        self.change_y += 6
        self.end_game = True
