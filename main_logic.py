import pygame
import random
import time
from animations import *
pygame.init()
clock = pygame.time.Clock()


class Unit:
    def __init__(self, name, hp, dmg, speed, image, animations):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.speed = speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.animations = animations

    def update(self, sc):
        self.x += self.speed
        if self.hp > 0:
            if self.animCount + 1 >= 60:
                self.animCount = 0
                print("обнулили")
            sc.blit(self.animations[self.animCount // 15], (self.x, self.y))
            self.animCount += 1
        else:
            self.kill()


class Cat(pygame.sprite.Sprite, Unit):
    def __init__(self, name, hp, dmg, speed, image, animations):
        pygame.sprite.Sprite.__init__(self)
        Unit.__init__(self, name, hp, dmg, speed, image, animations)
        self.rect = self.image.get_rect()
        self.x = 1100
        self.y = random.choice([620, 625, 630]) - self.rect.bottom
        self.animCount = 0

    def update(self, sc):
        self.x -= self.speed
        if self.hp > 0:
            if self.animCount + 1 >= 60:
                self.animCount = 0
            sc.blit(self.animations[self.animCount // 15], (self.x, self.y))
            self.animCount += 1
        else:
            self.kill()

class Enemy(pygame.sprite.Sprite, Unit):
    def __init__(self, name, hp, dmg, speed, image, animations):
        pygame.sprite.Sprite.__init__(self)
        Unit.__init__(self, name, hp, dmg, speed, image, animations)
        self.rect = self.image.get_rect()
        self.x = 100
        self.y = random.choice([620, 625, 630]) - self.rect.bottom
        self.animCount = 0

    def update(self, sc):
        self.x += self.speed
        if self.hp > 0:
            if self.animCount + 1 >= 60:
                self.animCount = 0
                print("обнулили")
            sc.blit(self.animations[self.animCount // 15], (self.x, self.y))
            self.animCount += 1
        else:
            self.kill()


class Level:
    def play(self, time, enemys, level):
        if level == 1:
            if time == 100:
                enemys.add(Enemy("nos", 1000, 10, 0.5, "image/nos.png", nosorog_animations))
            if time == 300:
                enemys.add(Enemy("nos", 1000, 10, 0.5, "image/nos.png", nosorog_animations))

        if level == 2:
            if time == 100:
                enemys.add(Enemy("capla", 1000, 10, 1, "image/capla.png"))
            if time == 300:
                enemys.add(Enemy("capla", 1000, 10, 1, "image/capla.png"))
