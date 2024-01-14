from game import run
from start_window import start_window, manual, setings


if __name__ == "__main__":
    while True:
        resilt = start_window()
        if resilt == 'run':
            break
        elif resilt == 'manual':
            manual()
        elif resilt == 'setings':
            setings()
        elif resilt == 'exit':
            quit()
    run()
