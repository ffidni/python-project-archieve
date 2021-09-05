from time import sleep
from webbrowser import open
from functions import *
import keyboard

menu = lambda: open('file:///C:/Users/asd/desktop/coding stuffs/projects/hotkey/functions.py')

def main():
    global hotkeys
    files = load_files()
    hotkeys = [i for i in files]
    for name in files:
        keyboard.add_hotkey(files[name][1], eval(files[name][0]))
    keyboard.add_hotkey('ctrl+shift+z', menu)
    while True:
        for name in files:
            if name not in hotkeys:
                keyboard.add_hotkey(files[name][1], eval(files[name][0]))

        sleep(0.8)

if __name__ == '__main__':
    main()
