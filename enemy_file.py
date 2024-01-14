import random

import pygame


def get_enemy(board, all_sprite, enemy_sprite, enemy_image, cell_cize, heroes, door_sprite, sound_ydar):
    enemyes = []
    x_her, y_her = board.return_heroes_cords()
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "X":
                board.field[y][x] = 'E'
                enemy = Enemy(all_sprite, enemy_sprite, enemy_image, cell_cize, heroes, y, x, board, door_sprite,
                              sound_ydar)
                enemy.rect.x = heroes.rect.x + (x - x_her) * cell_cize - 7 + cell_cize // 2
                enemy.rect.y = heroes.rect.y + (y - y_her) * cell_cize + 6 + cell_cize // 2
                enemyes.append(enemy)
    return enemyes


def get_feature_cell(self):
    x_her, y_her = self.board.return_heroes_cords()
    if ((x_her - 1) // 10) % 2 != 0 and ((y_her - 1) // 10) % 2 != 0:
        return False,

    road = self.check_paths()
    if road is not None:
        if self.check_cooldown_move():
            try:
                road = road[1:]
                return True, road[0][0], road[0][1]
            except IndexError:
                return False,
    return False,


def check_intersection(self, y_en, x_en):
    for elem in self.enemy_sprite:  # враг не проходит сквозь врага
        if elem != self and elem.y == y_en and elem.x == x_en:
            return False

    for elem in self.door_sprite:  # враг не может пройти через дверь
        if elem.y == y_en and elem.x == x_en:
            return False
    return True


class Enemy(pygame.sprite.Sprite):
    def __init__(self, all_sprite, enemy_sprite, enemy_image, cell_cize, heroes, y, x, board, door_sprite, sound_ydar):
        super().__init__(all_sprite, enemy_sprite)
        self.image = enemy_image
        self.image = pygame.transform.scale(self.image, (cell_cize - 10, cell_cize - 10))
        self.rect = self.image.get_rect()

        count_enemy = sum(map(lambda x: x.count('X'), board.field)) + sum(map(lambda x: x.count('E'), board.field))
        level = heroes.level

        if count_enemy == 1:
            self.level = heroes.level + random.randint(10, 15)
        elif 2 <= count_enemy <= 4:
            self.level = heroes.level + random.randint(5, 7)
        else:
            self.level = heroes.level + random.randint(-3, 3)
        while self.level <= 0:
            self.level += 1
        self.heroes = heroes

        self.hp = self.level * 10 + 100

        self.y = y
        self.x = x

        self.board = board
        self.cell_cize = cell_cize
        self.door_sprite = door_sprite
        self.all_sprite = all_sprite
        self.enemy_sprite = enemy_sprite

        self.clock_move = pygame.time.Clock()
        self.cur_time_move = 0
        self.limit_time_move = 0.42

        self.clock_attack = pygame.time.Clock()
        self.cur_time_attack = 0
        self.limit_time_attack = 1.3

        self.clock_stop = pygame.time.Clock()
        self.cur_time_stop = 0
        self.limit_time_stop = 1.7

        self.sound_ydar = sound_ydar

        self.is_stop = False

    def check_paths(self):
        start = (self.x, self.y)
        end = self.board.return_heroes_cords()
        queue = [start]
        paths = {start: [start]}
        while queue:
            x, y = queue.pop(0)
            if (x, y) == end:
                return paths[(x, y)]
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:  # Четыре направления
                nx, ny = x + dx, y + dy
                if self.board.field[ny][nx] not in 'СEКKСЕД' and (nx, ny) not in paths:
                    queue.append((nx, ny))
                    paths[(nx, ny)] = paths[(x, y)] + [(nx, ny)]
        return None

    def move(self):
        if self.is_stop and not self.check_cooldown_stop():
            return False

        check_cell = get_feature_cell(self)
        if not check_cell[0]:
            return False

        x_en, y_en = check_cell[1], check_cell[2]
        if (x_en, y_en) == self.board.return_heroes_cords():  # атака героя
            if self.check_cooldown_attack():
                self.heroes.hp -= self.level * 5
                self.sound_ydar.play(0)
            return

        if not check_intersection(self, y_en, x_en):
            return

        if self.board.field[self.y][self.x] == 'E':
            self.board.field[self.y][self.x] = '.'

        if x_en > self.x and self.board.field[self.y][self.x] not in 'СEKСK':  # право
            if self.board.field[y_en][x_en] in 'CEKСK':
                return

            self.x += 1
            self.rect.x += self.cell_cize
            self.board.field[self.y][self.x] = 'E'
            return

        elif x_en < self.x and self.board.field[self.y][self.x] not in 'CEKСK':  # лево
            if self.board.field[y_en][x_en] in 'CEKСK':
                return
            self.x -= 1
            self.rect.x -= self.cell_cize
            self.board.field[self.y][self.x] = 'E'
            return

        elif y_en > self.y and self.board.field[self.y][self.x] not in 'CEKСK':  # низ
            if self.board.field[y_en][x_en] in 'CEKСK':
                return
            self.y += 1
            self.rect.y += self.cell_cize
            self.board.field[self.y][self.x] = 'E'
            return

        elif y_en < self.y and self.board.field[self.y][self.x] not in 'CEKСK':  # верх
            if self.board.field[y_en][x_en] in 'CEKСK':
                return
            self.y -= 1
            self.rect.y -= self.cell_cize
            self.board.field[self.y][self.x] = 'E'
            return

        for elem in self.enemy_sprite:
            self.board.field[elem.y][elem.x] = 'E'

    def check_cooldown_move(self):
        self.clock_move.tick()
        self.cur_time_move += self.clock_move.get_time() / 1000
        if self.cur_time_move > self.limit_time_move:
            self.cur_time_move = 0
            return True
        return False

    def check_cooldown_attack(self):
        self.clock_attack.tick()
        self.cur_time_attack += self.clock_attack.get_time() / 1000
        if self.cur_time_attack > self.limit_time_attack:
            self.cur_time_attack = 0
            return True
        return False

    def check_cooldown_stop(self):
        self.clock_stop.tick()
        self.cur_time_stop += self.clock_stop.get_time() / 1000
        if self.cur_time_stop > self.limit_time_stop:
            self.cur_time_stop = 0
            self.is_stop = False
            return True
        return False
