import pygame
import os
from maps import generation_map
from heroes_file import Heroes
from box_file import get_boxes
from doors_file import get_doors
from pol_file import get_pols, Pol
from walls_file import get_walls


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


class Camera:
    def __init__(self, width, height):
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height

    def apply(self, obj_sprite):
        obj_sprite.rect.x += self.dx
        obj_sprite.rect.y += self.dy

    def update(self, tracker_obj, check):
        self.dx = 0
        self.dy = 0
        y_n = 2
        x_n = 2
        if check == 'x':
            self.dx = -(tracker_obj.rect.x + tracker_obj.rect.w // x_n - self.width // x_n)
        elif check == 'y':
            self.dy = -(tracker_obj.rect.y + tracker_obj.rect.h // y_n - self.height // y_n)


def run():
    n = 10
    cell_cize = 65
    pygame.init()
    pygame.key.set_repeat(200, 70)
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = 1000, 1000
    pygame.display.set_caption('room')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
    pol_sprite = pygame.sprite.Group()

    board = Board(n, n, cell_cize)

    get_walls(board, wall_sprite, cell_cize, all_sprite, wall_image)
    get_pols(board, pol_sprite, cell_cize, pol_image, all_sprite)
    get_doors(board, all_sprite, door_sprite, door_image, cell_cize)
    get_boxes(board, all_sprite, box_sprite, box_image, cell_cize)

    camera = Camera(WIDTH, HEIGHT)
    heroes = Heroes(all_sprite, heroes_sprite, heroes_image, cell_cize, board, camera, box_sprite, Pol, pol_sprite,
                    pol_image)

    running = True

    camera.update(heroes, 'y')
    for elem in all_sprite:
        camera.apply(elem)

    camera.update(heroes, 'x')
    for elem in all_sprite:
        camera.apply(elem)

    fon = load_image(name='fon3.png', png=True, obrezanie_fon=False)
    fon = pygame.transform.scale(fon, (2000, 2000))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                heroes.attack(event)
            if event.type == pygame.KEYDOWN:
                heroes.move(event)

        screen.fill((0, 0, 0))
        screen.blit(fon, (0, 0))
        door_sprite.draw(screen)
        all_sprite.draw(screen)
        heroes_sprite.draw(screen)
        clock.tick(30)
        pygame.event.pump()
        pygame.display.flip()


run()
