import pygame
import os
from maps import generation_map
from heroes_file import Heroes
from box_file import get_boxes
from doors_file import get_doors
from pol_file import get_pols, Pol
from walls_file import get_walls
from portal_file import get_partals
from trap_file import get_trap
from enemy_file import get_enemy


class Board:
    def __init__(self, width, height, cell_cize):
        self.this_level = 1
        self.width = width
        self.height = height

        self.left_start = 65
        self.top_start = 65
        self.cell_size = cell_cize

        self.field = generation_map()
        self.add_wall(self.field)

        self.new_level = False

    def add_wall(self, field):
        max_len = max(map(lambda x: len(x), field)) + 2
        for i in range(len(field)):
            field[i] = [' '] + field[i] + [' ']
            while len(field[i]) != max_len:
                field[i].append(' ')

        spaces = [" " for _ in range(len(field[0]))]
        field.insert(0, spaces.copy())
        field.extend([spaces.copy()])

        for y in range(1, len(field) - 1):
            for x in range(1, len(field[0]) - 1):
                if field[y][x] != ' ' and field[y][x] != "С":
                    if x - 1 >= 0 and field[y][x - 1] == ' ':
                        field[y][x - 1] = 'С'
                    if x - 1 >= 0 and y - 1 >= 0 and field[y - 1][x - 1] == ' ':
                        field[y - 1][x - 1] = 'С'
                    if y - 1 >= 0 and field[y - 1][x] == ' ':
                        field[y - 1][x] = 'С'
                    if y - 1 >= 0 and x + 1 < len(field[0]) and field[y - 1][x + 1] == ' ':
                        field[y - 1][x + 1] = 'С'
                    if x + 1 < len(field[0]) and field[y][x + 1] == ' ':
                        field[y][x + 1] = 'С'
                    if y + 1 < len(field) and field[y + 1][x] == ' ':
                        field[y + 1][x] = 'С'
                    if y + 1 < len(field) and x - 1 >= 0 and field[y + 1][x - 1] == ' ':
                        field[y + 1][x - 1] = 'С'
                    if y + 1 < len(field) and x + 1 < len(field[0]) and field[y + 1][x + 1] == ' ':
                        field[y + 1][x + 1] = 'С'

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


class Game:
    def __init__(self, WIDTH, HEIGHT, board, cell_cize, screen, clock):
        self.wall_image = self.load_image(name='wall.png', png=True, obrezanie_fon=False)
        self.pol_image = self.load_image(name='pol.png', png=True, obrezanie_fon=False)
        self.door_image = self.load_image(name='door.png', png=True, obrezanie_fon=False)
        self.box_image = self.load_image(name='box.png', png=True, obrezanie_fon=False)
        self.heroes_image = self.load_image(name='heroes.png', png=True, obrezanie_fon=False)
        self.portal_image = self.load_image(name='portal2.png', png=True, obrezanie_fon=False)
        self.trap_image1 = self.load_image(name='trap1.png', png=True, obrezanie_fon=False)
        self.trap_image2 = self.load_image(name='trap2.png', png=True, obrezanie_fon=False)
        self.trap_image3 = self.load_image(name='trap5.png', png=True, obrezanie_fon=False)
        self.enemy_image = self.load_image(name='enemy.png', png=True, obrezanie_fon=False)
        self.fon = self.load_image(name='fon3.png', png=True, obrezanie_fon=False)
        self.fon = pygame.transform.scale(self.fon, (WIDTH, HEIGHT))

        self.all_sprite = pygame.sprite.Group()
        self.heroes_sprite = pygame.sprite.Group()
        self.wall_sprite = pygame.sprite.Group()
        self.box_sprite = pygame.sprite.Group()
        self.door_sprite = pygame.sprite.Group()
        self.pol_sprite = pygame.sprite.Group()
        self.portal_sprite = pygame.sprite.Group()
        self.trap_sprite = pygame.sprite.Group()
        self.enemy_sprite = pygame.sprite.Group()

        self.cell_cize = cell_cize
        self.screen = screen
        self.clock = clock
        self.board = board

        self.make_sprites()

        self.camera = Camera(WIDTH, HEIGHT)
        self.heroes = Heroes(self.all_sprite, self.heroes_sprite, self.heroes_image, self.cell_cize, board, self.camera,
                             self.box_sprite, Pol, self.pol_sprite,
                             self.pol_image, self.trap_sprite, self.enemy_sprite, self.enemy_image, self.door_sprite)

    def load_image(self, name, png=False, obrezanie_fon=False):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        if obrezanie_fon:  # убрать фон
            del_color = image.get_at((0, 0))
            image.set_colorkey(del_color)
        if not png:
            image = image.convert()
        else:
            image = image.convert_alpha()  # png
        return image

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.fon, (0, 0))
        self.door_sprite.draw(self.screen)
        self.all_sprite.draw(self.screen)
        self.enemy_sprite.draw(self.screen)
        self.heroes_sprite.draw(self.screen)
        self.clock.tick(30)
        pygame.event.pump()
        pygame.display.flip()

    def check_damage_trap(self):
        check_intersection = self.heroes.check_intersection_trap(self.trap_sprite)
        if check_intersection:
            check_intersection.update()
            if check_intersection.cur_image == 1:
                self.heroes.hp -= 10

        for trap in self.trap_sprite:
            if trap.cur_image != 0:
                trap.update()

    def check_event(self, event):
        if event.type == pygame.QUIT:
            return 'exit'
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.heroes.check_attack(event)
        if event.type == pygame.KEYDOWN:
            self.heroes.move(event)

            if self.board.new_level:
                return 'new_level'

    def start_update_camera(self):
        self.camera.update(self.heroes, 'y')
        for elem in self.all_sprite:
            self.camera.apply(elem)

        self.camera.update(self.heroes, 'x')
        for elem in self.all_sprite:
            self.camera.apply(elem)

    def make_sprites(self):
        get_walls(self.board, self.wall_sprite, self.cell_cize, self.all_sprite, self.wall_image)
        get_pols(self.board, self.pol_sprite, self.cell_cize, self.pol_image, self.all_sprite)
        get_doors(self.board, self.all_sprite, self.door_sprite, self.door_image, self.cell_cize)
        get_boxes(self.board, self.all_sprite, self.box_sprite, self.box_image, self.cell_cize)
        get_partals(self.board, self.all_sprite, self.portal_sprite, self.portal_image, self.cell_cize)
        get_trap(self.board, self.all_sprite, self.trap_sprite, self.trap_image1, self.trap_image2, self.trap_image3,
                 self.cell_cize)
        try:
            get_enemy(self.board, self.all_sprite, self.enemy_sprite, self.enemy_image, self.cell_cize, self.heroes,
                      self.door_sprite)
        except Exception:
            pass

    def new_level(self):
        self.board.new_level = False
        for elem in self.all_sprite:
            if elem != self.heroes:
                elem.kill()

        self.board.field = generation_map()
        self.board.add_wall(self.board.field)
        self.make_sprites()

        x_n, y_n = self.board.return_heroes_cords()
        self.heroes.rect.x = x_n * self.cell_cize - 20 + self.cell_cize
        self.heroes.rect.y = y_n * self.cell_cize + self.cell_cize - 33

        self.start_update_camera()

    def check_heroes_hp(self):
        if self.heroes.hp <= 0:
            self.new_level()
            self.heroes.hp = 100


def run():
    n = 10
    cell_cize = 65
    running = True

    pygame.init()
    pygame.key.set_repeat(200, 70)
    clock = pygame.time.Clock()
    # WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    WIDTH, HEIGHT = 1000, 1000
    pygame.display.set_caption('room')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    board = Board(n, n, cell_cize)
    game = Game(WIDTH, HEIGHT, board, cell_cize, screen, clock)
    game.start_update_camera()

    while running:
        for event in pygame.event.get():
            res = game.check_event(event)
            if res == 'exit':
                running = False
            if res == 'new_level':
                game.new_level()
        game.check_heroes_hp()
        game.check_damage_trap()
        game.update_screen()

        for elem in game.enemy_sprite:
            elem.move()
