import pygame, os


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
    cell_cize = 65
    running = True

    pygame.init()
    pygame.key.set_repeat(200, 70)
    clock = pygame.time.Clock()
    # WIDTH, HEIGHT = 1000, 1000
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

    pygame.display.set_caption('Ты будешь гореть в аду')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    text_coord = 50
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
                print(pygame.mouse.get_pos())




def manual():
    pass

def setings():
    pass