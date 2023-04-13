import pygame
from game import Game
from score import Score

 
pygame.init()

#générer la fenètre du jeu
screen = pygame.display.set_mode((1080,720))
icon = pygame.image.load("assets/icon.jpg")
pygame.display.set_caption("Pycarus")
pygame.display.set_icon(icon)

game = Game(screen)

running = True
while running :
    pygame.time.Clock().tick(60)

    # Affichage des images
    game.scroll.scroll()
    screen.blit(game.player.image, game.player.rect)
    game.player.all_projectiles.draw(screen)
    game.all_ennemie.draw(screen)
    game.afficherScore(screen)

        # Charger les sprites par groupe
    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.bar_de_vie(screen)

    for ennemie in game.all_ennemie:
        ennemie.move()
        ennemie.bar_de_vie(screen)
        ennemie.update_animation()

    # Gestion des mouvements
    if (game.pressed.get(pygame.K_z) or game.pressed.get(pygame.K_UP)) and game.player.rect.y > 0:
        game.player.move_up()
    if (game.pressed.get(pygame.K_s) or game.pressed.get(pygame.K_DOWN)) and game.player.rect.y < 680:
        game.player.move_down()
    if (game.pressed.get(pygame.K_q) or game.pressed.get(pygame.K_LEFT)) and game.player.rect.x > 0: 
        game.player.move_left()
    if (game.pressed.get(pygame.K_d) or game.pressed.get(pygame.K_RIGHT)) and game.player.rect.x < 980:
        game.player.move_right()


    #MAJ de l'écran
    pygame.display.flip()
    

    # Shutdown la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            with open('score.txt', 'a') as f:
                f.write(f"Score : {str(game.score.score)}\n")
            pygame.quit()

    #Detecter si des touche sdu clavier sont appuyer
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
    #Detecter si des touche sdu clavier sont relacher
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False   



    
      