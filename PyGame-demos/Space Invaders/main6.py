import pygame, random

# declare constants
WIDTH = 800
HEIGHT = 600
P_VELOCITY = 4
E_VELOCITY = 0.5
NUM_ENEMIES = 6
NUM_ENEMY_ROWS = 3
ENEMY_X_GAP = 120
ENEMY_Y_GAP = 60
FRAMERATE = 100

# pygame set up
pygame.init()
pygame.display.set_caption("Space Invaders - FCC")
icon = pygame.image.load('spaceship-32.png') # icons by https://www.freepik.com
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load('background.png')
clock = pygame.time.Clock()

# create any classes
class Player():
    def __init__(self, pImg, pX, pY, p_dX):
        self.img = pImg
        self.x = pX
        self.y = pY
        self.dx = p_dX
    def update(self):
        self.x += self.dx
        # ensure the player doesn't leave the screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
    def show(self):
        global screen
        screen.blit(self.img, (self.x,self.y))

class Enemy():
    def __init__(self, eImg, eX, eY):
        self.img = eImg
        self.x = eX
        self.y = eY
        self.direction = 1
        self.moves = 1
    def update(self):
        self.x += self.direction * E_VELOCITY
        if self.moves % 125 == 0:
            self.direction = -self.direction
            self.y += 10
        self.moves += 1

    def show(self):
        global screen
        screen.blit(self.img, (self.x,self.y))

        

# initialise game objects
p1 = Player(pygame.image.load('spaceship-64.png'),360,500,0)
enemies = []
for i in range(0,NUM_ENEMY_ROWS):
    enemies.append([])
for j in range(0,NUM_ENEMY_ROWS):
    for k in range(0,NUM_ENEMIES):
        enemies[j].append( Enemy(pygame.image.load('enemy-64.png'), 35 + k * ENEMY_X_GAP ,20 + j * ENEMY_Y_GAP) )

# game loop
running = True
while running:
    screen.fill((0,0,0)) # give the background an RGB value
    screen.blit(background, (0, 0)) # background Image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("Left pressed")
                p1.dx = -P_VELOCITY
            if event.key == pygame.K_RIGHT:
                # print("Right pressed")
                p1.dx = P_VELOCITY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Left or right released")
                p1.dx = 0
    clock.tick( FRAMERATE )
    p1.update()
    p1.show() # draw AFTER filling the background
    
    for i in range(0,NUM_ENEMY_ROWS):
        for j in range(0,NUM_ENEMIES):
            enemies[i][j].update()
            enemies[i][j].show()
    # for enemy in enemies:
    #     enemy.update()
    #     enemy.show()
    
    pygame.display.update()



