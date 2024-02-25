import sys
# sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # this sets width and height of screen # alt f4 to close windows that are to big

pygame.display.set_caption("SUPER POTATO BRUH") # this sets the name on top window/screen

running = True  #this is a loop for when the pygame is open and running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # this is the code for hitting the red x on the pygame window
            running = False

    # fill screen with white
    screen.fill((255, 255, 255)) #this is RGB (determines how much red, green, and blue is needed) white = 225, 225, 225, black = 0,0,0, Greay = 128, 128, 128

    #redraw screen
    pygame.display.flip()

pygame.quit()