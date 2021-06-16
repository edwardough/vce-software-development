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
VELOCITY = 0.2

# create any classes
class Player():
    def __init__(self, pImg, pX, pY):
        self.img = pImg
        self.x = pX
        self.y = pY
    def update(self, dx, dy):
        self.x += dx
        self.y += dy
        # ensure the player doesn't leave the screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
    def show(self):
        global screen
        screen.blit(self.img, (self.x,self.y))

# create any objects
p1 = Player(pygame.image.load('spaceship-64.png'),360,490)
p1_dx = 0

# game loop
running = True
while running:
    screen.fill((0,0,0)) # give the background an RGB value
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("Left pressed")
                p1_dx = -VELOCITY
            if event.key == pygame.K_RIGHT:
                # print("Right pressed")
                p1_dx = VELOCITY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Left or right released")
                p1_dx = 0
    p1.update(p1_dx,0)
    p1.show() # draw AFTER filling the background
    pygame.display.update()



