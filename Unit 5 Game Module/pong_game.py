import pygame
import math
import time
pygame.init()
 
LENGTH = 1280
WIDTH = 700
screen = pygame.display.set_mode((LENGTH, WIDTH))

pygame.display.set_caption('Pong Game')

p1y = 250
p2y = 160
ballx = LENGTH/2
bally = WIDTH/2
p1score = 0
p2score = 0
beep = pygame.mixer.Sound('Unit 5 Game Module/sound effects/beep.wav')
swoosh = pygame.mixer.Sound('Unit 5 Game Module/sound effects/ES_Whip Whoosh Swoosh 3 - SFX Producer.mp3') 
pygame.mixer.music.load('Unit 5 Game Module\sound effects\ES_Albatross - Lexica.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

key = pygame.key.get_pressed() 
clock = pygame.time.Clock() 

x_vel = 15
y_vel = 8

running = True
while running:
    screen.fill('BLACK')

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

          
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if p1y >=0:
            p1y-=15
    if keys[pygame.K_s]:
        if p1y <=620:
            p1y+=15
 
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(250,p1y,20,90))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if p2y >=0:
            p2y-=15
    if keys[pygame.K_DOWN]:
        if p2y <=620:
            p2y+=15
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(1070,p2y,20,90))

    clock.tick(30)
     

    if ballx > (LENGTH-20):
        ballx = LENGTH//2
        bally = WIDTH//2
        p1score+=1
        pygame.mixer.Sound.play(beep)
        
    if ballx < 20:
        ballx = LENGTH//2
        bally = WIDTH//2
        p2score+=1
        pygame.mixer.Sound.play(beep)

    font = pygame.font.SysFont(None, 36)

    text_one = font.render(f"P1 Score: {int(p1score)}" , True, 'white')
    screen.blit(text_one, (100,30))

    text_one = font.render(f"P2 Score: {int(p2score)}" , True, 'white')
    screen.blit(text_one, (1050,30))

    if bally > (WIDTH-20):
            y_vel = -10
    if bally < 20:
            y_vel = 10

    bally += y_vel

    p1_rect = pygame.Rect(250,p1y,20,90)
    p2_rect = pygame.Rect(1070,p2y,20,90)
    ball_rect = pygame.Rect(ballx-20,bally-20,40,40)
        
    if p1_rect.colliderect(ball_rect):
        x_vel=abs(x_vel)
        pygame.mixer.Sound.play(swoosh)

    if p2_rect.colliderect(ball_rect):
        x_vel=abs(x_vel)*-1
        pygame.mixer.Sound.play(swoosh)

    ballx += x_vel
    pygame.draw.circle(screen, ('cyan'), (ballx, bally), 20)

    if p1score == 10:
        screen.blit((font.render(f"Player 1 Won!", True, 'white')),(580,300))
        pygame.display.update()
        time.sleep(10)
        running = False
    
    if p2score == 10:
        screen.blit((font.render(f"Player 2 Won!", True, 'white')),(550,300))
        pygame.display.update()
        time.sleep(10)
        running = False
    
    pygame.display.flip()


