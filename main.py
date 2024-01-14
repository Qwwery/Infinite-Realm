from game import run
from start_window import start_window, guide, settings


if __name__ == "__main__":
    while True:
        result = start_window()
        if result == 'run':
            break
        elif result == 'settings':
            settings()
        elif result == 'manual':
            guide()
        elif result == 'exit':
            quit()
    run()
