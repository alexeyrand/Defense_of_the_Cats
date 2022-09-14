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

bg_surf = pygame.image.load("image/bckg2.png").convert_alpha()
bg_surf = pygame.transform.scale(bg_surf, (1200, 750))

cats = pygame.sprite.Group()

enemys = pygame.sprite.Group()

level = 1

fps = 0
running = True


level = 1
flag = False
while running:
    sc.blit(bg_surf, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cats.add(Cat("Shishilan", 1000, 1000000, 1.4, 120, 70, "image/animations/Cats/shishilan/shishilan.png", shishilan_animations))
            if event.key == pygame.K_RIGHT:
                cats.add(Cat("Cat", 1000, 1000000, 1.4, 60, 55, "image/animations/Cats/cat/cat1.png", cat_animations))


    Level.play(Level, fps, enemys, level)
    for cat in cats:
        if cat.x > 0 and all([cat.x - cat.attack_range > enemy.x for enemy in enemys]):
            cat.update(sc)
            print(cat.rect.bottom)
        else:
            cat.stay(sc)
    for enemy in enemys:
        if enemy.x < W and enemy.x != W and all([enemy.x + enemy.attack_range < cat.x for cat in cats]):
            enemy.update(sc)
        else:
            enemy.stay(sc)

    pygame.display.update()
    clock.tick(FPS)


    fps += 1
    #print(fps)
