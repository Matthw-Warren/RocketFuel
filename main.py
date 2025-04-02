import pygame
from sys import exit



#Set some parameters: 
height = 600
width = 400


pygame.init()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ScreenWindow")
clock = pygame.time.Clock()


background = pygame.image.load('graphics/background.png')
clouds = pygame.image.load('graphics/clouds.png')


Rocket_nofire = pygame.image.load('graphics/Rocket/Rocket_NoFire.png')
Rocket_fire1 = pygame.image.load('graphics/Rocket/Rocket_Fire1.png')
Rocket_fire2 = pygame.image.load('graphics/Rocket/Rocket_Fire2.png')



Bird1 = pygame.image.load('graphics/Bird1.png')
Bird2 = pygame.image.load('graphics/Bird2.png')
bird_coords = []




#Load the sprite and create a surfaceloop

#Want an initial launch sequence for the game
#This will be a simple game 

#OK, so we'll want a starter screen, which can just be the background with The title, and a start button! 


i=0
while(True):
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            


    screen.fill('blue')
    # blit the surface to the screen at (100, 100)
    screen.blit(background, (0,-1400))
    if i%2 == 0:
        screen.blit(Bird1, (4*i%400, 100))
    if i%2 == 1:
        screen.blit(Bird2, (4*i%400, 100))
    i+=1
    if 10*i%1200- 800>0:
        screen.blit(clouds,(10*i%1200- 800 -1200  ,0))
    screen.blit(clouds, (10*i%1200-800,0) )
    screen.blit(Rocket_nofire, (160,400))
    pygame.display.update()
    clock.tick(12)  








