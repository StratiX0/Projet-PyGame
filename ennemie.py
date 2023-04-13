import pygame
import random
import animation

class Ennemie(animation.AnimateSprite):
    def __init__(self, game) :
        super().__init__("piaf",game)
        self.game = game
        self.health = 50
        self.max_health = 100
        self.attack = 5
        self.velocity = 15
        self.image = pygame.image.load("assets/perso/piaf/piaf1.png")
        self.rect = self.image.get_rect()
        self.rect.x  = 1250
        self.rect.y = 100  + random.randint(0,500)
        self.gauche = True
        self.all_projectiles = pygame.sprite.Group()

    def degat(self, attack):
        self.health -= attack
        if self.health <= 0 :
            self.game.score.ajouterScore()
            self.rect.x = 1250
            self.rect.y = 100 + random.randint(0,500)
            self.health = self.max_health
            
    def move(self):
        if self.rect.x >= 1300:
            self.gauche = True
        elif self.rect.x <= -250:
            self.gauche = False

        if not self.game.check_collision(self, self.game.all_players):
            if self.gauche == True:
                self.rect.x -= self.velocity
                self.game.animation.flip = True
                # self.rect.y -= self.velocity 
            else:
                self.rect.x += self.velocity
                self.game.animation.flip = False
                # self.rect.y += self.velocity
        else :
            self.game.player.degat(self.attack)

    def update_animation(self):
        self.animate()

    def bar_de_vie(self, surface):

        pygame.draw.rect(surface, (255,0,0), [self.rect.x, self.rect.y -5, self.health, 5])

        pygame.draw.rect(surface, (11,210,46), [self.rect.x, self.rect.y -5, self.health, 5])
        

# class Piaf(Ennemie):
#     def __init__(self,game):
#         super().__init__(game, "piaf")

    