import pygame
import random
import time
import math
from animations import *
from setting import *

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_mode((W, H))
wings = []

class Wings:
    def __init__(self, x, y, image, image_cat):
        self.x = x
        self.y = y
        self.animWings = 0
        self.image = pygame.image.load(image).convert_alpha()
        self.image_cat = image_cat
        self.image_cat = pygame.transform.rotate(self.image_cat, -35)
        self.const = self.y

    def drow(self, sc):
        if self.animWings < 45:
            sc.blit(self.image_cat, (self.x, self.y))
            self.y = self.const - 35 * abs(math.sin((0.1 * ((3.14 * (self.y + 94 * self.animWings)) // 180)))**(5/2))
            self.x += 2.5
            self.animWings += 1
        else:
            if self.y != 0:
                sc.blit(self.image, (self.x, self.y))
                self.y -= 3
            else:
                self.kill()


class Unit:
    def __init__(self, name, hp, damage, speed, attack_speed, attack_delay, attack_range, image, animations):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.attack_speed = attack_speed
        self.attack_delay = attack_delay
        self.attack_range = attack_range
        self.image = pygame.image.load(image).convert_alpha()
        self.shadow = pygame.image.load("image/shadow.png").convert_alpha()
        self.shadow.set_alpha(128)
        self.rect = self.image.get_rect()
        self.animations = animations
        self.animCount = 0
        self.animAtack = 0

class Cat(pygame.sprite.Sprite, Unit):
    def __init__(self, name, hp, damage, speed, attack_speed, attack_delay, attack_range, image, animations):
        pygame.sprite.Sprite.__init__(self)
        Unit.__init__(self, name, hp, damage, speed, attack_speed, attack_delay, attack_range, image, animations)
        self.x = 1100
        self.y = random.choice([630, 633, 636]) - self.rect.bottom

    def update(self, sc):
        if self.x < W:
            self.x -= self.speed
            if self.hp > 0:
                if self.animCount + 1 >= FPS:
                    self.animCount = 0
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["move"][self.animCount // (FPS // len(self.animations["move"]))], (self.x, self.y))
                self.animCount += 1
            else:
                self.kill()

    def attack(self, sc, enemys, bases):
        if len(enemys) != 0:
            aim = [enemy for enemy in enemys if enemy.x == min(enemy.x for enemy in enemys)]
        else:
            aim = [bases[0]]
        aim[0].hp = aim[0].hp - self.damage

    def stay(self, sc, enemys, bases):
        if self.hp > 0:
            if self.animAtack < self.attack_speed:
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["attack"][self.animAtack // (self.attack_speed // len(self.animations["attack"]))], (self.x, self.y))
                self.animAtack += 1
                if self.animAtack == self.attack_speed - 1:
                    self.attack(sc, enemys, bases)
            elif  self.attack_delay > self.animAtack >= self.attack_speed:
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["move"][0], (self.x, self.y))
                self.animAtack += 1
            elif self.animAtack >= self.attack_delay:
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["move"][0], (self.x, self.y))
                self.animAtack = 0
        else:
            wings.append(Wings(self.x, self.y, "image/Wings.png", self.image))
            self.kill()

class Enemy(pygame.sprite.Sprite, Unit):
    def __init__(self, name, hp, damage, speed, attack_speed, attack_delay, attack_range, image, animations):
        pygame.sprite.Sprite.__init__(self)
        Unit.__init__(self, name, hp, damage, speed, attack_speed, attack_delay, attack_range, image, animations)
        self.x = 40
        self.y = random.choice([630, 633, 636]) - self.rect.bottom

    def update(self, sc):
        if self.x < W:
            self.x += self.speed
            if self.hp > 0:
                if self.animCount + 1 >= FPS:
                    self.animCount = 0
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["move"][self.animCount // (FPS // len(self.animations["move"]))], (self.x, self.y))
                self.animCount += 1
            else:
                self.kill()

    def attack(self, sc, enemys, bases):
        if len(enemys) != 0:
            aim = [enemy for enemy in enemys if enemy.x == min(enemy.x for enemy in enemys)]
        else:
            aim = [bases[1]]
        aim[0].hp = aim[0].hp - self.damage

    def stay(self, sc, enemys, bases):
        if self.hp > 0:
            if self.animAtack < self.attack_speed:
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["attack"][self.animAtack // ((self.attack_speed + 2) // len(self.animations["attack"]))], (self.x, self.y))
                self.animAtack += 1
                if self.animAtack == self.attack_speed - 1:
                    self.attack(sc, enemys, bases)
            elif  self.attack_delay > self.animAtack >= self.attack_speed:
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["move"][0], (self.x, self.y))
                self.animAtack += 1
            elif self.animAtack >= self.attack_delay:
                sc.blit(self.shadow, (self.x, self.y + self.rect.bottom - 10))
                sc.blit(self.animations["move"][0], (self.x, self.y))
                self.animAtack = 0
        else:
            self.kill()

class Base:
    def __init__(self, hp, image, x, y):
#        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def update(self, sc):
        sc.blit(self.image, (self.x, self.y))

class Level:
    def play(self, time, enemys, bases, level):
        if level == 1:
            if len(bases) == 0:
                bases.append(Base(1000, "image/base/enemy_tower1.png", 40, 470))
                bases.append(Base(1000, "image/base/cat_tower1.png", 1082, 470))
            if time == 100:
                enemys.add(give_enemy("Red_rhino"))
            if time == 500:
                enemys.add(give_enemy("Red_rhino"))
            if time == 500:
                enemys.add(give_enemy("Red_rhino"))

        if level == 2:
            if time == 100:
                enemys.add(Enemy("capla", 1000, 10, 1, "image/capla.png"))
            if time == 300:
                enemys.add(Enemy("capla", 1000, 10, 1, "image/capla.png"))


# Create_cats and enemys
# def __init__(self, name, hp, damage, speed, attack_speed, attack_delay, attack_range, image, animations):
def give_cat(cat_name):
    if cat_name == "Shishilan":
        return Cat("Shishilan", 1000, 100, 1.4, 120, 300, 270, "image/animations/Cats/shishilan/shishilan.png", shishilan_animations)

    if cat_name == "Base_cat":
        return Cat("Cat", 1000, 10000000, 3.4, 60,  80, 5, "image/animations/Cats/cat/cat1.png", cat_animations)

    if cat_name == "test":
        return Cat("test", 1000, 10, 0, 60,  80, 55, "image/animations/Cats/cat/cat1.png", cat_animations)

def give_enemy(enemy_name):
    if enemy_name == "Red_rhino":
        return Enemy("nos", 4000, 200, 2.5, 27, 28, 5, "image/animations/Enemy/Red_rhino/red_rhino1.png", red_rhino_animations)
