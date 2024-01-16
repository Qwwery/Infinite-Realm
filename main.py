from game import run
from start_window import start_window, guide, settings
import pygame
import os

if __name__ == "__main__":
    pygame.init()
    sound = pygame.mixer.Sound(os.path.join('assets', 'music', 'a.mp3'))
    sound.set_volume(0.088)
    voice = pygame.mixer.Channel(5)
    open(os.path.join('assets', 'files_for_info_game', 'this_fon.txt'), mode='w').write('True')
    sound.play(-1)
    lvl = 1
    hp = 100
    while True:
        result = start_window()
        if result == 'run':
            break
        elif result == 'settings':
            settings(sound, voice)
        elif result == 'manual':
            guide()

        elif result == 'exit':
            quit()
        elif result == 'continue':
            with open(os.path.join('assets', 'files_for_info_game', 'LAST_LEVEL.txt'), 'r') as info:
                try:
                    info = info.read().split('\n')
                    lvl = int(info[0])
                    hp = int(info[1])
                except Exception:
                    lvl = 1
                    hp = 100
            break

    run(sound, voice, lvl, hp)
