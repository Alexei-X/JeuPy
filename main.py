#coding:utf-8

# importation des modules pygame et time
import pygame
import time

# variables des couleurs
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# initialisation de pygame
pygame.init()

# création de la fenêtre
res = (800, 600)
screen_surface = pygame.display.set_mode(res)
pygame.display.set_caption("Jeu Pygame")

# création du joueur
player_x = 350
player_y = 240
player = pygame.Rect(player_x, player_y, 30, 60)
pygame.draw.rect(screen_surface, blue, player)
pygame.display.flip()

# fonction pour aller à droite
def moveRight():
    global player_x, player_y
    time.sleep(.030)
    if player_x >= 770:
        pass
    else:
        player_x += 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.display.flip()

# fonction pour aller à gauche
def moveLeft():
    global player_x, player_y
    time.sleep(.030)
    if player_x <= 0:
        pass
    else:
        player_x -= 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.display.flip()

# fonction pour aller en haut
def moveUp():
    global player_x, player_y
    time.sleep(.030)
    if player_y <= 0:
        pass
    else:
        player_y -= 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.display.flip()

# fonction pour aller en bas
def moveDown():
    global player_x, player_y
    time.sleep(.030)
    if player_y >= 540:
        pass
    else:
        player_y += 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.display.flip()

# boucle principale du jeu
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        moveRight()
    elif keys[pygame.K_LEFT]:
        moveLeft()
    elif keys[pygame.K_UP]:
        moveUp()
    elif keys[pygame.K_DOWN]:
        moveDown()
    print(player_y)















