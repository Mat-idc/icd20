import pygame
import math
pygame.init()
 
LENGTH = 500
WIDTH = 500
screen = pygame.display.set_mode((LENGTH, WIDTH))
screen.fill((0,255,220))
pygame.display.set_caption("Snowman")
 
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
   
    
    pygame.draw.circle(screen, (255, 255, 255), (250, 400), 100)
    pygame.draw.circle(screen, (255, 255, 255), (250, 250), 70)
    pygame.draw.circle(screen, (255, 255, 255), (250, 150), 50)
    pygame.draw.circle(screen, (0, 0, 0), (250, 359), 10)
    pygame.draw.circle(screen, (0, 0, 0), (250, 397), 10)
    pygame.draw.circle(screen, (0, 0, 0), (250, 240), 10)
    pygame.draw.circle(screen, (0, 0, 0), (250, 270), 10)
    pygame.draw.circle(screen, (0, 0, 0), (230, 130), 5)
    pygame.draw.circle(screen, (0, 0, 0), (270, 130), 5)
    pygame.draw.arc(screen, (0, 0, 0), pygame.Rect(225, 130, 50, 50), math.pi, 2 * math.pi, 3)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 80, 100, 30)) #I used rectangles for the hat
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(230, 30, 43, 60))
    pygame.display.update()



 #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, 0, box_width, 50)) # this is the red square
                                     # horizontal, vertical, radius size
    #pygame.draw.circle(screen, (0, 255, 0), (1000, 300), 100) #this is the circle

    #pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 20) #this is the line, star point, end position, thickness

    #pygame.draw.polygon(screen, (255, 255, 0), [(200, 200), (300, 300), (400, 200)]) #this is a triangle

    #pygame.draw.arc(screen, (255, 0, 255), pygame.Rect(100, 100, 200, 200), 0, math.pi/2, 2) # these are angles. a whole circle is 2 pi, half a circle 1 pi, 90 degrees is pi/2.

    #pygame.draw.arc(screen,(255,0,0),pygame.Rect(10,10,200,200), 0.5*math.pi, math.pi,10)
    
    # pygame.draw.ellipse(screen, (0, 0, 255), pygame.Rect(200, 200, 200, 100))
    # pygame.draw.aaline(screen, (255, 0, 255), (0, 0), (800, 600))
    # pygame.draw.lines(screen, (100, 255, 0), False, [(100, 100), (200, 200), (300, 100)], 2)
   