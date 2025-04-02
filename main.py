import pygame
from sys import exit



#Set some parameters: 
height = 600
width = 400


pygame.init()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ScreenWindow")
clock = pygame.time.Clock()


background = pygame.Surface((10, 20))
surface.fill('red')
sprite = pygame.image.load('graphics/sprite.png')
#Load the sprite and create a surface



surface_coords = [100,100]

#Now we start our game loop

#Want an initial launch sequence for the game
#This will be a simple game 

while(initial_countdown < 200):
    


    initial_countdown += 1








while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_UP:
                surface_coords[1] -= 10



    screen.fill('blue')
    # blit the surface to the screen at (100, 100)
    screen.blit(surface, surface_coords)
    screen.blit(sprite, (0,0))
    pygame.display.update()
    clock.tick(60)  








