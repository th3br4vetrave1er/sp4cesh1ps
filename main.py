import pygame

# General setup

pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
runnig = True


while runnig:
    # Event loop here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    # Draw of a game



pygame.quit()

