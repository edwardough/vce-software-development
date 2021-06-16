import pygame

# initialise pygame
pygame.init()

# variables
WIDTH = 800
HEIGHT = 600

# create the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



