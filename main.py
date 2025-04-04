import pygame
from sys import exit
import sys


#Set some parameters: 
height = 600
width = 400


pygame.init()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ScreenWindow")
clock = pygame.time.Clock()

#Commento
background = pygame.image.load('graphics/background.png')
clouds = pygame.image.load('graphics/clouds.png')
ash = pygame.image.load('graphics/ashLayer.png')

Rocket_nofire = pygame.image.load('graphics/Rocket/Rocket_NoFire.png')
Rocket_fire1 = pygame.image.load('graphics/Rocket/Rocket_Fire1.png')
Rocket_fire2 = pygame.image.load('graphics/Rocket/Rocket_Fire2.png')

Rocket_fire1_leftrot = pygame.transform.rotate(Rocket_fire1,-5)
Rocket_fire1_rightrot = pygame.transform.rotate(Rocket_fire1,5)

Rocket_fire2_leftrot = pygame.transform.rotate(Rocket_fire2,-5)
Rocket_fire2_rightrot = pygame.transform.rotate(Rocket_fire2,5)

Bird1 = pygame.image.load('graphics/Bird1.png')
Bird2 = pygame.image.load('graphics/Bird2.png')
bird_coords = []




#Load the sprite and create a surfaceloop

#Want an initial launch sequence for the game
#This will be a simple game 

#OK, so we'll want a starter screen, which can just be the background with The title, and a start button! 


overallcount=0
startsequence_count=0
flightsequence_count=0


background_height = 0
rocket_height = 0
background_height = 0

TitleScreenLoop = True
flightsequence = False


text_font = pygame.font.SysFont('Courier',20)


def drawText(text, font, colour):
    text_img = font.render(text, font, colour)
    screen.blit(text_img, (125,200))


startsequence = False





while(True):
    
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #             exit

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                TitleScreenLoop = False
                startsequence = True
            if event.key == pygame.K_ESCAPE:
                    exit()

    screen.fill('blue')
    
    
    
    
    
    if TitleScreenLoop:
       
        screen.blit(background, (0,-1400))
        if overallcount%2 == 0:
            screen.blit(Bird1, (4*overallcount%400, 100))
        if overallcount%2 == 1:
            screen.blit(Bird2, (4*overallcount%400, 100))
        overallcount+=1
        if 2*overallcount%1200- 800>0:
            screen.blit(clouds,(2*overallcount%1200- 800 -1200  ,0))
        screen.blit(clouds, (2*overallcount%1200-800,0) )
        screen.blit(Rocket_nofire, (160,380))
        drawText('PRESS SPACE!', text_font, 'Black')

    
    if startsequence:
        startsequence_count +=1
        screen.blit(background, (0,-1400))
        if overallcount%2 == 0:
            screen.blit(Bird1, (4*overallcount%400, 100))
        if overallcount%2 == 1:
            screen.blit(Bird2, (4*overallcount%400, 100))
        overallcount+=1
        if 2*overallcount%1200- 800>0:
            screen.blit(clouds,(2*overallcount%1200- 800 -1200  ,0))
            screen.blit(clouds, (2*overallcount%1200-800,0) )
        screen.blit(clouds, (2*overallcount%1200-800,0) )
        ashop = ash.copy()
        alpha = min(10 * (startsequence_count), 255) 
        ashop.fill((255, 255, 255 , alpha), None, pygame.BLEND_RGBA_MULT)
        screen.blit(ashop, (0,0))
        if  startsequence_count < 40:
            if (startsequence_count%4) ==0:
                screen.blit(Rocket_fire1_leftrot, (160,380))
            if (startsequence_count%4) ==1:
                screen.blit(Rocket_fire2_rightrot, (160,380))
            if( startsequence_count%4) ==2:
                screen.blit(Rocket_fire2_leftrot, (160,380))
            if (startsequence_count%4) ==3:
                screen.blit(Rocket_fire1_rightrot, (160,380))
        #Now we want to move the rocket up - call this phase 1 - where the rocket moves up in the air air
        if startsequence_count > 40 and startsequence_count < 80:
            if (startsequence_count%2) ==0:
                screen.blit(Rocket_fire1, (160,380-rocket_height))
            if (startsequence_count%2) ==1:
                screen.blit(Rocket_fire2, (160,380-rocket_height))
            rocket_height +=4
        if startsequence_count > 80:
            startsequence = False
            flightsequence = True
        #
    if flightsequence:
        if flightsequence_count < 100:
            background_height += 10
            
            screen.blit(background, (0,-1400 +background_height))
            screen.blit(ash, (0,background_height))
            if overallcount%2 == 0:
                screen.blit(Bird1, (4*overallcount%400,background_height))
            if overallcount%2 == 1:
                screen.blit(Bird2, (4*overallcount%400, background_height))
            overallcount+=1
            if 2*overallcount%1200- 800>0:
                screen.blit(clouds,(2*overallcount%1200- 800 -1200 , background_height))
                screen.blit(clouds, (2*overallcount%1200-800, background_height))
            screen.blit(clouds, (2*overallcount%1200-800,background_height))
            if rocket_height >2:
                screen.blit(Rocket_fire1, (160,380-rocket_height))
                rocket_height -=2





        
            

    

    pygame.display.update()
    clock.tick(12)  







