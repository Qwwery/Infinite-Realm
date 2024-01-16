from random import randint
import pygame
import os


def upp_level_hero(self, enemy_level):
    musuk = pygame.mixer.Sound(os.path.join('assets', 'music', 'level.wav'))
    xp = enemy_level * randint(5, 13)
    self.xp += xp
    if self.xp >= self.level * 100:
        musuk.play(0)
        self.xp -= (self.level * 100)
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.damage_spear += 5
        self.damage_sword += 5
