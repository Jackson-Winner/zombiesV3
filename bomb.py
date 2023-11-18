import pygame
import random
from game_parameters import (SCREEN_WIDTH, SCREEN_HEIGHT, ROAD_TILE_SIZE,
                             GRASS_TILE_SIZE, BOMB_SIZE, CHANCE_BOMB_SPAWN, MAX_NUKES)


class Bomb(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/bomb.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


nukes = pygame.sprite.Group()


def spawn_nuke():
    bomb_spawn = random.randint(0, CHANCE_BOMB_SPAWN)
    if bomb_spawn == CHANCE_BOMB_SPAWN and len(nukes) != MAX_NUKES:
        nukes.add(Bomb(random.randint(GRASS_TILE_SIZE, SCREEN_WIDTH-GRASS_TILE_SIZE-BOMB_SIZE),
                       random.randint(ROAD_TILE_SIZE, SCREEN_HEIGHT-ROAD_TILE_SIZE-BOMB_SIZE)))
