from random import randint


def upp_level_hero(self, enemy_level):
    xp = enemy_level * randint(5, 13)
    self.xp += xp
    if self.xp >= self.level * 100:
        self.xp -= (self.level * 100)
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.damage_spear += 5
        self.damage_sword += 5
