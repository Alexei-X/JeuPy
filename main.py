#coding:utf-8

# importation des modules pygame, random et time
import pygame
import time
import random

# variables des couleurs
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# temps initial
begin_time = time.time()

# initialisation de pygame
pygame.init()

# création de la fenêtre
res = (400, 500)
screen_surface = pygame.display.set_mode(res)
pygame.display.set_caption("Jeu Pygame")

# création du joueur
player_x = 150
player_y = 190
player = pygame.Rect(player_x, player_y, 30, 60)
pygame.draw.rect(screen_surface, blue, player)
pygame.display.flip()

# création de l'ennemi 1
ennemy1_x = random.choice(range(0, 370, 10))
ennemy1_y = -70
ennemy1 = pygame.Rect(ennemy1_x, -60, 40, 60)

# création de l'ennemi 2
ennemy2_x = random.choice(range(0, 370, 10))
ennemy2_y = -70
ennemy2 = pygame.Rect(ennemy2_x, -60, 40, 60)

# création de l'ennemi 3
ennemy3_x = random.choice(range(0, 370, 10))
ennemy3_y = -70
ennemy3 = pygame.Rect(ennemy3_x, -60, 40, 60)

# création de l'ennemi 4
ennemy4_x = random.choice(range(0, 370, 10))
ennemy4_y = -70
ennemy4 = pygame.Rect(ennemy4_x, -60, 40, 60)

# fonction de collision
def collide():
    if player.colliderect(ennemy1) or player.colliderect(ennemy2) or player.colliderect(ennemy3)\
    or player.colliderect(ennemy4):
        quit()

# fonction pour aller à droite
def moveRight():
    global player_x, player_y, ennemy1_x, ennemy1_y, ennemy2_x, ennemy2_y, ennemy3_x, ennemy3_y, ennemy4_x, ennemy4_y
    time.sleep(.010)
    if player_x >= 370:
        pass
    else:
        player_x += 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        ennemy1 = pygame.Rect(ennemy1_x, ennemy1_y, 40, 60)
        ennemy2 = pygame.Rect(ennemy2_x, ennemy2_y, 40, 60)
        ennemy3 = pygame.Rect(ennemy3_x, ennemy3_y, 40, 60)
        ennemy4 = pygame.Rect(ennemy4_x, ennemy4_y, 40, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.draw.rect(screen_surface, red, ennemy1)
        pygame.draw.rect(screen_surface, red, ennemy2)
        pygame.draw.rect(screen_surface, red, ennemy3)
        pygame.draw.rect(screen_surface, red, ennemy4)
        pygame.display.flip()

# fonction pour aller à gauche
def moveLeft():
    global player_x, player_y, ennemy1_x, ennemy1_y, ennemy1, ennemy2_x, ennemy2_y, ennemy2
    time.sleep(.010)
    if player_x <= 0:
        pass
    else:
        player_x -= 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        ennemy1 = pygame.Rect(ennemy1_x, ennemy1_y, 40, 60)
        ennemy2 = pygame.Rect(ennemy2_x, ennemy2_y, 40, 60)
        ennemy3 = pygame.Rect(ennemy3_x, ennemy3_y, 40, 60)
        ennemy4 = pygame.Rect(ennemy4_x, ennemy4_y, 40, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.draw.rect(screen_surface, red, ennemy1)
        pygame.draw.rect(screen_surface, red, ennemy2)
        pygame.draw.rect(screen_surface, red, ennemy3)
        pygame.draw.rect(screen_surface, red, ennemy4)
        pygame.display.flip()

# fonction pour aller en haut
def moveUp():
    global player_x, player_y, ennemy1_x, ennemy1_y, ennemy1, ennemy2_x, ennemy2_y, ennemy2
    time.sleep(.010)
    if player_y <= 0:
        pass
    else:
        player_y -= 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        ennemy1 = pygame.Rect(ennemy1_x, ennemy1_y, 40, 60)
        ennemy2 = pygame.Rect(ennemy2_x, ennemy2_y, 40, 60)
        ennemy3 = pygame.Rect(ennemy3_x, ennemy3_y, 40, 60)
        ennemy4 = pygame.Rect(ennemy4_x, ennemy4_y, 40, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.draw.rect(screen_surface, red, ennemy1)
        pygame.draw.rect(screen_surface, red, ennemy2)
        pygame.draw.rect(screen_surface, red, ennemy3)
        pygame.draw.rect(screen_surface, red, ennemy4)
        pygame.display.flip()

# fonction pour aller en bas
def moveDown():
    global player_x, player_y, ennemy1_x, ennemy1_y, ennemy1, ennemy2_x, ennemy2_y, ennemy2
    time.sleep(.010)
    if player_y >= 440:
        pass
    else:
        player_y += 5
        screen_surface.fill(black)
        player = pygame.Rect(player_x, player_y, 30, 60)
        ennemy1 = pygame.Rect(ennemy1_x, ennemy1_y, 40, 60)
        ennemy2 = pygame.Rect(ennemy2_x, ennemy2_y, 40, 60)
        ennemy3 = pygame.Rect(ennemy3_x, ennemy3_y, 40, 60)
        ennemy4 = pygame.Rect(ennemy4_x, ennemy4_y, 40, 60)
        pygame.draw.rect(screen_surface, blue, player)
        pygame.draw.rect(screen_surface, red, ennemy1)
        pygame.draw.rect(screen_surface, red, ennemy2)
        pygame.draw.rect(screen_surface, red, ennemy3)
        pygame.draw.rect(screen_surface, red, ennemy4)
        pygame.display.flip()

# fonction de spawn d'ennemi 1
def spawn_ennemy1():
    global ennemy1, ennemy_x1, ennemy_y1
    ennemy_y1 = -70
    ennemy_x1 = random.choice(range(0, 370, 10))
    ennemy1 = pygame.Rect(ennemy_x1, ennemy_y1, 40, 60)
    pygame.draw.rect(screen_surface, red, ennemy1)
    pygame.display.flip()

# fonction de spawn d'ennemi 2
def spawn_ennemy2():
    global ennemy2, ennemy2_x, ennemy2_y
    ennemy2_y = -70
    ennemy2_x = random.choice(range(0, 370, 10))
    ennemy2 = pygame.Rect(ennemy2_x, ennemy2_y, 40, 60)
    pygame.draw.rect(screen_surface, red, ennemy2)
    pygame.display.flip()

# fonction de spawn d'ennemi 3
def spawn_ennemy3():
    global ennemy3, ennemy3_x, ennemy3_y
    ennemy3_y = -70
    ennemy3_x = random.choice(range(0, 370, 10))
    ennemy3 = pygame.Rect(ennemy3_x, ennemy3_y, 40, 60)
    pygame.draw.rect(screen_surface, red, ennemy3)
    pygame.display.flip()

# fonction de spawn d'ennemi 4
def spawn_ennemy4():
    global ennemy4, ennemy4_x, ennemy4_y
    ennemy4_y = -70
    ennemy4_x = random.choice(range(0, 370, 10))
    ennemy4 = pygame.Rect(ennemy4_x, ennemy2_y, 40, 60)
    pygame.draw.rect(screen_surface, red, ennemy4)
    pygame.display.flip()

# fonction de mouvement de l'ennemi
def move_ennemy():
    global ennemy1, ennemy1_x, ennemy1_y, ennemy2, ennemy2_x, ennemy2_y, player, player_x, player_y, ennemy3_y, ennemy4_y
    time.sleep(.007)
    ennemy1_y += 10
    ennemy2_y += 10
    ennemy3_y += 10
    ennemy4_y += 10
    ennemy1 = pygame.Rect(ennemy1_x, ennemy1_y, 40, 60)
    ennemy2 = pygame.Rect(ennemy2_x, ennemy2_y, 40, 60)
    ennemy3 = pygame.Rect(ennemy3_x, ennemy3_y, 40, 60)
    ennemy4 = pygame.Rect(ennemy4_x, ennemy4_y, 40, 60)
    player = pygame.Rect(player_x, player_y, 30, 60)
    screen_surface.fill(black)
    pygame.draw.rect(screen_surface, red, ennemy1)
    pygame.draw.rect(screen_surface, red, ennemy2)
    pygame.draw.rect(screen_surface, red, ennemy3)
    pygame.draw.rect(screen_surface, red, ennemy4)
    pygame.draw.rect(screen_surface, blue, player)
    pygame.display.flip()
    collide()
    

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
        
    if begin_time < 1:
        continue
    else:
        if int(time.time() - begin_time) % 2 == 0:
            spawn_ennemy1()
        elif int(time.time() - begin_time) % 3 == 0:
            spawn_ennemy2()
        elif int(time.time() - begin_time) % 4 == 0:
            spawn_ennemy3()
        elif int(time.time() - begin_time) % 5 == 0:
            spawn_ennemy4()
            
    move_ennemy()
