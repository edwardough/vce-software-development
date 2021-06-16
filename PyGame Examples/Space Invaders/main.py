import pygame, random, math
from pygame import mixer

# declare constants
WIDTH = 800
HEIGHT = 600
P_VELOCITY = 4
E_VELOCITY = 0.5
NUM_ENEMIES = 6
NUM_ENEMY_ROWS = 6
TOTAL_ENEMIES = NUM_ENEMY_ROWS * NUM_ENEMIES
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
score_font = pygame.font.Font('freesansbold.ttf', 24)
over_font = pygame.font.Font('freesansbold.ttf', 64)
# mixer.music.load("background-music.wav")
# mixer.music.play(-1)

# classes and functions
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
    HORIZONTAL_SCALER = 120
    def __init__(self, eImg, eX, eY):
        self.img = eImg
        self.x = eX
        self.y = eY
        self.direction = 1
        self.moves = 1
        self.alive = True
    def update(self):
        self.x += self.direction * E_VELOCITY
        if self.moves % Enemy.HORIZONTAL_SCALER == 0: # CURRENTLY GLITCHING AT HIGH LEVELS
            self.direction = -self.direction
            self.y += 10
        self.moves += 1
    def show(self):
        global screen
        if self.alive == True:
            screen.blit(self.img, (self.x,self.y))

class Laser():
    def __init__(self, lImg, lX, lY):
        self.img = lImg
        self.x = lX
        self.y = lY
        self.direction = -1
        self.liveRound = True
    def update(self):
        self.y += self.direction * P_VELOCITY
    def show(self):
        global screen
        if self.liveRound == True:
            screen.blit(self.img, (self.x,self.y))        

def isLaserHit( theEnemy, theLaser ):
    if theEnemy.alive == True and theLaser.liveRound == True:
        distance = math.sqrt(math.pow((theEnemy.x + 32) - (theLaser.x + 8), 2) + (math.pow((theEnemy.y + 32) - theLaser.y, 2)))
        if distance < 27:
            return True
        else:
            return False

def show_score( fontX, fontY ):
    score = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (fontX, fontY))

def goUpLevel( ):
    global enemies, E_VELOCITY
    E_VELOCITY *= 1.2
    Enemy.HORIZONTAL_SCALER = int(Enemy.HORIZONTAL_SCALER * 0.8)
    enemies = []
    for i in range(0,NUM_ENEMY_ROWS):
        enemies.append([])
    for j in range(0,NUM_ENEMY_ROWS):
        for k in range(0,NUM_ENEMIES):
            enemies[j].append( Enemy(pygame.image.load('enemy-64.png'), 35 + k * ENEMY_X_GAP ,20 + j * ENEMY_Y_GAP) )

# initialise game objects and variables
score_value = 0
p1 = Player(pygame.image.load('spaceship-64.png'),360,500,0)
lasers = []
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
            if event.key == pygame.K_SPACE:
                lasers.append( Laser(pygame.image.load('laser-16.png'),p1.x + 23,p1.y-15))
                laserSound = mixer.Sound("laser-sound.wav")
                laserSound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Left or right released")
                p1.dx = 0

    clock.tick( FRAMERATE )
    
    p1.update()
    p1.show()
    
    for i in range(0,NUM_ENEMY_ROWS):
        for j in range(0,NUM_ENEMIES):
            enemies[i][j].update()
            enemies[i][j].show()

    # check if any laser shots have left the screen
    popLaser = False
    for laser in lasers:
        if laser.y <= 0:
            popLaser = True
        laser.update()
        laser.show()
    if popLaser == True: 
        lasers.pop(0) # note don't try this inside previous loop

    for laser in lasers: # check if any lasers hit their targets
        for i in range(0,NUM_ENEMY_ROWS):
            for j in range(0,NUM_ENEMIES):
                if isLaserHit(enemies[i][j],laser) == True:
                    score_value += 1 # add to score
                    enemies[i][j].alive = False
                    laser.liveRound = False
                    explosionSound = mixer.Sound("explosion-sound.wav") 
                    explosionSound.play()
                    if score_value % TOTAL_ENEMIES == 0:
                        goUpLevel()

    show_score( 10, 10 )

    pygame.display.update()



