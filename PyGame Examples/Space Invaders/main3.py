import pygame

# initialise pygame
pygame.init()
pygame.display.set_caption("Space Invaders - FCC")
icon = pygame.image.load('spaceship-32.png') # icon by https://www.freepik.com
pygame.display.set_icon(icon)

# declare important variables and constants
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# create any classes
class Player():
    def __init__(self, pImg, pX, pY):
        self.img = pImg
        self.x = pX
        self.y = pY
    def update(self):
        global screen
        screen.blit(self.img, (self.x,self.y))

# create any objects
p1 = Player(pygame.image.load('spaceship-64.png'),360,490)

# game loop
running = True
while running:

    screen.fill((0,0,0)) # give the background an RGB value

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    p1.update() # draw AFTER filling the background
    pygame.display.update()



