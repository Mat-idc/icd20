import random
import sys
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 700
BACKGROUND_SCROLL_SPEED = 1  # Speed of background scrolling

# Background position
background_x = 0



# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("Unit 5 Game Module\Python Game Assignment Graphics + SFX/Untitled design (35).png")
background_rect = background_image.get_rect()


# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill screen with white

    # Scroll the background
    background_x -= BACKGROUND_SCROLL_SPEED
    if background_x < -background_rect.width:
        background_x = 0

    # Draw the background
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_rect.width, 0))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 60 FPS

pygame.quit()
sys.exit()
