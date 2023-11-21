import pygame
import random
import math
import time
from game_parameters import (ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED, GRASS_TILE_SIZE,
                             ROAD_TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, COOLDOWN_TIME)
from player import player


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../zombies/assets/sprites/zombie.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(GRASS_TILE_SIZE, SCREEN_WIDTH - 2 * GRASS_TILE_SIZE)
        random_number = random.randint(0, 1)
        if random_number == 0:
            self.rect.y = -GRASS_TILE_SIZE
        elif random_number == 1:
            self.rect.y = SCREEN_HEIGHT

    def update(self):
        # Find displacement (dx, dy) between enemy and player.
        dx = player.player_x - self.rect.x
        dy = player.player_y - self.rect.y
        dist = math.hypot(dx, dy)
        # Make dx,dy normal vectors
        dx = dx / dist
        dy = dy / dist
        # Move along this normal vector towards the player at a random speed.
        self.rect.x += dx * random.uniform(ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED)
        self.rect.y += dy * random.uniform(ZOMBIE_MIN_SPEED, ZOMBIE_MAX_SPEED)


# Create a sprite group for the zombies
enemies = pygame.sprite.Group()


# This creates a function so that you can choose how many enemies spawn at once and in total
def add_enemies(total, amount):

    if len(enemies) < total:
        for _ in range(amount):
            enemies.add(Enemy())


class Delay:

    def __init__(self, wait=1):
        self.last = time.time()
        self.wait = wait

    def spawn(self, total, amount):
        # Spawn zombie only after 1 second
        now = time.time()
        if now - self.last >= self.wait:
            self.last = now
            add_enemies(total, amount)


cooldown = Delay(COOLDOWN_TIME)
