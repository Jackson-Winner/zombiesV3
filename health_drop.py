import pygame
import random
from game_parameters import (SCREEN_WIDTH, SCREEN_HEIGHT, BOMB_SIZE, CHANCE_BOMB_SPAWN,
                             ROAD_TILE_SIZE, GRASS_TILE_SIZE, CHANCE_HEART_SPAWN, MAX_HEARTS)


class Health(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/heart.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


hearts = pygame.sprite.Group()


def spawn_heart():
    heart_spawn = random.randint(0, CHANCE_BOMB_SPAWN)
    if heart_spawn == CHANCE_HEART_SPAWN and len(hearts) != MAX_HEARTS:
        hearts.add(Health(random.randint(GRASS_TILE_SIZE, SCREEN_WIDTH-GRASS_TILE_SIZE-BOMB_SIZE),
                          random.randint(ROAD_TILE_SIZE, SCREEN_HEIGHT-ROAD_TILE_SIZE-BOMB_SIZE)))
