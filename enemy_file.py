import pygame


def get_enemy(board, all_sprite, enemy_sprite, enemy_image, cell_cize, heroes, door_sprite):
    enemyes = []
    x_her, y_her = board.return_heroes_cords()
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "X":
                board.field[y][x] = 'E'
                enemy = Enemy(all_sprite, enemy_sprite, enemy_image, cell_cize, heroes, y, x, board, door_sprite)
                enemy.rect.x = heroes.rect.x + (x - x_her) * cell_cize - 7 + cell_cize // 2
                enemy.rect.y = heroes.rect.y + (y - y_her) * cell_cize + 6 + cell_cize // 2
                enemyes.append(enemy)
    return enemyes


class Enemy(pygame.sprite.Sprite):
    def __init__(self, all_sprite, enemy_sprite, enemy_image, cell_cize, heroes, y, x, board, door_sprite):
        super().__init__(all_sprite, enemy_sprite)
        self.image = enemy_image
        self.image = pygame.transform.scale(self.image, (cell_cize - 10, cell_cize - 10))
        self.rect = self.image.get_rect()
        self.hp = 100
        self.level = 0
        self.heroes = heroes
        self.y = y
        self.x = x
        self.board = board
        self.cell_cize = cell_cize
        self.door_sprite = door_sprite
        self.all_sprite = all_sprite
        self.enemy_sprite = enemy_sprite

        self.clock_cool_down = pygame.time.Clock()
        self.cur_time_cool_down = 0
        self.limit_time_cool_down = 0.3

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
        x_her, y_her = self.board.return_heroes_cords()
        if ((x_her - 1) // 10) % 2 != 0 and ((y_her - 1) // 10) % 2 != 0:
            return

        road = self.check_paths()
        if road is not None:
            if self.check_cooldown():
                if len(road) < 2:
                    return
                road = road[1:]
                x_en, y_en = road[0][0], road[0][1]

                if (x_en, y_en) == self.board.return_heroes_cords():
                    return

                for elem in self.enemy_sprite:
                    if elem != self and elem.y == y_en and elem.x == x_en:
                        return

                if self.board.field[self.y][self.x] == 'E':
                    self.board.field[self.y][self.x] = '.'

                if x_en > self.x and self.board.field[self.y][self.x] not in 'СEKСK':
                    if self.board.field[y_en][x_en] in 'CEKСK':
                        return

                    self.x += 1
                    self.rect.x += self.cell_cize
                    self.board.field[self.y][self.x] = 'E'
                    return

                elif x_en < self.x and self.board.field[self.y][self.x] not in 'CEKСK':
                    if self.board.field[y_en][x_en] in 'CEKСK':
                        return
                    self.x -= 1
                    self.rect.x -= self.cell_cize
                    self.board.field[self.y][self.x] = 'E'
                    return

                elif y_en > self.y and self.board.field[self.y][self.x] not in 'CEKСK':
                    if self.board.field[y_en][x_en] in 'CEKСK':
                        return
                    self.y += 1
                    self.rect.y += self.cell_cize
                    self.board.field[self.y][self.x] = 'E'
                    return

                elif y_en < self.y and self.board.field[self.y][self.x] not in 'CEKСK':
                    if self.board.field[y_en][x_en] in 'CEKСK':
                        return
                    self.y -= 1
                    self.rect.y -= self.cell_cize
                    self.board.field[self.y][self.x] = 'E'
                    return
                if self.board.field[self.y][self.x] not in 'СCKКЛД':
                    self.board.field[self.y][self.x] = 'E'

    def check_cooldown(self):
        self.clock_cool_down.tick()
        self.cur_time_cool_down += self.clock_cool_down.get_time() / 1000
        if self.cur_time_cool_down > self.limit_time_cool_down:
            self.cur_time_cool_down = 0
            return True
        return False
