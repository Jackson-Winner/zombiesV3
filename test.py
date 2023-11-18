import pygame
pygame.init()

display = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

GRAY = pygame.Color('gray12')

display_width, display_height = display.get_size()

x = display_width * 0.45
y = display_height * 0.8

x_change = 0
y_change = 0
image = pygame.image.load("../zombies/assets/sprites/player.png")
max_speed = 6
crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    keys = pygame.key.get_pressed()

    # handle left and right movement
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        x_change = -max_speed
    elif keys[pygame.K_d] and not keys[pygame.K_a]:
        x_change = max_speed
    else:
        x_change = 0

    # handle up and down movement
    if keys[pygame.K_w] and not keys[pygame.K_s]:
        y_change = -max_speed
    elif keys[pygame.K_s] and not keys[pygame.K_w]:
        y_change = max_speed
    else:
        y_change = 0

    x += x_change  # Move the object.
    y += y_change

    display.fill(GRAY)
    #pygame.draw.rect(display, (0, 120, 250), (x, y, 20, 40))
    display.blit(image, (x,y))
    pygame.display.update()
    clock.tick(60)