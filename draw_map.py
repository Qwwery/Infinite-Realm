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
        self.field.insert(0, spaces.copy())
        self.field.extend([spaces.copy()])

        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                if self.field[y][x] != ' ' and self.field[y][x] != "С":
                    if x - 1 >= 0 and self.field[y][x - 1] == ' ':
                        self.field[y][x - 1] = 'С'
                    if x - 1 >= 0 and y - 1 >= 0 and self.field[y - 1][x - 1] == ' ':
                        self.field[y - 1][x - 1] = 'С'
                    if y - 1 >= 0 and self.field[y - 1][x] == ' ':
                        self.field[y - 1][x] = 'С'
                    if y - 1 >= 0 and x + 1 < len(self.field[0]) and self.field[y - 1][x + 1] == ' ':
                        self.field[y - 1][x + 1] = 'С'
                    if x + 1 < len(self.field[0]) and self.field[y][x + 1] == ' ':
                        self.field[y][x + 1] = 'С'
                    if y + 1 < len(self.field) and self.field[y + 1][x] == ' ':
                        self.field[y + 1][x] = 'С'
                    if y + 1 < len(self.field) and x - 1 >= 0 and self.field[y + 1][x - 1] == ' ':
                        self.field[y + 1][x - 1] = 'С'
                    if y + 1 < len(self.field) and x + 1 < len(self.field[0]) and self.field[y + 1][x + 1] == ' ':
                        self.field[y + 1][x + 1] = 'С'

    def return_heroes_cords(self):
        for y_n in range(len(self.field)):
            for x_n in range(len(self.field[y_n])):
                if self.field[y_n][x_n] == "@":
                    return x_n, y_n


class Heroes(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, heroes_sprite)
        self.image = heroes_image
        self.image = pygame.transform.scale(self.image, (cell_cize * 1.5, cell_cize * 1.5))
        self.mask = pygame.mask.from_surface(self.image)
        self.image_left = pygame.transform.flip(surface=self.image, flip_x=True, flip_y=False)
        self.image_right = self.image

        self.sword = "меч"
        self.spear = "копье"
        self.bow = "лук"
        self.weapon = self.spear

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
            if board.field[y_her][x_her + 1] in "KКСC":  # добавить Д
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
            if board.field[y_her][x_her - 1] in "KКСC":  # добавить Д
                self.rect.x += speed
                return
            board.field[y_her][x_her] = '.'
            board.field[y_her][x_her - 1] = "@"

            camera.update(heroes, 'x')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rect.y -= speed
            if board.field[y_her - 1][x_her] in "KКСC":  # добавить Д
                self.rect.y += speed
                return
            board.field[y_her - 1][x_her] = "@"
            board.field[y_her][x_her] = "."

            camera.update(heroes, 'y')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rect.y += speed
            if board.field[y_her + 1][x_her] in "KКСC":  # добавить Д
                self.rect.y -= speed
                return
            board.field[y_her + 1][x_her] = "@"
            board.field[y_her][x_her] = "."

            camera.update(heroes, 'y')
            for elem in all_sprite:
                camera.apply(elem)

    def del_box(self, elem, DISTANCE, delta_x, delta_y):
        """
        функция заменяет в поле доски коробки на пустоту путем удаления спрайта коробки и создания спрайта пола
        значения y(32, 33, 98) и x(20, 45, 85) получены путем вычисления разниц координат спрайтов
        """
        x_her, y_her = board.return_heroes_cords()
        print(delta_x, delta_y)
        # print(boxes.rect.x - self.rect.x, boxes.rect.y - self.rect.y)

        if self.weapon == self.spear and delta_x == -45 and delta_y == 33:  # копье лево одна клетка
            if board.field[y_her][x_her - 1] in "KК":
                board.field[y_her][x_her - 1] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x - self.rect.x == -45 and boxes.rect.y - self.rect.y == 33:
                        create_pol(boxes)
        elif self.weapon == self.spear and delta_x == 85 and delta_y == 33:  # копье право одна клетка
            if board.field[y_her][x_her + 1] in "KК":
                board.field[y_her][x_her + 1] = '.'
            for boxes in box_sprite:
                if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 33:
                    create_pol(boxes)
        elif self.weapon == self.spear and delta_x == 20 and delta_y == 98:  # копье низ одна клетка
            if board.field[y_her + 1][x_her] in "KК":
                board.field[y_her + 1][x_her] = '.'
            for boxes in box_sprite:
                if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == 98:
                    create_pol(boxes)
        elif self.weapon == self.spear and delta_x == 20 and delta_y == -32:  # копье низ одна клетка
            if board.field[y_her - 1][x_her] in "KК":
                board.field[y_her - 1][x_her] = '.'
                for boxes in box_sprite:
                    if boxes.rect.x - self.rect.x == 20 and boxes.rect.y - self.rect.y == -32:
                        create_pol(boxes)

        if delta_x > 20 and delta_y < 0:  # право верх
            if heroes.weapon == heroes.sword:
                if board.field[y_her - 1][x_her + 1] in "KК":
                    board.field[y_her - 1][x_her + 1] = '.'
                if board.field[y_her][x_her + 1] in "KК":
                    board.field[y_her][x_her + 1] = '.'
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32:
                        create_pol(boxes)
            elif heroes.weapon == heroes.spear:
                if board.field[y_her - 1][x_her] != '.' or board.field[y_her][x_her + 1] != '.':
                    return
                else:
                    if board.field[y_her - 1][x_her + 1] in "КK":
                        board.field[y_her - 1][x_her + 1] = '.'
                        for boxes in box_sprite:
                            if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == -32:
                                create_pol(boxes)

        elif delta_x > 0 and delta_y == 33:  # право
            if heroes.weapon == heroes.sword:
                if board.field[y_her - 1][x_her + 1] in "KК":
                    board.field[y_her - 1][x_her + 1] = '.'
                if board.field[y_her][x_her + 1] in "KК":
                    board.field[y_her][x_her + 1] = '.'
                if board.field[y_her + 1][x_her + 1] in "KК":
                    board.field[y_her + 1][x_her + 1] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes)
            elif heroes.weapon == heroes.spear:
                pass


        elif delta_x > 20 and delta_y > 0:  # право низ
            if heroes.weapon == self.sword:
                if board.field[y_her][x_her + 1] in "КK":
                    board.field[y_her][x_her + 1] = '.'
                if board.field[y_her + 1][x_her + 1] in "КK":
                    board.field[y_her + 1][x_her + 1] = '.'
                if board.field[y_her + 1][x_her] in "КK":
                    board.field[y_her + 1][x_her] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes)
            elif heroes.weapon == self.spear:
                if board.field[y_her][x_her + 1] != '.' or board.field[y_her + 1][x_her] != '.':
                    return
                else:
                    if board.field[y_her + 1][x_her + 1] in "КK":
                        board.field[y_her + 1][x_her + 1] = '.'
                        for boxes in box_sprite:
                            if boxes.rect.x - self.rect.x == 85 and boxes.rect.y - self.rect.y == 98:
                                create_pol(boxes)



        elif delta_x == 20 and delta_y < 0:  # верх
            if self.weapon == self.sword:
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                if board.field[y_her - 1][x_her - 1] in "KК":
                    board.field[y_her - 1][x_her - 1] = '.'
                if board.field[y_her - 1][x_her + 1] in "KК":
                    board.field[y_her - 1][x_her + 1] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == 32:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                pass

        elif delta_x == 20 and delta_y > 0:  # низ
            if heroes.weapon == heroes.sword:
                if board.field[y_her + 1][x_her] in "KК":
                    board.field[y_her + 1][x_her] = '.'
                if board.field[y_her + 1][x_her - 1] in "KК":
                    board.field[y_her + 1][x_her - 1] = '.'
                if board.field[y_her + 1][x_her + 1] in "KК":
                    board.field[y_her + 1][x_her + 1] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -85 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                pass

        elif delta_x < 0 and delta_y > 33:  # лево низ
            if self.weapon == self.sword:
                if board.field[y_her + 1][x_her - 1] in "KК":
                    board.field[y_her + 1][x_her - 1] = '.'
                if board.field[y_her][x_her - 1] in "KК":
                    board.field[y_her][x_her - 1] = '.'
                if board.field[y_her + 1][x_her] in "KК":
                    board.field[y_her + 1][x_her] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                if board.field[y_her][x_her - 1] != '.' or board.field[y_her + 1][x_her] != '.':
                    return
                else:
                    if board.field[y_her + 1][x_her - 1] in "KК":
                        board.field[y_her + 1][x_her - 1] = '.'
                        for boxes in box_sprite:
                            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                                create_pol(boxes)

        elif delta_x < 0 and delta_y == 33:  # лево
            if self.weapon == self.sword:
                if board.field[y_her - 1][x_her - 1] in "KК":
                    board.field[y_her - 1][x_her - 1] = '.'
                if board.field[y_her][x_her - 1] in "KК":
                    board.field[y_her][x_her - 1] = '.'
                if board.field[y_her + 1][x_her - 1] in "KК":
                    board.field[y_her + 1][x_her - 1] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -98:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                pass

        elif delta_x < 0 and delta_y < 0:  # лево верх
            if self.weapon == self.sword:
                if board.field[y_her - 1][x_her] in "KК":
                    board.field[y_her - 1][x_her] = '.'
                if board.field[y_her][x_her - 1] in "KК":
                    board.field[y_her][x_her - 1] = '.'
                if board.field[y_her - 1][x_her - 1] in "KК":
                    board.field[y_her - 1][x_her - 1] = '.'

                for boxes in box_sprite:
                    if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == -20 and self.rect.y - boxes.rect.y == 32 or \
                            self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == -33:
                        create_pol(boxes)
            elif self.weapon == self.spear:
                if board.field[y_her][x_her - 1] != '.' or board.field[y_her - 1][x_her] != '.':
                    return
                else:
                    if board.field[y_her - 1][x_her - 1] in "КK":
                        board.field[y_her - 1][x_her - 1] = '.'
                        for boxes in box_sprite:
                            if self.rect.x - boxes.rect.x == 45 and self.rect.y - boxes.rect.y == 32:
                                create_pol(boxes)

    def left_box_attack(self, DISTANCE, *args):
        """
        проверка корректности атаки коробок, когда герой находится левее коробки
        атака совершается в случае правильности логики
        """
        for elem in all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x - 20 <= elem.rect.x:
                    self.del_box(elem, DISTANCE, elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def right_box_attack(self, DISTANCE, *args):
        """
        проверка корректности атаки коробок, когда герой находится правее коробки
        атака совершается в случае правильности логики
        """
        for elem in all_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x + 20 >= elem.rect.x:
                    self.del_box(elem, DISTANCE, elem.rect.x - self.rect.x, elem.rect.y - self.rect.y)

    def attack(self, *args):
        DISTANCE = 65  # коээфицент дальности
        if self.image == self.image_left:  # герой находится слева
            self.left_box_attack(DISTANCE, *args)
        else:  # герой находится справа
            self.right_box_attack(DISTANCE, *args)


class Box(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, box_sprite)
        self.image = box_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Wall(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, wall_sprite)
        self.image = wall_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Pol(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite)
        self.image = pol_image
        self.image = pygame.transform.scale(self.image, (cell_cize, cell_cize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = board.left_start
        self.rect.y = board.top_start


class Door(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, door_sprite)
        self.image = door_image
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
width, height = 975, 975
pygame.display.set_caption('room')
screen = pygame.display.set_mode((width, height))

wall_image = load_image(name='wall.png', png=True, obrezanie_fon=False)
pol_image = load_image(name='pol.png', png=True, obrezanie_fon=False)
door_image = load_image(name='door.png', png=True, obrezanie_fon=False)
box_image = load_image(name='box.png', png=True, obrezanie_fon=False)
heroes_image = load_image(name='heroes.png', png=True, obrezanie_fon=False)

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

fon = load_image(name='fon3.png', png=True, obrezanie_fon=False)
fon = pygame.transform.scale(fon, (1000, 1000))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            heroes.move(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            heroes.attack(event)
    screen.fill((0, 0, 0))
    screen.blit(fon, (0, 0))
    door_sprite.draw(screen)
    all_sprite.draw(screen)
    heroes_sprite.draw(screen)
    clock.tick(30)
    pygame.event.pump()
    pygame.display.flip()
