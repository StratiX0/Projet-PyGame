import pygame
from player import Player
from ennemie import Ennemie
from scroller import Scroll
from animation import AnimateSprite
from score import Score

class Game:
    def __init__(self, screen):
        self.all_players = pygame.sprite.Group()
        self.animation = AnimateSprite("piaf", self)
        self.scroll = Scroll(screen)
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_ennemie = pygame.sprite.Group()
        self.pressed = {}
        self.ennemie = Ennemie(self)
        self.spawn_ennemie()
        self.spawn_ennemie()
        self.score = Score()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_ennemie(self):
        ennemie = Ennemie(self)
        self.all_ennemie.add(ennemie)
    
    def ajoutScore(self,):
        self.score.ajouterScore()

    def afficherScore(self, screen):
        self.score.afficherScore(screen)


