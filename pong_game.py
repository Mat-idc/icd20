import pygame
import math
pygame.init()
 
LENGTH = 1280
WIDTH = 700
screen = pygame.display.set_mode((LENGTH, WIDTH))

pygame.display.set_caption('Pong Game')

p1y = 250
p2y = 160
ballx = LENGTH/2
bally = WIDTH/2

key = pygame.key.get_pressed() 
clock = pygame.time.Clock() 

x_vel = 8
y_vel = 8

running = True
while running:

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    pygame.draw.rect(screen,(255,0,0), pygame.Rect(250,p1y,20,90))
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(1070,p2y,20,90))

        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print('up')
        if p1y >=0:
            p1y-=9
    if keys[pygame.K_s]:
        print('down')
        if p1y <=620:
            p1y+=9
 
    pygame.draw.rect(screen,'WHITE',pygame.Rect(25,p1y,25,100))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print('up')
        if p2y >=0:
            p2y-=9
    if keys[pygame.K_DOWN]:
        print('down')
        if p2y <=620:
            p2y+=9

    
 
    pygame.draw.rect(screen,'WHITE',pygame.Rect(25,p2y,25,100))

    clock.tick(30)
     

    if ballx > (LENGTH-20):
        x_vel = -10
    if ballx < 20:
        x_vel = 10

    ballx += x_vel


    if bally > (WIDTH-20):
        print('here')
        y_vel = -20
    if bally < 20:
        y_vel = 10

    bally += y_vel
    pygame.draw.circle(screen, (225, 225, 0), (ballx, bally), 20)

    pygame.display.flip()
    