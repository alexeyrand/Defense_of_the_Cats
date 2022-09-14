import pygame
import random
from animations import *
from setting import *
from main_logic import *

pygame.init()
pygame.display.set_mode((W, H))
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

bg_surf = pygame.image.load("image/bckg2.png").convert()
bg_surf = pygame.transform.scale(bg_surf, (1200, 750))

cats = pygame.sprite.Group()
enemys = pygame.sprite.Group()

level = 1



fps = 0
running = True


level = 1
while running:
    sc.blit(bg_surf, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cats.add(Cat("Shishilan", 1000, 1000000, 0.4, "image/animations/shishilan/shishilan.png", shishilan_animations))
            if event.key == pygame.K_RIGHT:
                cats.add(Cat("Balaluga", 1000, 1000000, 0.4, "image/balaluga.png", shishilan_animations))


    Level.play(Level, fps, enemys, level)
    cats.update(sc)

    enemys.update(sc)

    pygame.display.update()
    clock.tick(FPS)


    fps += 1
    print(fps)
