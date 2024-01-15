from game import run
from start_window import start_window, guide, settings
import pygame, os

if __name__ == "__main__":
    pygame.init()
    sound = pygame.mixer.Sound(os.path.join('assets', 'music', 'a.mp3'))
    sound.set_volume(0.088)
    voice = pygame.mixer.Channel(5)
    open('this_fon.txt', mode='w').write('True')
    sound.play(-1)
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
    run(sound, voice)
