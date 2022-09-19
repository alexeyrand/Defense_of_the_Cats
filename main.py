import pygame
import random
from animations import *
from setting import *
from logic import *



pygame.init()
pygame.display.set_mode((W, H))
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

bg_surf = pygame.image.load("image/bckg2.png").convert_alpha()
win = pygame.image.load("image/pobeda.png").convert_alpha()
win_rect = win.get_rect()
bg_surf = pygame.transform.scale(bg_surf, (1200, 750))


wg = pygame.image.load("image/Wings.png").convert_alpha()

cats = pygame.sprite.Group()
#cats.add(give_cat("test"))
enemys = pygame.sprite.Group()
bases = []

level = 1

time = 0
running = True

level = 1


while running:
    Level.play(Level, time, enemys, bases, level)
    sc.blit(bg_surf, (0, 0))
    if bases[0].hp > 0 and bases[1].hp > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cats.add(give_cat("Shishilan"))
                if event.key == pygame.K_RIGHT:
                    cats.add(give_cat("Base_cat"))
    elif bases[0].hp <= 0:
        sc.blit(win, (W//2 - win_rect.right // 2, H//2 - win_rect.bottom))
    elif bases[1].hp <= 0:
        sc.blit(win, (W//2 - win_rect.right // 2, H//2 - win_rect.bottom))

    for base in bases:
        if base.x == 40:      #base enemy
            base.update(sc)
        if base.x == 1082:    #base cat
            base.update(sc)

    for cat in cats:
        if cat.x > 0 and (all([(cat.x - cat.attack_range) > enemy.x + enemy.rect.right for enemy in enemys]) and (cat.x - cat.attack_range) > bases[0].x + bases[0].rect.right):
            cat.update(sc)
        else:
            cat.stay(sc, enemys, bases)

    for enemy in enemys:
        if enemy.x < W and enemy.x + enemy.rect.right != W and (all([(enemy.x + enemy.attack_range + enemy.rect.right) < cat.x for cat in cats]) and (enemy.x + enemy.attack_range + enemy.rect.right) < bases[1].x):
            enemy.update(sc)
        else:
            enemy.stay(sc, cats, bases)
    for wing in wings:
        wing.drow(sc)
    pygame.display.update()
    clock.tick(FPS)


    time += 1
    #print(fps)
