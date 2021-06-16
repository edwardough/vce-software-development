import pygame

# initialise pygame
pygame.init()
pygame.display.set_caption("Space Invaders - FCC")
# icon by https://www.freepik.com
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# variables
WIDTH = 800
HEIGHT = 600

# create the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))



# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



