import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/perso/player_plane.png")
        self.image = pygame.transform.scale(self.image , (100,50))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    
    def degat(self, attack) : 
        
        self.health -= attack

        if self.health <= 0 : 
            self.rect.x = 400
            self.rect.y = 300
            self.health = self.max_health
        

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        # check si on touche pas un monstre
        if not self.game.check_collision(self,self.game.all_ennemie):
            self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity

    def bar_de_vie(self, surface):

        pygame.draw.rect(surface, (255,0,0), [self.rect.x, self.rect.y -5, self.health, 5])
        
        pygame.draw.rect(surface, (11,210,46), [self.rect.x, self.rect.y -5, self.health, 5])
        

