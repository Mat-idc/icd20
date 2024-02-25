import pygame
import math
pygame.init()
 
LENGTH = 500
WIDTH = 500
screen = pygame.display.set_mode((LENGTH, WIDTH))
screen.fill((255,255,255))
pygame.display.set_caption("The sun")
 
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
   
    
    pygame.draw.circle(screen, (255,255,0), (250, 190), 55)
    pygame.draw.line(screen, (255,255,0), (250, 70), (250, 310), 20)
    pygame.draw.line(screen, (255,255,0), (130, 190), (370, 190), 20)
    pygame.draw.line(screen, (255,255,0), (160, 115), (340, 265), 23)
    pygame.draw.line(screen, (255,255,0), (160, 265), (340, 115), 23)
    #pygame.draw.line(screen, (255,255,0), (256, 60), (256, 150), 20)  # 1st num in pair one, 2nd num in pair one (horizontall position, up & down), #1st num in pair two 2nd num in pair two (horizontall position, up and down)
    #pygame.draw.line(screen, (255,255,0), (320, 110), (150, 160), 20)
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
   