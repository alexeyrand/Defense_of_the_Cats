import pygame
import random
import time
from animations import *
from setting import *
pygame.init()
clock = pygame.time.Clock()


class Unit:
    def __init__(self, name, hp, damage, speed, attack_speed, attack_range, image, animations):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.animations = animations
        self.animCount = 0
        self.animAtack = 0

    def attack(self, sc):
        sc.blit(self.animations["attack"][self.animAtack // (self.attack_speed // len(self.animations["attack"]))], (self.x, self.y))
        self.animAtack += 1

    def stay(self, sc):
        if self.animAtack < self.attack_speed:
            self.attack(sc)
        elif  300 > self.animAtack >= self.attack_speed:
            sc.blit(self.animations["move"][0], (self.x, self.y))
            self.animAtack += 1
        elif self.animAtack >= 300:
            self.animAtack = 0

class Cat(pygame.sprite.Sprite, Unit):
    def __init__(self, name, hp, damage, speed, attack_speed, attack_range, image, animations):
        pygame.sprite.Sprite.__init__(self)
        Unit.__init__(self, name, hp, damage, speed, attack_speed, attack_range, image, animations)
        self.x = 1100
        self.y = random.choice([630, 633, 636]) - self.rect.bottom


    def update(self, sc):
        if self.x < W:
            self.x -= self.speed
            if self.hp > 0:
                if self.animCount + 1 >= FPS:
                    self.animCount = 0
                sc.blit(self.animations["move"][self.animCount // (FPS // len(self.animations["move"]))], (self.x, self.y))
                self.animCount += 1
            else:
                self.kill()


class Enemy(pygame.sprite.Sprite, Unit):
    def __init__(self, name, hp, damage, speed, attack_speed, attack_range, image, animations):
        pygame.sprite.Sprite.__init__(self)
        Unit.__init__(self, name, hp, damage, speed, attack_speed, attack_range, image, animations)
        self.x = 100
        self.y = random.choice([630, 633, 636]) - self.rect.bottom

    def update(self, sc):
        if self.x < W:
            self.x += self.speed
            if self.hp > 0:
                if self.animCount + 1 >= FPS:
                    self.animCount = 0
                sc.blit(self.animations["move"][self.animCount // (FPS // len(self.animations["move"]))], (self.x, self.y))
                self.animCount += 1
            else:
                self.kill()


class Level:
    def play(self, time, enemys, level):
        if level == 1:
            if time == 100:
                enemys.add(Enemy("nos", 1000, 10, 0.5, 60, 55, "image/nos.png", red_rhino_animations))
            if time == 500:
                enemys.add(Enemy("nos", 1000, 10, 0.5, 60, 55, "image/nos.png", red_rhino_animations))

        if level == 2:
            if time == 100:
                enemys.add(Enemy("capla", 1000, 10, 1, "image/capla.png"))
            if time == 300:
                enemys.add(Enemy("capla", 1000, 10, 1, "image/capla.png"))
