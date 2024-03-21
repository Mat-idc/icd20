import pygame
import math
pygame.init()
 
LENGTH = 1280
WIDTH = 720
screen = pygame.display.set_mode((LENGTH, WIDTH))
screen.fill('aqua')
pygame.display.set_caption("The Shape Scene Project")
 
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


#sun (4 line, and 1 circle)
    pygame.draw.circle(screen, (255,255,0), (250, 190), 60)
    pygame.draw.line(screen, (255,255,0), (250, 70), (250, 310), 10)
    pygame.draw.line(screen, (255,255,0), (130, 190), (370, 190), 10)
    pygame.draw.line(screen, (255,255,0), (160, 115), (340, 265), 13)
    pygame.draw.line(screen, (255,255,0), (160, 265), (340, 115), 13)

#moutains (2 polygons)
    pygame.draw.polygon(screen,'azure4', [(0,720),(0,400),(160,200),(310,400),(510,200),(810,400), (1010,250), (1290,400),(1290,720)])
    pygame.draw.polygon(screen,'lightcyan3', [(0,760),(0,440),(150,240),(300,440),(500,240),(800,440), (1000,290), (1280,440),(1280,760)])

#grass (1 rectangle)
    pygame.draw.rect(screen,'green', pygame.Rect(0,470,10080,670))

#pond (1 elipse)
    pygame.draw.ellipse(screen, 'blue', pygame.Rect(670,605,500,90))

#house (1 polygon, 1 circle, 2 rectangles)
    pygame.draw.rect(screen,'saddlebrown', pygame.Rect(10,580,250,170))
    pygame.draw.polygon(screen,'orangered4', [(10,580),(260,580),(140,450)])
    pygame.draw.circle(screen,'gold2', (140, 540), 35)
    pygame.draw.rect(screen,'firebrick4', pygame.Rect(110,620,60,120))

#stickman (1 arc, 1 line, 1 lines)
    pygame.draw.line(screen, 'chocolate1', (850, 670), (850, 600), 10)    
    pygame.draw.lines(screen,'chocolate1', False, [(800,630), (850,620), (900, 650)], 10)
    pygame.draw.circle(screen,'chocolate1', (850,580),22,5)

#tree (1 polygon, 1 rectangle)
    pygame.draw.rect(screen,'brown', pygame.Rect(575,600,50,600))
    pygame.draw.polygon(screen,'darkgreen', [(500,600),(700,600),(600,400)])
    
    pygame.display.flip()