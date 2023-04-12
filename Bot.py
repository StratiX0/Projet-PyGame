import pygame
import random
from Vaisseau import SCREEN_HEIGHT, SCREEN_WIDTH

class Bot:

    def __init__(self):
        self.vie = 500
        self.degat = 50
        self.speed = 500
        self.avance = True

    def b_deplacement(self,bot_pos, bot, dt, screen):
        screen.blit(bot,bot_pos)

        print(self.avance)
        if bot_pos.x >= SCREEN_WIDTH:
            self.avance = True
        elif bot_pos.x <=250:
            self.avance = False


        # fait déplacer le bot vers la gauche
        if self.avance == True:
            bot_pos.x -= self.speed * dt
        else:
            bot_pos.x += self.speed * dt

    