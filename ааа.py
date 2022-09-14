import pygame
import random
import time
from setting import *
from main_logic import *

pygame.init()
pygame.display.set_mode((W, H))
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

bg_surf = pygame.image.load("img/bckg2.png").convert()
bg_surf = pygame.transform.scale(bg_surf, (1200, 750))
sc.blit(bg_surf, (0, 0))

f = 0
cats = []
enemys =[]
running = True

nos  = Enemy("nos", 1000, 10, 1, "img/nos.png")
enemys.append(nos)
fps = 0
while running:
    if f > 15:
        f = 0
    sc.blit(bg_surf, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cats.append(Cat("Shishilan", 1000, 1000000, 0.7, "img/shishilan.png"))
            if event.key == pygame.K_RIGHT:
                cats.append(Cat("Sshishilan", 1000, 1000000, 0.7, "img/balaluga.png"))


    if cats:
        for cat in cats:
            cat.image = cat.image.convert_alpha()
            if cat.hp > 0:
                if cat.x < W and cat.x > 0 and all([cat.x >  enemy.x + enemy.rect.bottom for enemy in enemys]):
                    cat.update(f, sc)
                else:
                    #if
                    print(max([100, 1]))
                    sc.blit(cat.image, (cat.x, cat.y))



    if enemys:
        for enemy in enemys:
            enemy.image = enemy.image.convert_alpha()
            if enemy.x < W and enemy.x != W and all([enemy.x <  cat.x - cat.rect.bottom for cat in cats]):
                enemy.update(f, sc)
            else:
                enemy.x = enemy.x
                sc.blit(enemy.image, (enemy.x, enemy.y))
    pygame.display.update()
    clock.tick(FPS)

    f += 1
    fps += 1
    print(fps)
