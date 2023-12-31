import sys
import pygame
from game_parameters import SCREEN_WIDTH, SCREEN_HEIGHT, GRASS_TILE_SIZE, ROAD_TILE_SIZE, MAX_SPEED

pygame.mixer.init()
pygame.joystick.init()

try:
    joystick = pygame.joystick.Joystick(0)
except pygame.error:
    print("Please connect a controller or it won't work!")
    pygame.quit()
    sys.exit()

print(f"{joystick.get_name()} Connected \nPower Level: {joystick.get_power_level()}")
hurt = pygame.mixer.Sound("assets/sounds/hurt.wav")


# Create class for player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # TODO Flip fish if going other way
        self.image = pygame.image.load("../zombies/assets/sprites/player.png")
        self.rect = self.image.get_rect()
        self.player_x = SCREEN_WIDTH/2
        self.player_y = SCREEN_HEIGHT/2
        self.X_CHANGE = 0
        self.Y_CHANGE = 0
        self.MAX_SPEED = MAX_SPEED

    def move(self):

        x_value = joystick.get_axis(0)
        y_value = joystick.get_axis(1)

        # Compensate for stick drift
        if abs(x_value) < 0.1:
            x_value = 0
        if abs(y_value) < 0.1:
            y_value = 0

        self.X_CHANGE = x_value * self.MAX_SPEED
        self.Y_CHANGE = y_value * self.MAX_SPEED

        self.player_x += self.X_CHANGE
        self.player_y += self.Y_CHANGE

        # Bound the Player to the play area
        if self.player_x >= SCREEN_WIDTH - 2 * GRASS_TILE_SIZE:
            self.player_x = SCREEN_WIDTH - 2 * GRASS_TILE_SIZE
        elif self.player_x < GRASS_TILE_SIZE:
            self.player_x = GRASS_TILE_SIZE

        if self.player_y >= SCREEN_HEIGHT - 2 * ROAD_TILE_SIZE:
            self.player_y = SCREEN_HEIGHT - 2 * ROAD_TILE_SIZE
        elif self.player_y < ROAD_TILE_SIZE:
            self.player_y = ROAD_TILE_SIZE

        self.rect.x = self.player_x
        self.rect.y = self.player_y

    def draw(self, surface):
        surface.blit(self.image, (self.player_x, self.player_y))


# Create an instance of the Player class
player = Player()
