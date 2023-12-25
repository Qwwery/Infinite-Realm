import pygame
import os


def get_walls():
    walls = []
    for y in range(len(board.field)):
        for x in range(len(board.field)):
            if board.field[y][x] in "CС":
                wall = Wall(wall_sprite)
                wall.rect.x = x * cell_cize + board.left_start
                wall.rect.y = y * cell_cize + board.top_start
                walls.append(wall)
    return walls


def get_boxes():
    boxes = []
    for y in range(len(board.field)):
        for x in range(len(board.field)):
            if board.field[y][x] in "KК":
                box = Box(box_sprite)
                box.rect.x = x * cell_cize + board.left_start
                box.rect.y = y * cell_cize + board.top_start
                boxes.append(box)
    return boxes


def get_pols():
    pols = []
    for y in range(len(board.field)):
        for x in range(len(board.field)):
            if board.field[y][x] in ".@ВB":
                pol = Pol(box_sprite)
                pol.rect.x = x * cell_cize + board.left_start
                pol.rect.y = y * cell_cize + board.top_start
                pols.append(pol)
    return pols


def get_doors():
    doors = []
    for y in range(len(board.field)):
        for x in range(len(board.field)):
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

        self.field = [['К', 'К', '.', '.', 'В', 'В', '.', '.', 'К', 'К'],
                      ['К', 'К', '.', 'К', '.', '.', 'К', '.', '.', 'К'],
                      ['К', 'К', '.', '.', '.', '.', '.', '.', 'К', 'К'],
                      ['.', '.', 'К', '.', '.', '.', 'К', '.', '.', 'К'],
                      ['В', '.', 'К', 'К', '.', 'К', '.', '.', '.', 'В'],
                      ['В', 'К', 'К', 'К', '@', '.', 'К', '.', '.', 'В'],
                      ['.', '.', 'К', 'К', '.', '.', '.', '.', '.', 'К'],
                      ['К', '.', '.', '.', 'К', '.', '.', 'К', 'К', 'К'],
                      ['К', '.', 'К', '.', '.', '.', '.', '.', '.', '.'],
                      ['К', 'К', '.', '.', 'В', 'В', '.', '.', 'К', 'К']]

        self.generate_wall()

    def generate_wall(self):
        for y in range(self.height):
            self.field[y] = ["C"] + self.field[y] + ["C"]
        self.field.insert(0, ["C"] * len(self.field[0]))
        self.field.insert(len(self.field), ["C"] * len(self.field[0]))

        for y in range(len(self.field)):
            for x in range(len(self.field)):
                if y == 0 and x > 0:
                    if self.field[y + 1][x] == "B" or self.field[y + 1][x] == 'В':
                        self.field[y][x] = "Д"
                elif x == 0 and y > 0:
                    if self.field[y][x + 1] == "B" or self.field[y][x + 1] == 'В':
                        self.field[y][x] = "Д"
                elif y == len(self.field) - 1 and x > 0:
                    if self.field[y - 1][x] == "B" or self.field[y - 1][x] == 'В':
                        self.field[y][x] = "Д"
                elif x == len(self.field) - 1 and y > 0:
                    if self.field[y][x - 1] == "B" or self.field[y][x - 1] == 'В':
                        self.field[y][x] = "Д"

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

        self.rect = self.image.get_rect()
        x_n, y_n = board.return_heroes_cords()
        self.rect.x = x_n * (cell_cize) - 20 + cell_cize
        self.rect.y = y_n * (cell_cize) + cell_cize - 33

    def move(self, event):
        x_her, y_her = board.return_heroes_cords()
        speed = board.cell_size

        if event.key == pygame.K_RIGHT:
            self.rect.x += speed
            self.image = self.image_left
            if board.field[y_her][x_her + 1] in "KКСCД":
                self.rect.x -= speed
                return
            board.field[y_her][x_her] = '.'
            board.field[y_her][x_her + 1] = "@"

            camera.update(heroes, 'x')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_LEFT:
            self.rect.x -= speed
            self.image = self.image_right
            if board.field[y_her][x_her - 1] in "KКСCД":
                self.rect.x += speed
                return
            board.field[y_her][x_her] = '.'
            board.field[y_her][x_her - 1] = "@"

            camera.update(heroes, 'x')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_UP:
            self.rect.y -= speed
            if board.field[y_her - 1][x_her] in "KКСCД":
                self.rect.y += speed
                return
            board.field[y_her - 1][x_her] = "@"
            board.field[y_her][x_her] = "."

            camera.update(heroes, 'y')
            for elem in all_sprite:
                camera.apply(elem)

        if event.key == pygame.K_DOWN:
            self.rect.y += speed
            if board.field[y_her + 1][x_her] in "KКСCД":
                self.rect.y -= speed
                return
            board.field[y_her + 1][x_her] = "@"
            board.field[y_her][x_her] = "."

            camera.update(heroes, 'y')
            for elem in all_sprite:
                camera.apply(elem)

    def del_box(self, elem, delta_x):
        """
        функция заменяет в поле доски коробку на пустоту путем удаления спрайта коробки и создания спрайта пола
        значения 32, 33, 98 получены путем вычисления разниц координат спрайтов
        """
        delta_y = abs(self.rect.y - elem.rect.y)
        x_her, y_her = board.return_heroes_cords()
        if delta_y == 32:
            board.field[y_her - 1][x_her + delta_x] = '.'
        elif delta_y == 33:
            board.field[y_her][x_her + delta_x] = '.'
        elif delta_y == 98:
            board.field[y_her + 1][x_her + delta_x] = '.'
        pol = Pol()
        pol.rect.x = elem.rect.x
        pol.rect.y = elem.rect.y
        elem.kill()

    def left_box_attack(self, DISTANCE, *args):
        """
        проверка корректности атаки коробок, когда герой находится левее коробки
        атака совершается в случае правильности логики
        """
        for elem in box_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x + 20 >= elem.rect.x or abs(elem.rect.x - self.rect.x) > board.cell_size + 20 + DISTANCE:
                    return
                if elem.rect.y <= self.rect.y:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size - 33 + DISTANCE):
                        return
                else:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size + 33 + DISTANCE):
                        return
                self.del_box(elem, 1)

    def right_box_attack(self, DISTANCE, *args):
        """
        проверка корректности атаки коробок, когда герой находится правее коробки
        атака совершается в случае правильности логики
        """
        for elem in box_sprite:
            if elem.rect.collidepoint(args[0].pos):
                if self.rect.x < elem.rect.x or abs(elem.rect.x - self.rect.x) > board.cell_size - 20 + DISTANCE:
                    return
                if elem.rect.y <= self.rect.y:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size - 33 + DISTANCE):
                        return
                else:
                    if not (abs(elem.rect.y - self.rect.y) <= board.cell_size + 33 + DISTANCE):
                        return
                self.del_box(elem, -1)

    def attack(self, *args):
        DISTANCE = 0  # коээфицент дальности
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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            heroes.move(event)
        if event.type == pygame.MOUSEBUTTONUP:
            heroes.attack(event)

    screen.fill(pygame.Color('black'))
    door_sprite.draw(screen)
    all_sprite.draw(screen)
    heroes_sprite.draw(screen)
    clock.tick(30)
    pygame.event.pump()
    pygame.display.flip()
