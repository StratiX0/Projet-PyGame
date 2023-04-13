import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 25.1
        self.player = player
        self.image = pygame.image.load("assets/projectille/beams.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 20

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        # Check si le projectile est tjr dand l'écran
        if self.rect.x > 1030:
            self.remove()

        for ennemie in self.player.game.check_collision(self, self.player.game.all_ennemie):
            self.remove()

            ennemie.degat(self.player.attack)
        
