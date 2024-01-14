import pygame, os


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * height for i in range(width)]

        self.left = 0
        self.top = 0
        self.cell_size = 30

    def render(self, screen):
        for y_num in range(self.height):
            for x_num in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (
                self.cell_size * x_num + self.left, self.cell_size * y_num + self.top, self.cell_size, self.cell_size),
                                 3)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x = (x - self.left) // self.cell_size
        y = (y - self.top) // self.cell_size

        if x < 0 or y < 0 or x + 1 > self.height or y + 1 > self.width:
            return None
        return x, y




def load_image(name, png=False, obrezanie_fon=False):
    full_name = os.path.join('image', 'start_images', name)
    image = pygame.image.load(full_name)
    if obrezanie_fon:  # убрать фон
        del_color = image.get_at((0, 0))
        image.set_colorkey(del_color)
    if not png:
        image = image.convert()
    else:
        image = image.convert_alpha()  # png
    return image

def start_window():
    n = 10
    running = True

    pygame.init()
    pygame.key.set_repeat(200, 70)
    size = WIDTH, HEIGHT = 1000, 1000
    # size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    board = Board(WIDTH, HEIGHT)

    screen = pygame.display.set_mode(size)
    board.render(screen)


    pygame.display.set_caption('Ты готов гореть в аду?')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    start_fon = load_image(name='fon.png', png=True, obrezanie_fon=True)
    start_fon = pygame.transform.scale(start_fon, (WIDTH, HEIGHT))
    screen.blit(start_fon, (0, 0))
    pygame.display.flip()
    font = pygame.font.Font(None, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = board.get_cell(event.pos)
                if 9 <= y <= 12:
                    return 'run'
                elif 13 <= y <= 17:
                    return 'countinue'
                elif 18 <= y <= 22:
                    return 'settings'
                elif 23 <= y <= 25:
                    return 'guide'


def settings():

    n = 10
    running = True
    with open('this_fon.txt', 'r') as file:
        file = file.read()
        this_fon = True if file == 'True' else False
    pygame.init()
    pygame.key.set_repeat(200, 70)
    size = WIDTH, HEIGHT = 1000, 1000
    # size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    board = Board(WIDTH, HEIGHT)

    screen = pygame.display.set_mode(size)
    board.render(screen)


    pygame.display.set_caption('Ты готов гореть в аду?')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    volume_fon = load_image(name='volume.png', png=True, obrezanie_fon=True)
    volume_fon = pygame.transform.scale(volume_fon, (WIDTH, HEIGHT))

    not_volume_fon = load_image(name='not_volume.png', png=True, obrezanie_fon=True)
    not_volume_fon = pygame.transform.scale(not_volume_fon, (WIDTH, HEIGHT))
    print(this_fon)
    if this_fon:
        screen.blit(volume_fon, (0, 0))
    else:
        screen.blit(not_volume_fon, (0, 0))
    pygame.display.flip()
    font = pygame.font.Font(None, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = board.get_cell(event.pos)
                if 7 <= y <= 21:

                    if this_fon:
                        this_fon = False
                        screen.blit(not_volume_fon, (0, 0))
                    else:
                        this_fon = True
                        screen.blit(volume_fon, (0, 0))
                    with open('this_fon.txt', 'w') as file:
                        file.write(str(this_fon))
                    pygame.display.flip()
                elif 30 <= y <= 35:
                    return




def guide():
    pass
