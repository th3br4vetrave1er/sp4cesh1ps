import pygame
from os.path import join
from random import random, randint
# General setup

pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("SP4CESH1PS")

running = True

# Plain Surface
surf = pygame.Surface((100,200))
surf.fill("darkgreen")
x = 100

# Importing image
star_surf = pygame.image.load(join("images","star.png")).convert_alpha()
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # Event loop here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    # Draw of a game

    display_surface.fill("purple")
    x += 0.1
    display_surface.blit(player_surf, (x,150))
    for pos in star_positions:
              display_surface.blit(star_surf, pos)

    pygame.display.update()



pygame.quit()

