import pygame

pygame.init()

res = (800, 600)
screen_surface = pygame.display.set_mode(res)
pygame.display.set_caption("Jeu Pygame")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False














