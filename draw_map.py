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

        self.left_start = 94
        self.top_start = 94
        self.cell_size = cell_cize

        self.field = [['К', 'К', '.', '.', 'В', 'В', '.', '.', 'К', 'К'],
                      ['К', 'К', '.', 'К', '.', '.', 'К', '.', '.', 'К'],
                      ['К', 'К', '.', '.', '.', '.', '.', '.', 'К', 'К'],
                      ['.', '.', 'К', '.', '.', '.', 'К', '.', '.', 'К'],
                      ['В', '.', 'К', 'К', '.', 'К', '.', '.', '.', 'В'],
                      ['В', 'К', 'К', 'К', 'К', '.', 'К', '.', '.', 'В'],
                      ['.', '.', 'К', 'К', '.', '.', '.', '.', '.', 'К'],
                      ['К', '.', '.', '.', 'К', '.', '.', 'К', 'К', 'К'],
                      ['К', '.', 'К', '.', '.', '.', '.', '.', 'К', 'К'],
                      ['К', 'К', '.', '.', 'В', 'В', '.', '.', 'К', 'К']]

        self.generate_wall()
        self.box = load_image(name='box.png', png=True, obrezanie_fon=False)
        self.pol = load_image(name='pol.png', png=True, obrezanie_fon=False)
        self.door = load_image(name='door.png', png=True, obrezanie_fon=False)
        self.box = pygame.transform.scale(self.box, (cell_cize, cell_cize))
        self.pol = pygame.transform.scale(self.pol, (cell_cize, cell_cize))
        self.door = pygame.transform.scale(self.door, (cell_cize, cell_cize))
        self.wall = load_image(name='wall.png', png=True, obrezanie_fon=False)
        self.wall = pygame.transform.scale(self.wall, (cell_cize, cell_cize))

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

    def render(self, screen):
        for y in range(len(self.field)):
            for x in range(len(self.field)):
                # if self.field[y][x] == 'К' or self.field[y][x] == "K":
                # screen.blit(self.box, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))
                if self.field[y][x] == "." or self.field[y][x] == "B" or self.field[y][x] == 'В':
                    screen.blit(self.pol, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))
                elif self.field[y][x] == "Д":
                    screen.blit(self.door, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))

               # pygame.draw.rect(screen, pygame.Color('pink'),
                                # (self.cell_size * x + self.left_start, self.cell_size * y + self.top_start,
                                #  self.cell_size, self.cell_size), width=1)


class Heroes(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(all_sprite, heroes_sprite)
        self.image = load_image(name='heroes.png', png=True, obrezanie_fon=False)
        self.image = pygame.transform.scale(self.image, (cell_cize * 1.5, cell_cize * 1.5))
        self.mask = pygame.mask.from_surface(self.image)
        self.image_left = pygame.transform.flip(surface=self.image, flip_x=True, flip_y=False)
        self.image_right = self.image

        self.rect = self.image.get_rect()
        self.rect.x = 6 * cell_cize + 20
        self.rect.y = 3 * cell_cize

    def update(self, event):
        x = (self.rect.x - board.left_start) // board.cell_size
        y = (self.rect.y - board.top_start) // board.cell_size
        speed = 0.65
        if event.key == pygame.K_RIGHT:
            self.rect.x += speed
            self.image = self.image_right
            for elem in walls:
                if pygame.sprite.collide_mask(self, elem):
                    self.rect.x -= speed
                    self.image = self.image_left
                    return
            if x < len(board.field) and board.field[y + 1][x + 1] in "KК":
                self.rect.x -= speed
                self.image = self.image_left

        if event.key == pygame.K_LEFT:
            self.rect.x -= speed
            self.image = self.image_left
            for elem in walls:
                if pygame.sprite.collide_mask(self, elem):
                    self.rect.x += speed
                    self.image = self.image_right
                    return
            if x > 0 and board.field[y + 1][x] in "KК":
                self.rect.x += speed
                self.image = self.image_right

        if event.key == pygame.K_UP:
            self.rect.y -= speed
            for elem in walls:
                if pygame.sprite.collide_mask(self, elem):
                    self.rect.y += speed
                    return
            for elem in boxes:
                if pygame.sprite.collide_mask(self, elem):
                    if board.field[y][x + 1] in "KК":
                        self.rect.y += speed
                        return

        if event.key == pygame.K_DOWN:
            self.rect.y += speed
            for elem in walls:
                if pygame.sprite.collide_mask(self, elem):
                    self.rect.y -= speed
                    return
            for elem in boxes:
                if pygame.sprite.collide_mask(self, elem):
                    if board.field[y + 1][x + 1] in "KК":
                        self.rect.y -= speed
                        return


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


n = 10
cell_cize = 65
pygame.init()
pygame.key.set_repeat(True)
clock = pygame.time.Clock()
pygame.display.set_caption('room')
screen = pygame.display.set_mode((963, 963))

all_sprite = pygame.sprite.Group()
heroes_sprite = pygame.sprite.Group()
wall_sprite = pygame.sprite.Group()
box_sprite = pygame.sprite.Group()
heroes = Heroes(heroes_sprite)
board = Board(n, n, cell_cize)
walls = get_walls().copy()
boxes = get_boxes().copy()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            heroes.update(event)

    screen.fill(pygame.Color('black'))
    board.render(screen)
    all_sprite.draw(screen)
    board.render(screen)
    heroes_sprite.draw(screen)
    clock.tick(30)
    pygame.event.pump()
    pygame.display.flip()