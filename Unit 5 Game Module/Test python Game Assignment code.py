#code

#This imports game modules for pygame, math, time and random
import pygame 
import math
import time
import random
pygame.init() 
#This is where I define the screen length and width and set the caption for the screen window
LENGTH = 1280
WIDTH = 700
BACKGROUND_SCROLL_SPEED = 3  # Speed of background scrolling

# Background position
background_x = 0

# Set up the display
screen = pygame.display.set_mode((LENGTH, WIDTH))
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("Unit 5 Game Module\Python Game Assignment Graphics + SFX\clouds.png")
background_rect = background_image.get_rect()
screen = pygame.display.set_mode((LENGTH, WIDTH)) #Uppercase lettered variables mean it's a constant variable/it never changes
pygame.display.set_caption('Fruit Collectors')
#This is where I set the timer for the fruit spawn, make an empty list for fruits and define the two players scores
fruit_time = 60
fruit_timer = fruit_time
fruits = []
score = 0
score2= 0
#This is where I import the images for my icons in the game, I also scale them to make sure they're the right size
pygame.draw.rect(screen,'green', pygame.Rect(0,650,1300,270))
apple_image = pygame.image.load('Unit 5 Game Module\Python Game Assignment Graphics + SFX\IMG-1867-768x768-removebg-preview.png')
apple_image = pygame.transform.scale(apple_image,(70,70)) #this makes the fruit the right size
banana_image = pygame.image.load('Unit 5 Game Module\Python Game Assignment Graphics + SFX\drawing-banana-step-6-removebg-preview.png')
banana_image = pygame.transform.scale(banana_image,(70,70)) 
basket_image = pygame.image.load('Unit 5 Game Module\Python Game Assignment Graphics + SFX/basket.png')
basket_image = pygame.transform.scale(basket_image,(90,90))
basket2_image = pygame.image.load('Unit 5 Game Module\Python Game Assignment Graphics + SFX\imgbin-easter-basket-picnic-basket-empty-s-W3stek8AiLm2uAKm8fT2xe5Rb__1_-removebg-preview.png')
basket2_image = pygame.transform.scale(basket2_image,(110,90)) 
broccoli_image = pygame.image.load('Unit 5 Game Module\Python Game Assignment Graphics + SFX\drawing-vegetable.png')
broccoli_image = pygame.transform.scale(broccoli_image,(70,90)) 
#This defines the x coordinates where both baskets will start
basketx1 = 700 
basketx2 = 300
#These are the variables for the baskets y coordinates and for the baskets hitboxes y coordinates
baskety1 = 610
baskety2 = 610
hitbaskety1 = 609
hitbaskety2 = 609
#This is where I define the fonts I use in my game
font = pygame.font.SysFont(None, 36) 
font2 = pygame.font.SysFont(None, 70) 
#This is where I import sound effects and background music, I also set the volume for the background music
score_sfx = pygame.mixer.Sound('Unit 5 Game Module\Python Game Assignment Graphics + SFX\ES_Multimedia Beep 6 - SFX Producer.mp3')
basket_collect_sfx = pygame.mixer.Sound('Unit 5 Game Module\Python Game Assignment Graphics + SFX\ES_Fruit Vegetable Impacts - SFX Producer.mp3') 
pygame.mixer.music.load('Unit 5 Game Module\Python Game Assignment Graphics + SFX\ES_Helios - Lexica (1).mp3')
pygame.mixer.music.set_volume(0.5)
#This loops the song so it restarts it from the beginning when it ends
pygame.mixer.music.play(-1)
#This is the countdown timer for the game
time_remaining = 65  #This is the initial start time in seconds
clock = pygame.time.Clock() 
#This defines jumping for baskets 1 and 2 as boolean variables and it defines how high the baskets can jump
jumping = False
jump_count = 10
jump_count2 = 10
jumping2 = False

#This starts the main game loop
running = True
while running:
    #This makes the aqua background and green rectange, for the sky and grass
    screen.fill('aqua')
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

    #This allows you to exit the program
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen,'green', pygame.Rect(0,650,1300,270))


#This is for the end of game screen, it will check if the time is less than 0 and will blit the end game message with players scores to the screen
    time_remaining -= clock.get_time() / 1000 
    if time_remaining <= 0:
       end_screen = font2.render(f"Game Over! Final Score P1: {int(score)} and P2: {int(score2)}", True, 'black') 
       end_screen2 = font2.render(f"Team Score: {(score)+(score2)}", True, 'black')
       screen.blit(end_screen, (150, 300))
       screen.blit(end_screen2, (460, 400))

    
#This is for the start screen, it will blit what each fruit and vegetable is worth and it will show this until the timer gets to 60 seconds
    elif time_remaining >= 60:
        start_screen = font2.render(f"Points: Banna = 3, Apple = 2, Broccoli = -1", True, 'black')
        screen.blit(start_screen, (150, 300)) 

        
    

#This increases the spawn rate of fruits as the timer goes down 
    else:
        if time_remaining <= 20:
            fruit_time = 15
        elif time_remaining <=30:
            fruit_time = 25
        elif time_remaining <=50:
            fruit_time = 30
        elif time_remaining <=55:
            fruit_time = 35
#This part picks a random number for the x coordinate of the screen, spawns the fruits at a y coordinate of -20 and selects a random fruit or vegetable image and appends this all to a list called fruits
        fruit_timer -= 1
        if fruit_timer<=0:
            fruits.append([random.randint(10,1190),-20,random.choice([banana_image, apple_image, broccoli_image, banana_image, apple_image])]) #The -20 is so fruits start falling above the zero line/off screen
            fruit_timer = fruit_time
#This is the list for the hitboxes around the fruits
        fruit_border = []

        for y in fruits:
            #This adds a rect/border around each fruit
            fruit_border.append(pygame.Rect(y[0], y[1], 70, 70))
            #This makes each fruit's y value go up which makes it look like there falling
            y[1]+=10
            #This blits the fruits to the screen
            screen.blit(y[2],(y[0], y[1])) #This refers back to the list above, the y[0] affects the horizontal spawnpoint of the fruits, y[1] affects the vertical spawnpoint and y[2] displays the random fruit image
    

        #This defines the invisible border around the baskets that makes it possible to collect fruits
        basket_rect = pygame.Rect(basketx1, hitbaskety1, 90,90)
        basket_rect2 = pygame.Rect(basketx2, hitbaskety2, 100,100)

        
     
        #This defines what happens when the basket hits the fruit and it adds sfx for each contact, this is for player 1
        for rect in fruit_border:
            if rect.colliderect(basket_rect):
                index = fruit_border.index(rect)
                fruit_border.remove(rect)
                #This is a feature I implemented into my game. Orginally all fruits were worth one point but to make the fruits different values I made each one of them worth different points.    
                #This makes different fruits worth different points
                if fruits[index][2] == apple_image:
                    score += 2  
                elif fruits[index][2] == banana_image:
                    score += 3
                #Here is another feature I added which was implementing a new food item that reduced points. So I added broccoli, since the game is called fruit collectors, and I made it so that your score would minus 1 when you hit the broccolis.
                elif fruits[index][2] == broccoli_image:
                    score -=1
                #This removes what is at the index position
                fruits.pop(index)
                #This makes sfx for the basket 1 collect sound and score increase sound  
                pygame.mixer.Sound.play(basket_collect_sfx)             
                pygame.mixer.Sound.play(score_sfx) 

#This defines what happens when the basket hits the fruit and it adds sfx for each contact this is for player 2 
            elif rect.colliderect(basket_rect2):
                index = fruit_border.index(rect)
                fruit_border.remove(rect)
                #This makes different fruits worth different points 
                if fruits[index][2] == apple_image:
                        score2 += 2  
                elif fruits[index][2] == banana_image:
                        score2 += 3
                elif fruits[index][2] == broccoli_image:
                        score2 -=1
                fruits.pop(index)
                #This makes the sound effect for when fruits collect in basket 2 and the sfx for the score increase
                pygame.mixer.Sound.play(basket_collect_sfx)
                pygame.mixer.Sound.play(score_sfx)                     
        #This blits the score to the screen for player 2            
        text_score2 = font.render(f"P2 Score: {(score2)}", True, 'black')
        screen.blit(text_score2, (300,30))
        #This blits the score to screen for player 1  
        text_score = font.render(f"P1 Score: {(score)}", True, 'black')
        screen.blit(text_score, (70,30))
        
        
        #This blits both baskets images to the screen
        screen.blit(basket_image, (basketx1, baskety1))
        screen.blit(basket2_image, (basketx2, baskety2))
              
        #This makes it so keys can be pressed
        Keys = pygame.key.get_pressed() 
        #These are the left and right controls for basket 1
        if Keys[pygame.K_LEFT] and basketx1 >= 0:
            basketx1 -= 15   #-=15 is so it goes in the left direction  
        if Keys[pygame.K_RIGHT] and basketx1 <= 1190:
            basketx1 +=15    #+=15 is so it goes in the right direction  
        #This jumping section was a new feature I implemented to my game. I added it to make the game more fair because originally when the baskets overlapped all points would go to player 1. This is because player 1's basket was being checked first in the collision part of my code.
        #To make my game more fair I added this jumping feature that added another dynamic to the game and reduced the chances of both baskets overlapping each other.
        #When the up arrow key gets pressed and you're not already jumping than it will change jumping to equal True, this is for basket1
        if Keys[pygame.K_UP] and not jumping:
            jumping = True
      
        #This determines the direction of the jump 
        if jumping:
            if jump_count >= -10: 
                direction = 1 #Direction positive 1 = up
                if jump_count < 0:
                    direction = -1 #Direction negative 1 = down
                #This creates the arch for the jumps
                baskety1 -= (jump_count**2) * 0.1 * direction 
                hitbaskety1 -= (jump_count**2) * 0.1 * direction 
                jump_count -= 1
        #This resets the jump_count variable
            else:
                jumping = False
                jump_count = 10
        #This game used to be a single player game so I implemented a new change by adding another basket with the same functions as the first basket to make it a multiplayer game. 
        #This allows two players to either work together and get a high Team Score or go against each other to see who can get the highest score.
        #These are the left and right controls for basket 2
        if Keys[pygame.K_a] and basketx2 >= 0:
            basketx2 -= 15  #-=15 is so it goes in the left direction 
        if Keys[pygame.K_d] and basketx2 <= 1190:
            basketx2 +=15   #+=15 is so it goes in the right direction 
        #When the w key gets pressed and you're not already jumping than jumping2 equals True, this is for basket 2
        if Keys[pygame.K_w] and not jumping2:
            jumping2 = True
        #This determines the direction of jumps
        if jumping2:
            if jump_count2 >= -10:
                direction = 1 #Direction positive 1 = up
                if jump_count2 < 0:
                    direction = -1 #Direction negative 1 = down
                #This determines the amount of arch and the up or down direction
                baskety2 -= (jump_count2 ** 2) * 0.1 * direction 
                hitbaskety2-= (jump_count2 ** 2) * 0.1 * direction
                jump_count2 -= 1
            #This resets the jump_count2 variable  
            else:
                jumping2 = False
                jump_count2 = 10
    
        
        #This blits the amount of time remaining which is the clock on the top right of the screen
        text_time_remaining = font.render(f"Time: {int(time_remaining)}", True, 'black')
        screen.blit(text_time_remaining, (1100,30))
        #This prints the time on the clock
        #print(clock.get_time())

    

     

    

    #This sets the pygame tick speed to 30
    clock.tick(30)
    #This updates the display of the screen
    pygame.display.flip()
