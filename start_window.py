import pygame
import os


def load_image(name, png=False, obrezanie_fon=False):
    full_name = os.path.join('assets', 'data', name)
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
    running = True

    pygame.init()
    pygame.key.set_repeat(200, 70)
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

    pygame.display.set_caption('Ты готов гореть в аду?')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    start_fon_1 = load_image(name='bnju_bnjut1.png', png=True, obrezanie_fon=True)
    start_fon_2 = load_image(name='bnju_bnjut2.png', png=True, obrezanie_fon=True)
    start_fon_3 = load_image(name='bnju_bnjut3.png', png=True, obrezanie_fon=True)
    start_fon_4 = load_image(name='bnju_bnjut4.png', png=True, obrezanie_fon=True)

    start_fon = pygame.transform.scale(start_fon_1, (WIDTH, HEIGHT))

    screen.blit(start_fon, (0, 0))
    pygame.display.flip()
    point = 0
    def draw(point):
        if point == 0:
            start_fon = pygame.transform.scale(start_fon_1, (WIDTH, HEIGHT))
        elif point == 1:
            start_fon = pygame.transform.scale(start_fon_2, (WIDTH, HEIGHT))
        elif point == 2:
            start_fon = pygame.transform.scale(start_fon_3, (WIDTH, HEIGHT))
        else:
            start_fon = pygame.transform.scale(start_fon_4, (WIDTH, HEIGHT))
        screen.blit(start_fon, (0, 0))
        pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.KEYDOWN:
                if event.key == 1073741905:
                    point += 1
                    if point > 3:
                        point = 0
                elif event.key == 1073741906:
                    point -= 1
                    if point < 0:
                        point = 3
                elif event.key == 13:
                    if point == 0:
                        return 'run'
                    elif point == 1:
                        return 'continue'
                    elif point == 2:
                        return 'settings'
                    elif point == 3:
                        return 'manual'
                draw(point)


def settings(sound, voice):
    running = True
    with open(os.path.join('assets', 'files_for_info_game', 'this_fon.txt'), 'r') as file:
        file = file.read()
        this_fon = True if file == 'True' else False
    pygame.init()
    pygame.key.set_repeat(200, 70)
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ты готов гореть в аду?')

    volume_fon = load_image(name='volume.png', png=True, obrezanie_fon=True)
    volume_fon = pygame.transform.scale(volume_fon, (WIDTH, HEIGHT))

    not_volume_fon = load_image(name='not_volume.png', png=True, obrezanie_fon=True)
    not_volume_fon = pygame.transform.scale(not_volume_fon, (WIDTH, HEIGHT))
    if this_fon:
        screen.blit(volume_fon, (0, 0))

    else:
        screen.blit(not_volume_fon, (0, 0))

    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if this_fon:
                    this_fon = False
                    sound.stop()
                    screen.blit(not_volume_fon, (0, 0))
                else:
                    this_fon = True
                    if not voice.get_busy():
                        sound.play(-1)

                    screen.blit(volume_fon, (0, 0))
                with open(os.path.join('assets', 'files_for_info_game', 'this_fon.txt'), 'w') as file:
                    file.write(str(this_fon))
                pygame.display.flip()
            elif event.type == 768:
                return


def guide():
    pass
