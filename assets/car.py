import pygame
import random
from game_parameters import *
from background import *

pygame.init()
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(f"../zombies/assets/sprites/car{random.randint(0,3)}.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.car_rev = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(5, 8)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x
    def draw(self, surface):
        self.blit(self.image, self.rect)

cars = pygame.sprite.Group()
