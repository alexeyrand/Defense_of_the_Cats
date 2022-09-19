import pygame
import random
import time
pygame.init()
clock = pygame.time.Clock()

##          Move animations
##______________________________________________________________________________
##          Cats
##______________________________________________________________________________
##          Cat

cat_animations_move = [pygame.image.load("image/animations/Cats/cat/cat1.png"), pygame.image.load("image/animations/Cats/cat/cat2.png"), pygame.image.load("image/animations/Cats/cat/cat3.png"), pygame.image.load("image/animations/Cats/cat/cat4.png")]

cat_animations_attack = [pygame.image.load("image/animations/Cats/cat/cat1_attack.png"), pygame.image.load("image/animations/Cats/cat/cat2_attack.png"), pygame.image.load("image/animations/Cats/cat/cat3_attack.png"), pygame.image.load("image/animations/Cats/cat/cat1_attack.png")]

cat_animations = {"move": cat_animations_move,
                  "attack": cat_animations_attack}


##______________________________________________________________________________
##          Shishilan

shishilan_animations_move = [pygame.image.load("image/animations/Cats/shishilan/shishilan.png"), pygame.image.load("image/animations/Cats/shishilan/shishilan2.png"), pygame.image.load("image/animations/Cats/shishilan/shishilan3.png"), pygame.image.load("image/animations/Cats/shishilan/shishilan2.png")]

shishilan_animations_attack = [pygame.image.load("image/animations/Cats/balaluga/balaluga1.png"), pygame.image.load("image/animations/Cats/balaluga/balaluga1.png"), pygame.image.load("image/animations/Cats/balaluga/balaluga1.png"), pygame.image.load("image/animations/Cats/balaluga/balaluga1.png")]

shishilan_animations = {"move": shishilan_animations_move,
                        "attack": shishilan_animations_attack}

##______________________________________________________________________________
##          Balaluga

balaluga_animations_move = [pygame.image.load("image/animations/Cats/balaluga/balaluga1.png"), pygame.image.load("image/animations/Cats/balaluga/balaluga2.png"), pygame.image.load("image/animations/Cats/balaluga/balaluga3.png"), pygame.image.load("image/animations/Cats/balaluga/balaluga2.png")]




##______________________________________________________________________________
##          Enemys
##______________________________________________________________________________
##          red_rhino

nosorog_animations_move = [pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino1.png"), pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino2.png"), pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino3.png"), pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino2.png")]
nosorog_animations_attack = [pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino1_attack.png"), pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino2_attack.png"), pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino3_attack.png"), pygame.image.load("image/animations/Enemy/Red_rhino/red_rhino2_attack.png")]

red_rhino_animations = {"move": nosorog_animations_move,
                        "attack": nosorog_animations_attack}
##         DICT
