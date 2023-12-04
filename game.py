import pygame.mixer

from background import *
from player import *
from enemy import *
from bomb import *
from health_drop import *
from game_parameters import *

# Initialize pygame
pygame.init()
main_menu_music = pygame.mixer.Sound("assets/sounds/doom.mp3")
music = pygame.mixer.Sound("assets/sounds/lastofus.mp3")
bomb_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")
heart_sound = pygame.mixer.Sound("assets/sounds/heart.mp3")

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RUN!")
start_font = pygame.font.Font("assets/fonts/game_font.ttf", 64)
instructions_font = pygame.font.Font("assets/fonts/game_font.ttf", 32)
game_over_font = pygame.font.Font("assets/fonts/game_font.ttf", 40)

# Clock objects
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

# Create Player stuff
health = GAME_HEALTH
score = 0
highscore = 0

while running:

    # Start Menu
    start = True
    pygame.mixer.Sound.play(main_menu_music)
    while start:

        # Display Title and start instructions
        screen.fill((0, 0, 0))
        message = start_font.render("ZOMBIE RUN!", True, (255, 0, 0))
        screen.blit(message, (SCREEN_WIDTH / 2 - message.get_width() / 2,
                              SCREEN_HEIGHT / 2 - message.get_height() / 2))
        instructions = instructions_font.render("Use the controller and press A to start",
                                                True, (255, 0, 0))
        screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2,
                                   (SCREEN_HEIGHT / 2 - instructions.get_height() / 2) + message.get_height()))
        screen.blit(start_screen_zombie, (SCREEN_WIDTH/2 - start_screen_zombie.get_width()/2, 20))

        # Flip the display
        pygame.display.flip()

        # Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                sys.exit()

        # Start Game and change modifiers
        if joystick.get_button(0) == True:
            score_last = time.time()
            difficulty_last = time.time()
            pygame.mixer.Sound.stop(main_menu_music)
            pygame.mixer.Sound.play(music)
            start = False

    # Logic for when the player is alive
    while health > 0:
        # Close Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Start background music
        if score_last == 0:
            pygame.mixer.Sound.start(music)

        # Draw Background
        screen.blit(background, (0, 0))

        # Draw Bombs and Heart drops
        spawn_nuke()
        spawn_heart()

        # Explode bomb if collided
        if nukes:
            nukes.draw(screen)
            result_bomb = pygame.sprite.spritecollide(player, nukes, True)
            if result_bomb:
                pygame.mixer.Sound.play(bomb_sound)
                enemies.empty()
                nukes.empty()

        # Add health if collided
        if hearts:
            hearts.draw(screen)
            result_heart = pygame.sprite.spritecollide(player, hearts, True)
            if result_heart:
                pygame.mixer.Sound.play(heart_sound)
                health += len(result_heart)

        # Show the score
        score_now = time.time()
        score_timer = int(score_now) - int(score_last)
        if score_timer >= SCORE_INTERVAL:
            score += 1
            score_last = time.time()
        if score > highscore:
            highscore = score

        score_text = game_over_font.render(f"Score: {score}", True, (255, 0, 0))
        screen.blit(score_text, (SCREEN_WIDTH - GRASS_TILE_SIZE - score_text.get_width(), ROAD_TILE_SIZE))
        highscore_text = game_over_font.render(f"Highscore: {highscore}", True, (255, 0, 0))
        screen.blit(highscore_text, (GRASS_TILE_SIZE, ROAD_TILE_SIZE))

        # Draw health icons
        for i in range(health):
            screen.blit(life_icon, ((i * GRASS_TILE_SIZE) + GRASS_TILE_SIZE, SCREEN_HEIGHT - 2*ROAD_TILE_SIZE))

        # Difficulty increases every 30 seconds
        difficulty_now = score_now
        difficulty_timer = int(difficulty_now) - int(difficulty_last)
        if difficulty_timer >= DIFFICULTY_INTERVAL:
            SPAWN_PER_INSTANCE += 1
            difficulty_last = time.time()

        # Add enemies to screen
        cooldown.spawn(TOTAL_ZOMBIES, SPAWN_PER_INSTANCE)

        # Updates the positions of all sprites
        player.move()
        enemies.update()

        # Check for enemy collisions with the player
        result_enemy = pygame.sprite.spritecollide(player, enemies, True)
        if result_enemy:
            pygame.mixer.Sound.play(hurt)
            health -= 1

        # Draw the Player and the enemies
        player.draw(screen)
        enemies.draw(screen)

        # Update the display
        pygame.display.update()

        # Limit Frame Rate
        clock.tick(60)
    dead = True
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Set screen to black
        screen.fill((0, 0, 0))

        # Display the game over text
        message_game_over = game_over_font.render("GAME OVER!", True, (255, 0, 0))
        screen.blit(message_game_over, (SCREEN_WIDTH / 2 - message_game_over.get_width() / 2,
                                        SCREEN_HEIGHT / 2 - message_game_over.get_height() / 2))
        instructions = instructions_font.render("Press A to restart", True, (255, 0, 0))
        screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2,
                                   (SCREEN_HEIGHT / 2 - instructions.get_height() / 2) + message_game_over.get_height()))

        # Restart the Game
        if joystick.get_button(0) == True:
            health = GAME_HEALTH
            score = 0
            SPAWN_PER_INSTANCE = 1
            player.player_x = SCREEN_WIDTH/2
            player.player_y = SCREEN_HEIGHT/2
            enemies.empty()
            nukes.empty()
            dead = False

        # Flip the Display
        pygame.display.flip()

pygame.quit()
