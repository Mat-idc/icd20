import pygame
import math
pygame.init()
 
LENGTH = 500
WIDTH = 500
screen = pygame.display.set_mode((LENGTH, WIDTH))
screen.fill((255,255,255))
pygame.display.set_caption("The McDonald's Rocket")
 
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
   
    
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(180,160,180,270))
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(110,190,70,270))
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(360,190,70,270))
    pygame.draw.polygon(screen, (255, 225, 0), [(180, 160), (360, 160), (270, 20)])
    pygame.draw.circle(screen, (225, 225, 0), (270, 360), 40)
    pygame.draw.circle(screen, (225, 225, 0), (270, 250), 40) 
    pygame.display.update()



 #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, 0, box_width, 50)) # this is the red square
                                     # horizontal, vertical, radius size
    pygame.draw.circle(screen, (0, 255, 0), (1000, 300), 100) #this is the circle

    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 20) #this is the line, star point, end position, thickness

    #pygame.draw.polygon(screen, (255, 255, 0), [(200, 200), (300, 300), (400, 200)]) #this is a triangle

    #pygame.draw.arc(screen, (255, 0, 255), pygame.Rect(100, 100, 200, 200), 0, math.pi/2, 2) # these are angles. a whole circle is 2 pi, half a circle 1 pi, 90 degrees is pi/2.

    #pygame.draw.arc(screen,(255,0,0),pygame.Rect(10,10,200,200), 0.5*math.pi, math.pi,10)
    
    # pygame.draw.ellipse(screen, (0, 0, 255), pygame.Rect(200, 200, 200, 100))
    # pygame.draw.aaline(screen, (255, 0, 255), (0, 0), (800, 600))
    # pygame.draw.lines(screen, (100, 255, 0), False, [(100, 100), (200, 200), (300, 100)], 2)
   