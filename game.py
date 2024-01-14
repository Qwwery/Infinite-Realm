import pygame
import os
from heroes_file import Heroes
from box_file import get_boxes
from doors_file import get_doors
from pol_file import get_pols, Pol
from walls_file import get_walls
from portal_file import get_partals
from trap_file import get_trap
from enemy_file import get_enemy
from camera_files import Camera
from maps import generation_map
from board_file import Board


class Game:
    def __init__(self, WIDTH, HEIGHT, board, cell_cize, screen, clock):
        self.start_fon = self.load_image(name='start_fon2.png', png=True, obrezanie_fon=False)
        self.start_fon = pygame.transform.scale(self.start_fon, (WIDTH, HEIGHT))
        self.end_fon = self.load_image(name='died.png', png=True, obrezanie_fon=False)
        self.end_fon = pygame.transform.scale(self.end_fon, (WIDTH, HEIGHT))
        self.wall_image = self.load_image(name='wall.png', png=True, obrezanie_fon=False)
        self.pol_image = self.load_image(name='pol.png', png=True, obrezanie_fon=False)
        self.door_image = self.load_image(name='door.png', png=True, obrezanie_fon=False)
        self.box_image = self.load_image(name='box.png', png=True, obrezanie_fon=False)
        self.heroes_image = self.load_image(name='heroes.png', png=True, obrezanie_fon=False)
        self.portal_image = self.load_image(name='portal2.png', png=True, obrezanie_fon=False)
        self.trap_image1 = self.load_image(name='trap1.png', png=True, obrezanie_fon=False)
        self.trap_image2 = self.load_image(name='trap2.png', png=True, obrezanie_fon=False)
        self.trap_image3 = self.load_image(name='trap5.png', png=True, obrezanie_fon=False)
        self.enemy_image = self.load_image(name='enemy3.png', png=True, obrezanie_fon=True)
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

        self.start_music = pygame.mixer.Sound(os.path.join('assets', 'music', 'start.mp3'))
        self.start_music.set_volume(0.2)

        self.trap_sound = pygame.mixer.Sound(os.path.join('assets', 'music', 'trap.mp3'))
        self.dead_music = pygame.mixer.Sound(os.path.join('assets', 'music', 'fon_dead.mp3'))
        self.kill = pygame.mixer.Sound(os.path.join('assets', 'music', 'kill.mp3'))
        self.level_sound = pygame.mixer.Sound(os.path.join('assets', 'music', 'level.wav'))
        self.box_sound = pygame.mixer.Sound(os.path.join('assets', 'music', 'box_sound.mp3'))

        self.make_sprites()

        self.camera = Camera(WIDTH, HEIGHT)
        self.heroes = Heroes(self.all_sprite, self.heroes_sprite, self.heroes_image, self.cell_cize, board, self.camera,
                             self.box_sprite, Pol, self.pol_sprite,
                             self.pol_image, self.trap_sprite, self.enemy_sprite, self.enemy_image, self.door_sprite,
                             self.kill)

    def load_image(self, name, png=False, obrezanie_fon=False):
        fullname = os.path.join('assets', 'data', name)
        image = pygame.image.load(fullname)
        if obrezanie_fon:  # убрать фон
            del_color = image.get_at((0, 0))
            image.set_colorkey(del_color)
        if not png:
            image = image.convert()
        else:
            image = image.convert_alpha()  # png
        return image

    def start_game(self):
        self.screen.blit(self.start_fon, (0, 0))
        self.start_music.play(-1)
        run_start = True
        while run_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    run_start = False
                    self.start_music.stop()
            pygame.display.flip()

    def render(self, obj, size=25, x=37.0634, y=-5):
        font = pygame.font.Font(None, size)
        text = font.render(str(obj.hp), True, pygame.Color("red"))
        text_x = obj.rect.x + x
        text_y = obj.rect.y + y
        self.screen.blit(text, (text_x, text_y))

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.fon, (0, 0))
        self.door_sprite.draw(self.screen)
        self.all_sprite.draw(self.screen)
        self.enemy_sprite.draw(self.screen)
        self.heroes_sprite.draw(self.screen)
        self.clock.tick(30)
        self.render(self.heroes, size=25, x=37.0634, y=-5)
        for elem in self.enemy_sprite:
            self.render(elem, size=15, x=18, y=-13)
        pygame.event.pump()
        pygame.display.flip()

    def check_damage_trap(self):
        check_intersection = self.heroes.check_intersection_trap(self.trap_sprite)
        if check_intersection:
            check_intersection.update()
            if check_intersection.cur_image == 1:
                self.heroes.hp -= 10
                if self.heroes.hp > 0:
                    self.trap_sound.play(0)

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
        get_partals(self.board, self.all_sprite, self.portal_sprite, self.portal_image, self.cell_cize)
        get_walls(self.board, self.wall_sprite, self.cell_cize, self.all_sprite, self.wall_image)
        get_pols(self.board, self.pol_sprite, self.cell_cize, self.pol_image, self.all_sprite)
        get_doors(self.board, self.all_sprite, self.door_sprite, self.door_image, self.cell_cize)
        get_boxes(self.board, self.all_sprite, self.box_sprite, self.box_image, self.cell_cize, self.box_sound)
        get_trap(self.board, self.all_sprite, self.trap_sprite, self.trap_image1, self.trap_image2, self.trap_image3,
                 self.cell_cize)
        try:
            get_enemy(self.board, self.all_sprite, self.enemy_sprite, self.enemy_image, self.cell_cize, self.heroes,
                      self.door_sprite)
        except Exception:
            pass

    def new_level(self):
        f = open('count.txt', mode='w')
        f.write('0')
        f.close()
        if self.heroes.hp > 0:
            self.level_sound.play(0)

        self.dead_music.stop()
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
        self.heroes.hp = 100

    def new_game(self):
        self.screen.blit(self.end_fon, (0, 0))
        run_start = True
        while run_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    run_start = False
            pygame.display.flip()

    def check_heroes_hp(self):
        if self.heroes.hp <= 0:
            self.dead_music.play(-1)
            self.new_game()
            self.new_level()

    def move_enemy(self):
        for y in range(len(self.board.field)):
            for x in range(len(self.board.field[y])):
                if self.board.field[y][x] in 'EЕ':
                    self.board.field[y][x] = '.'
        for elem in self.enemy_sprite:
            self.board.field[elem.y][elem.x] = 'E'
        for elem in self.enemy_sprite:
            elem.move()


def run():
    n = 10
    cell_cize = 65
    running = True

    pygame.init()
    pygame.key.set_repeat(200, 70)
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = 1000, 1000
    # WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

    pygame.display.set_caption('Ты будешь гореть в аду')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    board = Board(n, n, cell_cize)
    game = Game(WIDTH, HEIGHT, board, cell_cize, screen, clock)
    game.start_game()
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
        game.move_enemy()
