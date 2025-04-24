import pygame
from sys import exit
import sys
from numpy import random


#Set some parameters: 
screen_height = 600
screen_width = 400


#Building rocket class
Rocket_nofire = pygame.image.load('graphics/Rocket/Rocket_NoFire.png')
Rocket_fire1 = pygame.image.load('graphics/Rocket/Rocket_Fire1.png')
Rocket_fire2 = pygame.image.load('graphics/Rocket/Rocket_Fire2.png')
rocket_dict  = {0: Rocket_nofire, 1: Rocket_fire1, 2: Rocket_fire2}

ash = pygame.image.load('graphics/ashLayer.png')


#Could combine some of these into one class, for example moving objects up and down. For now will leave. 



class Rocket(pygame.sprite.Sprite):
    def __init__(self, relx,rely ,screen):
        self.relx = relx
        self.rely = rely
        self.screen = screen
        self.mode = 0
        self.tilt = 'centre'

    def moveleft(self, speed):
        self.relx -= speed

    def moveright(self, speed):
        self.relx += speed

    def moveup(self, speed):
        self.rely -= speed

    def blit(self):
        #Mode is 0, 1, or 2 the different 'fires'
        #direction is one of left, right or centre.
        convert = {'left' : +10, 'right' : -10, 'centre' : 0}
        toscreen = pygame.transform.rotate(rocket_dict[self.mode], convert[self.tilt])
        self.screen.blit(toscreen, (self.relx, self.rely))
    
    def set_direciton(self, direciton):
        self.tilt = direciton


    def change_mode(self):
        if self.mode == 1:
            self.mode = 2
        elif self.mode == 2 or self.mode == 0:
            self.mode = 1
    
    def liftofftilt(self):
        if self.tilt == 'centre' or self.tilt == 'right':
            self.tilt = 'left'
        elif self.tilt == 'left':
            self.tilt = 'right'

#Then birds
Bird1 = pygame.image.load('graphics/Bird1.png')
Bird2 = pygame.image.load('graphics/Bird2.png')
bird_dict = {1: Bird1, 2: Bird2}

class Bird:
    def __init__(self, relx,rely, screen):
        self.relx = relx
        self.rely = rely
        self.screen = screen
        self.mode = 1

    def moveright(self, speed):
        self.relx += speed
        self.relx = self.relx % screen_width

    def movedown(self,speed):
        self.rely += speed

    def blit(self, mode):
        self.screen.blit(bird_dict[mode], (self.relx, self.rely))

    def change(self):
        if self.mode == 1:
            self.mode = 2
        else:
            self.mode = 1

#Clouds
clouds = pygame.image.load('graphics/clouds.png')
class Cloud:
    def __init__(self, relx,rely, screen):
        self.relx = relx
        self.rely = rely
        self.screen = screen

    def moveright(self, speed):
        self.relx += speed

    def movedown(self,speed):
        self.rely += speed

    def blit(self):
        if self.relx%1200- 800>0:
            self.screen.blit(clouds,(self.relx%1200- 800 -1200  ,self.rely))
        self.screen.blit(clouds, (self.relx%1200-800,self.rely) )


class Background:
    def __init__(self, screen, rely):
        self.screen = screen
        self.background = pygame.image.load('graphics/background.png')
        self.main_background = pygame.image.load('graphics/MainBackground.png')
        self.ash = pygame.image.load('graphics/ashLayer.png')
        self.rely = rely
        self.ashalpha =0 
        self.mode = 'notmain'
        self.ashon = True

    def blit(self):
        if self.mode == 'main':
            self.screen.blit(self.main_background, (0, self.rely))
        else:
            self.screen.blit(self.background, (0, -1400 + self.rely))
        if self.ashon:    
            ashop = ash.copy()
            ashop.fill((255, 255, 255 , self.ashalpha), None, pygame.BLEND_RGBA_MULT)
            self.screen.blit(ashop, (25,self.rely))

    def ashupdate(self, rate=1):
        self.ashalpha += rate


    def movedown(self, speed):
        self.rely += speed   






star1 = pygame.image.load('graphics/star1.png')
star2 = pygame.image.load('graphics/star2.png')
star3 = pygame.image.load('graphics/star3.png')
star_dict = {1: star1, 2: star2, 3: star3}
#Not yet implemente stars so will for now leave this 

# We'd like to get background stars generated randomly - their lifetime will be while they're on the screen. 
# IN retrospect - stars dont really do this! - they're too far in the background


class back_star:
    def __init__(self, screen):
        self.distance = random.randint(1,5)
        self.relx = random.randint(400)
        self.rely =0
        self.star_type = random.randint(1,4)
        self.screen = screen
        self.star = star_dict[self.star_type]
        #Should change the size based on the distance.

    def movedown(self):
        self.rely += 1/self.distance

    def blit(self):
        self.screen.blit(self.star, (self.relx, self.rely))

    def kill(self):
        del self

class back_star_list:
    def __init__(self,screen):
        self.count = 0
        self.list = []
        self.screen = screen

    def add_star(self):
        new = back_star(self.screen)
        self.list.append(new)
        self.count +=1

    def update_stars(self):
        newlist = []
        for k in self.list:
            k.movedown()
            if k.rely<400:
                newlist.append(k)
            else:
                k.kill()
        self.list = newlist

    def blit_stars(self):
        for k in self.list:
            k.blit()



#Need to draw my asteroids.
# asteroid1 = pygame.image.load('graphics/')
# asteroid2 = pygame.image.load('graphics/')
# asteroid3 = pygame.image.load('graphics/')
# asteroid_dict = {1: asteroid1, 2: asteroid2, 3: asteroid3}


class asteroid:
    def __init__(self, screen):
        self.speed = random.randint(1,10)
        self.size = random.randint(1,3)
        self.relx = random.randint(400)
        self.rely =0
        self.asteroid_type = random.randint(1,4)
        self.screen = screen
        self.asteroid = star_dict[self.asteroid_type]


    def movedown(self):
        self.rely += speed

    def blit(self):
        self.screen.blit(self.star, (self.relx, self.rely))

    def kill(self):
        del self

#Next plan is to introduce a scoreboard (for getting stars), introduce asteroids (which can kill you), and lives. 

class asteroid_list:
    def __init__(self,screen):
        self.count = 0
        self.list = []
        self.screen = screen

    def add_asteroid(self):
        new = asteroid(self.screen)
        self.list.append(new)
        self.count +=1

    def update_asteroids(self):
        newlist = []
        for k in self.list:
            k.movedown()
            if k.rely<400:
                newlist.append(k)
            else:
                k.kill()
        self.list = newlist

    def blit_asteroids(self):
        for k in self.list:
            k.blit()


#Will package these types of objects into a bigger 'obj list' class - as this I've just copy pasted the back star code!



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Rocket Fuel")
        self.running = True
        self.clock = pygame.time.Clock()
        self.game_state = "menu"
        #We'll also initialise our objects - so the clouds, the rocket, the birds, the stars etc.
        self.rocket  = Rocket(165, 380, self.screen)
        self.bird = Bird(0, 100, self.screen)
        self.cloud = Cloud(0, 0, self.screen)
        self.background = Background(self.screen, 0)
        self.liftofftimer =0
        self.backstars = back_star_list(self.screen)
        self.maincount = 0


    def event_handling(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if self.game_state == "menu" and event.key == pygame.K_SPACE:
                            self.game_state = "liftoff"
                elif self.game_state == "maingame":
                    self.rocket.set_direciton('centre')                    



    def menu_draw(self):
        #This is our starting screen
        self.background.blit()
        self.bird.blit(self.bird.mode)
        self.cloud.blit()
        self.rocket.blit()
        text_font = pygame.font.SysFont('Courier',20)
        text_img = text_font.render('PRESS SPACE!', text_font, 'Black')
        self.screen.blit(text_img, (125,200))
        
    def menu_update(self):
        self.bird.change()
        self.bird.moveright(2)
        self.cloud.moveright(1)
        
    def liftoff_draw(self):
        self.background.blit()
        self.bird.blit(self.bird.mode)
        self.cloud.blit()
        self.rocket.blit()

    def liftoff_update(self):
        self.bird.change()
        self.bird.moveright(2)
        self.cloud.moveright(1)
        self.rocket.change_mode()
        self.liftofftimer += 1
        if self.liftofftimer <= 60:
            self.rocket.liftofftilt()
            self.background.ashupdate(255/60)
        if self.liftofftimer > 60:
            self.rocket.moveup(4)
            self.rocket.set_direciton('centre')
        if self.liftofftimer > 100:
            self.game_state = "flight"

        
    def flight_draw(self):
        self.background.blit()
        self.bird.blit(self.bird.mode)
        self.cloud.blit()
        self.rocket.blit()

    def flight_update(self):
        self.bird.change()
        self.bird.moveright(2)
        self.cloud.moveright(1)
        self.rocket.change_mode()
        self.background.movedown(10)
        self.bird.movedown(10)
        self.cloud.movedown(10)
        if self.background.rely > 1400:
            self.game_state = "maingame"
            self.background.mode = "main"
            self.background.rely= -600
            self.background.ashon = False

    def maingame_draw(self):
        self.background.blit()
        self.backstars.blit_stars()
        self.rocket.blit()
    
    def maingame_update(self):
        self.maincount = (self.maincount+1) % 40
        if self.background.rely < 0:
            self.background.movedown(10)
        self.rocket.change_mode()
        #We'd like to generate stars everynow and then. So we can use the gamecount to do so. If the count is a multiple of, say 40, lets add a star.
        if self.maincount == 0:
            self.backstars.add_star()


        self.backstars.update_stars()
        if self.rocket.rely< 380:
            self.rocket.moveup(-4)
    


    def draw(self):
        if self.game_state == "menu":
            self.menu_draw()
        elif self.game_state == "liftoff":
            self.liftoff_draw()
        elif self.game_state == "flight":   
            self.flight_draw()
        elif self.game_state == "maingame":
            self.maingame_draw()

    def update(self):
        if self.game_state == "menu":
            self.menu_update()
        elif self.game_state == "liftoff":
            self.liftoff_update()
        elif self.game_state == "flight":
            self.flight_update()   
        elif self.game_state == "maingame": 
            self.maingame_update()

    def run(self):
        while self.running:
            self.event_handling()
            self.update()
            self.draw()
            # pygame.display.flip()
            pygame.display.update()
            self.clock.tick(30)
            keys = pygame.key.get_pressed()  # Checking pressed keys
            if keys[pygame.K_LEFT]:
                self.rocket.set_direciton('left')
                self.rocket.moveleft(8)
            if keys[pygame.K_RIGHT]:
                self.rocket.set_direciton('right')
                self.rocket.moveright(8)

            

if __name__ == "__main__":
    game = Game()
    game.run()

