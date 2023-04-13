import pygame
from ennemie import Ennemie

class Score:
    def __init__(self) :
        self.score = 0
        
    def ajouterScore(self):
        self.score += 1


    def afficherScore(self, screen):
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))