import pygame
import math
pygame.init()
 
LENGTH = 1280
WIDTH = 720
screen = pygame.display.set_mode((LENGTH, WIDTH))
screen.fill('aqua')
pygame.display.set_caption("The Scene")
 
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

#house:
    pygame.draw.rect(screen,'coral4', pygame.Rect(10,600,180,300))
    pygame.draw.polygon(screen,'brown', [(10,600),(190,600),(95,450)])
    pygame.draw.circle(screen,'darkgoldenrod2', (100, 560), 35)
    pygame.draw.rect(screen,'brown1', pygame.Rect(80,625,50,100))

#2 trees:
    pygame.draw.polygon(screen,'green', [(200,600),(400,600),(300,400)])
    pygame.draw.rect(screen,'brown', pygame.Rect(280,600,50,600))

    pygame.draw.polygon(screen,'green', [(500,600),(700,600),(600,400)])
    pygame.draw.rect(screen,'brown', pygame.Rect(580,600,50,600))

#car
    pygame.draw.rect(screen,'red',pygame.Rect(950,650,250,50))
    pygame.draw.rect(screen,'red',pygame.Rect(1025,600,100,50))
    pygame.draw.circle(screen,'black', (1020,700), 20)
    pygame.draw.circle(screen,'black', (1150,700), 20)

#sun
    
    pygame.draw.circle(screen, (255,255,0), (250, 190), 55)
    pygame.draw.line(screen, (255,255,0), (250, 70), (250, 310), 20)
    pygame.draw.line(screen, (255,255,0), (130, 190), (370, 190), 20)
    pygame.draw.line(screen, (255,255,0), (160, 115), (340, 265), 23)
    pygame.draw.line(screen, (255,255,0), (160, 265), (340, 115), 23)
    #pygame.draw.polygon(screen,'brown', [(10,600),(190,600),(95,450)])
    #pygame.draw.polygon(screen,'brown', [(10,600),(190,600),(95,450)])

#stickman
    pygame.draw.line(screen, 'black', (850, 670), (850, 600), 10)
    pygame.draw.lines(screen,'black', False, [(800,720), (850,670), (900, 720)], 10)
    pygame.draw.lines(screen,'black', False, [(800,650), (850,620), (900, 650)], 10)
    pygame.draw.circle(screen,'black', (850,580),22,5)


#flag with 2 colors
    pygame.draw.line(screen, 'black', (750, 720), (750, 300), 10)
    pygame.draw.rect(screen,'red', pygame.Rect(756,300,150,100))
    pygame.draw.rect(screen,'gold1', pygame.Rect(820,325,20,50))
    pygame.draw.rect(screen,'gold1', pygame.Rect(800,340,60,20))

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