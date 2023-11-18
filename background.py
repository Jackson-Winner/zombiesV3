import pygame
from game_parameters import SCREEN_WIDTH, SCREEN_HEIGHT, GRASS_TILE_SIZE, ROAD_TILE_SIZE


def draw_background(surface):

    # Load Files
    road = pygame.image.load("../zombies/assets/sprites/road.png").convert()
    grass = pygame.image.load("../zombies/assets/sprites/grass.png").convert()
    water_l = pygame.image.load("../zombies/assets/sprites/water_l.png").convert()
    water_r = pygame.image.load("../zombies/assets/sprites/water_r.png").convert()
    water_tl = pygame.image.load("../zombies/assets/sprites/water_tl.png").convert()
    water_tr = pygame.image.load("../zombies/assets/sprites/water_tr.png").convert()
    water_bl = pygame.image.load("../zombies/assets/sprites/water_bl.png").convert()
    water_br = pygame.image.load("../zombies/assets/sprites/water_br.png").convert()

    # Fill the Screen with grass
    for x in range(0, SCREEN_WIDTH, GRASS_TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT-ROAD_TILE_SIZE, GRASS_TILE_SIZE):
            surface.blit(grass, (x, y))
    # Fill Sides with water
    for y in range(ROAD_TILE_SIZE, SCREEN_HEIGHT-ROAD_TILE_SIZE, GRASS_TILE_SIZE):
        surface.blit(water_r, (SCREEN_WIDTH-GRASS_TILE_SIZE, y))
        surface.blit(water_l, (0, y))

    # Create corner water
    surface.blit(water_tl, (0, ROAD_TILE_SIZE))
    surface.blit(water_bl, (0, SCREEN_HEIGHT-2*ROAD_TILE_SIZE))
    surface.blit(water_tr, (SCREEN_WIDTH - GRASS_TILE_SIZE, ROAD_TILE_SIZE))
    surface.blit(water_br, (SCREEN_WIDTH - GRASS_TILE_SIZE, SCREEN_HEIGHT - 2*ROAD_TILE_SIZE))

    # Fill upper and lower borders with roads
    for x in range(0, SCREEN_WIDTH, GRASS_TILE_SIZE):
        surface.blit(road, (x, 0))
        surface.blit(road, (x, SCREEN_HEIGHT-ROAD_TILE_SIZE))


# Start Screen Zombie
start_screen_zombie = pygame.image.load("assets/sprites/zombie_icon.png")

# Life Icon
life_icon = pygame.image.load("assets/sprites/heart.png")
life_icon.set_colorkey((255, 255, 255))
