import pygame

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, game):
        super().__init__()
        self.image = pygame.image.load(f"assets/perso/{sprite_name}/{sprite_name}1.png")
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.game = game
        self.flip = True

    def animate(self):
        self.current_image += 1
        if self.current_image >= len(self.images):
            self.current_image = 0
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image,(80,80))
        print(self.game.animation.flip)
        if self.game.animation.flip == True:
            self.image = pygame.transform.flip(self.image, True, False)


def load_animation_images(sprite_name):
    image = []
    path = f"assets/perso/{sprite_name}/{sprite_name}"
    for i in range(1,6):
        image_path = path + str(i) + ".png"
        image.append(pygame.image.load(image_path))
    return image

animations = {
    "piaf" : load_animation_images("piaf")
}

