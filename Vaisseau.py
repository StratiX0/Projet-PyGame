import pygame

#Gérer l'affichage de la fenètre 
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600


class Vaisseau:
    def __init__(self):
        self.vie = 500
        self.speed = 300

    def v_deplacement(self,player_pos, player, dt, screen):
        screen.blit(player,player_pos)

        keys = pygame.key.get_pressed()
        # déplace le joueur vers le haut si les bonnes touches sont presséees, et empêche le joueur de sortir de l'écran
        if (keys[pygame.K_z] or keys[pygame.K_UP]) and player_pos.y > 0:
            player_pos.y -= self.speed * dt
        # déplace le joueur vers le bas si les bonnes touches sont presséees, et empêche le joueur de sortir de l'écran
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_pos.y < SCREEN_HEIGHT-25:
            player_pos.y += self.speed * dt
        # déplace le joueur vers la gauche si les bonnes touches sont presséees, et empêche le joueur de sortir de l'écran
        if (keys[pygame.K_q] or keys[pygame.K_LEFT]) and player_pos.x > 0:
            player_pos.x -= self.speed * dt
        # déplace le joueur vers la droite si les bonnes touches sont presséees, et empêche le joueur de sortir de l'écran
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_pos.x < SCREEN_WIDTH-60:
            player_pos.x += self.speed * dt

   