# Starts the pygame
# Starts random

import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chase Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game loop
clock = pygame.time.Clock()
running = True

# Define the player and enemy positions and sizes
player_size = 50
player_x = (SCREEN_WIDTH - player_size) // 2
player_y = SCREEN_HEIGHT - player_size - 10
enemy_size = 50
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 5

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Move the enemy
    enemy_y += enemy_speed

    # If the enemy reaches the bottom of the screen, reset its position
    if enemy_y > SCREEN_HEIGHT:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
        enemy_y = 0

    # Draw the enemy
    pygame.draw.rect(screen, GREEN, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Check for collision between player and enemy
    if (player_x < enemy_x + enemy_size and
            player_x + player_size > enemy_x and
            player_y < enemy_y + enemy_size and
            player_y + player_size > enemy_y):
        print("Game Over")
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()