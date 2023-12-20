import pygame
import os


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
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.left_start = 10
        self.top_start = 10
        self.cell_size = 50

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

    def set_view(self, left, top, cell_size):
        self.left_start = left
        self.top_start = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(len(self.field)):
            for x in range(len(self.field)):
                if self.field[y][x] == 'К' or self.field[y][x] == "K":
                    screen.blit(self.box, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))
                elif self.field[y][x] == "." or self.field[y][x] == "B" or self.field[y][x] == 'В':
                    screen.blit(self.pol, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))
                elif self.field[y][x] == "C" or self.field[y][x] == "С":
                    screen.blit(self.wall, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))
                elif self.field[y][x] == "Д":
                    screen.blit(self.door, (x * self.cell_size + self.left_start, y * self.cell_size + self.top_start))

                pygame.draw.rect(screen, pygame.Color('white'),
                                 (self.cell_size * x + self.left_start, self.cell_size * y + self.top_start,
                                  self.cell_size, self.cell_size), width=1)


n = 10
cell_cize = 80
pygame.init()
pygame.display.set_caption('room')
screen = pygame.display.set_mode((963, 963))
board = Board(n, n)
running = True

screen.fill((0, 0, 0))
board.set_view(0, 0, cell_cize)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()