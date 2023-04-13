import pygame 
import math

class Scroll :
    def __init__(self, screen):
        self.image = pygame.image.load("assets/fond/bg_scroll.png")
        # self.image = pygame.transform.scale(self.image,(720,720))
        self.bg_width = self.image.get_width()
        self.tiles = math.ceil(1080 / self.bg_width) + 1
        self.screen = screen
        self.scroll_pos = 0
        pygame.time.Clock().tick(60)
        

    def scroll(self):
        
        for i in range(0 , self.tiles):
            self.screen.blit(self.image,(i * self.bg_width + self.scroll_pos, 0))

        self.scroll_pos -= 10

        if abs(self.scroll_pos) > self.bg_width:
            self.scroll_pos = 0

            