import pygame
import os
from maps import generation_map


def create_pol(boxes):
    """создание объекта пола и удаление объекта коробки"""
    pol = Pol()
    pol.rect.x = boxes.rect.x
    pol.rect.y = boxes.rect.y
    boxes.kill()


def get_walls():
    walls = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "CС":
                wall = Wall(wall_sprite)
                wall.rect.x = x * cell_cize + board.left_start
                wall.rect.y = y * cell_cize + board.top_start
                walls.append(wall)
    return walls


def get_boxes():
    boxes = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "KК":
                box = Box(box_sprite)
                box.rect.x = x * cell_cize + board.left_start
                box.rect.y = y * cell_cize + board.top_start
                boxes.append(box)
    return boxes


def get_pols():
    pols = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in ".@ВB":
                pol = Pol(box_sprite)
                pol.rect.x = x * cell_cize + board.left_start
                pol.rect.y = y * cell_cize + board.top_start
                pols.append(pol)
    return pols


def get_doors():
    doors = []
    for y in range(len(board.field)):
        for x in range(len(board.field[0])):
            if board.field[y][x] in "Д":
                door = Door(box_sprite)
                door.rect.x = x * cell_cize + board.left_start
                door.rect.y = y * cell_cize + board.top_start
                doors.append(door)
    return doors


def load_image(name, png=False, obrezanie_fon=False):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if obrezanie_fon:  # убрать фон
        del_color = image.get_at((0, 0))
        image.set_colorkey(del_color)
    if not png:
        image = image.convert()  # не png форматы
    else:
        image = image.convert_alpha()  # png
    return image


class Board:
    def __init__(self, width, height, cell_cize):
        self.width = width
        self.height = height

        self.left_start = 65
        self.top_start = 65
        self.cell_size = cell_cize

        self.field = generation_map()
        self.add_wall()

    def add_wall(self):
        max_len = max(map(lambda x: len(x), self.field)) + 2
        for i in range(len(self.field)):
            self.field[i] = [' '] + self.field[i] + [' ']
            while len(self.field[i]) != max_len:
                self.field[i].append(' ')

        spaces = [" " for _ in range(len(self.field[0]))]
        self.field.insert(0, spaces)
        self.field.extend([spaces])

        for y in range(len(self.field)):
            for x in range(len(self.field[0])):
                if self.field[y][x] != ' ' and self.field[y][x] != "С":
                    for x_n in range(x - 1, x + 2):
                        for y_n in range(y - 1, y + 2):
                            if 0 <= x_n < len(self.field[0]) and 0 <= y_n < len(self.field) and not (
                                    x == x_n or y == y_n) and self.field[y_n][x_n] == ' ':
                                self.field[y_n][x_n] = 'С'

    def return_heroes_cords(self):
        for y_n in range(len(self.field)):
            for x_n in range(len(self.field[y_n])):
                if self.field[y_n][x_n] == "@":
                    return x_n, y_n


class Heroes(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, heroes_sprite)
        self.image = load_image(name='heroes.png', png=True, obrezanie_fon=False)
        self.image = pygame.transform.scale(self.image, (cell_cize * 1.5, cell_cize * 1.5))
        self.mask = pygame.mask.from_surface(self.image)
        self.image_left = pygame.transform.flip(surface=self.image, flip_x=True, flip_y=False)
        self.image_right = self.image

        self.sword = "меч"
        self.spear = "копье"
        self.bow = "лук"
        self.weapon = self.sword

        self.rect = self.image.get_rect()
        x_n, y_n = board.return_heroes_cords()
        self.rect.x = x_n * (cell_cize) - 20 + cell_cize
        self.rect.y = y_n * (cell_cize) + cell_cize - 33

    def move(self, event):
        x_her, y_her = board.return_heroes_cords()
        speed = board.cell_size

        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rect.x += speed
            self.image = self.image_left
            if board.field[y_her][x_her + 1] in "KКСC": # добавить Д
                self.rect.x -= speed
                return
            board.field[y_her][x_her] = '.'
            board.field[y_her][x_her + 1] = "@"

            camera.update(heroes, 'x')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rect.x -= speed
            self.image = self.image_right
            if board.field[y_her][x_her - 1] in "KКСC": # добавить Д
                self.rect.x += speed
                return
            board.field[y_her][x_her] = '.'
            board.field[y_her][x_her - 1] = "@"

            camera.update(heroes, 'x')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rect.y -= speed
            if board.field[y_her - 1][x_her] in "KКСC": # добавить Д
                self.rect.y += speed
                return
            board.field[y_her - 1][x_her] = "@"
            board.field[y_her][x_her] = "."

            camera.update(heroes, 'y')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rect.y += speed
            if board.field[y_her + 1][x_her] in "KКСC": # добавить Д
                self.rect.y -= speed
                return
            board.field[y_her + 1][x_her] = "@"
            board.field[y_her][x_her] = "."

            camera.update(heroes, 'y')
            for elem in all_sprite:
                camera.apply(elem)

    def del_box(self, elem, DISTANCE):
        """
        функция заменяет в поле доски коробки на пустоту путем удаления спрайта коробки и создания спрайта пола
        значения y(32, 33, 98) и x(20, 45, 85) получены путем вычисления разниц координат спрайтов
        """
        delta_y = abs(self.rect.y - elem.rect.y)
        delta_x = abs(self.rect.x - elem.rect.x)
        x_her, y_her = board.return_heroes_cords()
        # print(delta_x, delta_y)

        if delta_y == 32 and delta_x == 85:
            if heroes.weapon == heroes.sword:
                if board.field[y_her - 1][x_her + 1] in "KК":
                    board.field[y_her - 1][x_her + 1] = '.'
                if board.field[y_her][x_her + 1] in "KК":
                    board.field[y_her][x_her + 1] = '.'
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y - elem.rect.y == board.cell_size or \
                            boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or \
                            elem.rect.x - boxes.rect.x == board.cell_size and boxes.rect.y == elem.rect.y:
                        create_pol(boxes)
            elif heroes.weapon == heroes.spear:
                if board.field[y_her][x_her + 1] in "KК" or board.field[y_her - 1][x_her] in "KК":
                    return
                else:
                    board.field[y_her - 1][x_her + 1] = '.'
                    for boxes in box_sprite:
                        if elem.rect.x == boxes.rect.x and elem.rect.y == boxes.rect.y:
                            create_pol(boxes)
                            break

        elif delta_y == 33 and delta_x == 85:
            if heroes.weapon == heroes.sword:
                if board.field[y_her - 1][x_her + 1] in "KК":
                    board.field[y_her - 1][x_her + 1] = '.'
                if board.field[y_her][x_her + 1] in "KК":
                    board.field[y_her][x_her + 1] = '.'
                if board.field[y_her + 1][x_her + 1] in "KК":
                    board.field[y_her + 1][x_her + 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y - elem.rect.y == board.cell_size or \
                            boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or boxes.rect.x == \
                            elem.rect.x and elem.rect.y - boxes.rect.y == board.cell_size:
                        create_pol(boxes)
            elif heroes.weapon == heroes.spear:
                if board.field[y_her][x_her + 1] in "KК":
                    board.field[y_her][x_her + 1] = '.'
                    for boxes in box_sprite:
                        if elem.rect.x == boxes.rect.x and elem.rect.y == boxes.rect.y:
                            create_pol(boxes)
                            break


        elif delta_y == 98 and delta_x == 85:
            if heroes.weapon == self.sword:
                if board.field[y_her][x_her + 1] in "КK":
                    board.field[y_her][x_her + 1] = '.'
                if board.field[y_her + 1][x_her + 1] in "КK":
                    board.field[y_her + 1][x_her + 1] = '.'
                if board.field[y_her + 1][x_her] in "КK":
                    board.field[y_her + 1][x_her] = '.'

                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and elem.rect.y - boxes.rect.y == board.cell_size or \
                            boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or \
                            elem.rect.x - boxes.rect.x == board.cell_size and boxes.rect.y - elem.rect.y == 0:
                        create_pol(boxes)
            elif heroes.weapon == self.spear:
                if board.field[y_her + 1][x_her] in "КK" or board.field[y_her][x_her + 1] in "KК":
                    return
                else:
                    board.field[y_her + 1][x_her + 1] = '.'
                    for boxes in box_sprite:
                        if elem.rect.x == boxes.rect.x and elem.rect.y == boxes.rect.y:
                            create_pol(boxes)
                            break

        elif delta_x == 20 and delta_y == 32:
            if self.weapon == self.sword:
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                if board.field[y_her - 1][x_her - 1] in "KК":
                    board.field[y_her - 1][x_her - 1] = '.'
                if board.field[y_her - 1][x_her + 1] in "KК":
                    board.field[y_her - 1][x_her + 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or \
                            abs(boxes.rect.x - elem.rect.x) == board.cell_size and boxes.rect.y == elem.rect.y:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                    for boxes in box_sprite:
                        if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y:
                            create_pol(boxes)
                            break

        elif delta_x == 20 and delta_y == 98:
            if heroes.weapon == heroes.sword:
                if board.field[y_her + 1][x_her] in "KК":
                    board.field[y_her + 1][x_her] = '.'
                if board.field[y_her + 1][x_her - 1] in "KК":
                    board.field[y_her + 1][x_her - 1] = '.'
                if board.field[y_her + 1][x_her + 1] in "KК":
                    board.field[y_her + 1][x_her + 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or \
                            abs(boxes.rect.x - elem.rect.x) == board.cell_size and boxes.rect.y == elem.rect.y:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                if board.field[y_her + 1][x_her] in "KК":
                    board.field[y_her + 1][x_her] = '.'
                    for boxes in box_sprite:
                        if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y:
                            create_pol(boxes)
                            break

        elif delta_x == 45 and delta_y == 98:
            if self.weapon == self.sword:
                if board.field[y_her + 1][x_her - 1] in "KК":
                    board.field[y_her + 1][x_her - 1] = '.'
                if board.field[y_her][x_her - 1] in "KК":
                    board.field[y_her][x_her - 1] = '.'
                if board.field[y_her + 1][x_her] in "KК":
                    board.field[y_her + 1][x_her] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or \
                            boxes.rect.x - elem.rect.x == board.cell_size and boxes.rect.y == elem.rect.y or \
                            boxes.rect.x == elem.rect.x and elem.rect.y - boxes.rect.y == board.cell_size:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                if board.field[y_her][x_her - 1] in "KК" or board.field[y_her + 1][x_her] in "KК":
                    return
                else:
                    board.field[y_her + 1][x_her - 1] = '.'
                    for boxes in box_sprite:
                        if elem.rect.x == boxes.rect.x and elem.rect.y == boxes.rect.y:
                            create_pol(boxes)
                            break

        elif delta_x == 45 and delta_y == 33:
            if self.weapon == self.sword:
                if board.field[y_her - 1][x_her - 1] in "KК":
                    board.field[y_her - 1][x_her - 1] = '.'
                if board.field[y_her][x_her - 1] in "KК":
                    board.field[y_her][x_her - 1] = '.'
                if board.field[y_her + 1][x_her - 1] in "KК":
                    board.field[y_her + 1][x_her - 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y - elem.rect.y == board.cell_size or \
                            boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or boxes.rect.x == elem.rect.x \
                            and elem.rect.y - boxes.rect.y == board.cell_size:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                board.field[y_her][x_her - 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y:
                        create_pol(boxes)
                        break

        elif delta_x == 45 and delta_y == 32:
            if self.weapon == self.sword:
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                if board.field[y_her][x_her - 1] in "KК":
                    board.field[y_her][x_her - 1] = '.'
                if board.field[y_her - 1][x_her - 1] in "KК":
                    board.field[y_her - 1][x_her - 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x == elem.rect.x and boxes.rect.y == elem.rect.y or \
                            boxes.rect.y == elem.rect.y and boxes.rect.x - elem.rect.x == board.cell_size or \
                            boxes.rect.x == elem.rect.x and boxes.rect.y - elem.rect.y == board.cell_size:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                if board.field[y_her][x_her - 1] in "KК" or board.field[y_her - 1][x_her] in "KК":
                    return
                else:
                    board.field[y_her - 1][x_her - 1] = '.'
                    for boxes in box_sprite:
                        if elem.rect.x == boxes.rect.x and elem.rect.y == boxes.rect.y:
                            create_pol(boxes)
                            break

    def left_box_attack(self, DISTANCE, *args):
        """
        проверка корректности атаки коробок, когда герой находится левее коробки
        атака совершается в случае правильности логики
        """
        for elem in all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x + 20 > elem.rect.x or abs(elem.rect.x - self.rect.x) > board.cell_size + 20 + DISTANCE:
                    return
                if elem.rect.y <= self.rect.y:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size - 33 + DISTANCE):
                        return
                else:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size + 33 + DISTANCE):
                        return
                self.del_box(elem, DISTANCE)

    def right_box_attack(self, DISTANCE, *args):
        """
        проверка корректности атаки коробок, когда герой находится правее коробки
        атака совершается в случае правильности логики
        """
        for elem in all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x + 20 < elem.rect.x or abs(elem.rect.x - self.rect.x) > board.cell_size - 20 + DISTANCE:
                    return
                if elem.rect.y <= self.rect.y:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size - 33 + DISTANCE):
                        return
                else:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size + 33 + DISTANCE):
                        return
                self.del_box(elem, DISTANCE)

    def attack(self, *args):
        DISTANCE = 65  # коээфицент дальности
        if self.image == self.image_left:  # герой находится слева
            self.left_box_attack(DISTANCE, *args)
        else:  # герой находится справа
            self.right_box_attack(DISTANCE, *args)


class Box(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, box_sprite)
        self.image = load_image(name='box.png', png=True, obrezanie_fon=False)
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Wall(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, wall_sprite)
        self.image = load_image(name='wall.png', png=True, obrezanie_fon=False)
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Pol(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite)
        self.image = load_image(name='pol.png', png=True, obrezanie_fon=False)
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Door(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, door_sprite)
        self.image = load_image(name='door.png', png=True, obrezanie_fon=False)
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj_sprite):
        obj_sprite.rect.x += self.dx
        obj_sprite.rect.y += self.dy

    def update(self, tracker_obj, check):
        self.dx = 0
        self.dy = 0
        y_n = 2
        x_n = 2
        if check == 'x':
            self.dx = -(tracker_obj.rect.x + tracker_obj.rect.w // x_n - width // x_n)
        elif check == 'y':
            self.dy = -(tracker_obj.rect.y + tracker_obj.rect.h // y_n - height // y_n)


n = 10
cell_cize = 65
pygame.init()
pygame.key.set_repeat(200, 70)
clock = pygame.time.Clock()
width = height = 975
pygame.display.set_caption('room')
screen = pygame.display.set_mode((width, height))

all_sprite = pygame.sprite.Group()
heroes_sprite = pygame.sprite.Group()
wall_sprite = pygame.sprite.Group()
box_sprite = pygame.sprite.Group()
door_sprite = pygame.sprite.Group()

board = Board(n, n, cell_cize)

get_walls()
get_pols()
get_doors()
get_boxes()

heroes = Heroes(heroes_sprite)
camera = Camera()
running = True

camera.update(heroes, 'y')
for elem in all_sprite:
    camera.apply(elem)

camera.update(heroes, 'x')
for elem in all_sprite:
    camera.apply(elem)

fon = load_image(name='fon1.png', png=True, obrezanie_fon=False)
fon = pygame.transform.scale(fon, (1000, 1000))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            heroes.move(event)
        if event.type == pygame.MOUSEBUTTONUP:
            heroes.attack(event)
    screen.fill((0, 0, 0))
    screen.blit(fon, (0, 0))
    door_sprite.draw(screen)
    all_sprite.draw(screen)
    heroes_sprite.draw(screen)
    clock.tick(30)
    pygame.event.pump()
    pygame.display.flip()
