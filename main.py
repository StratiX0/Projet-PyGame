import pygame
import math
import random
from Vaisseau import Vaisseau, SCREEN_HEIGHT, SCREEN_WIDTH
from Missil import Missil
from Bot import Bot
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Endless Scroll")

#charger l'image
bg = pygame.image.load("bg.png").convert()
player = pygame.image.load("player_plane.png").convert()
bot = pygame.image.load("player_plane_bot.png").convert()

#Définitions de variables utile
clock = pygame.time.Clock()
FPS = 60
bg_width = bg.get_width()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
dt = 0
player_pos = pygame.Vector2(SCREEN_WIDTH / 2, screen.get_height() / 2)




liste_bot = []
i=0
while i < random.randint(1,20):
    bot_pos = pygame.Vector2(SCREEN_WIDTH, random.randint(0,SCREEN_HEIGHT-25))
    liste_bot.append(bot_pos)
    i+=1



#Boucle du jeu
run = True




    
while run:

    clock.tick(FPS)
    #affiche l'image à la fin de la dernière
    for i in range(0 , tiles):
        screen.blit(bg, (i * bg_width + scroll,0))

    scroll -= 5 

    if abs(scroll) > bg_width:
        scroll = 0
    
    object = Vaisseau()
    object.v_deplacement(player_pos, player, dt, screen)
    d={}
    i=0
    for i in liste_bot:
        d["object_bot{0}".format(i)] = Bot()
        d["object_bot{0}".format(i)].b_deplacement(i, bot, dt, screen)
    
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()