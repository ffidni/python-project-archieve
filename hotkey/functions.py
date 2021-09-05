from time import sleep
from os import system, path
import webbrowser
import json
import keyboard

CLEAR_SCREEN = lambda: system('cls') 
DATA_PATH = 'C:/Users/asd/desktop/coding stuffs/projects/hotkey/db.json'
files = {}
hotkeys = []

def load_files():
    global files
    with open(DATA_PATH) as f:
        files = json.load(f)
    return files

def list_of_files():
    CLEAR_SCREEN()
    print("List of folder and files: ")
    for index,value in enumerate(files):
        print(f"{index+1}:\n\tName: {' '.join(value.split('_'))}\n\tHotkey: {files[value][1]}\n")

def remove_file():
    global hotkey
    list_of_files()
    user_input = input('Remove a file / Back: ').upper()
    if user_input in files:
            if user_input in files:
                files.pop(user_input)
                dump_file(files)
                hotkeys.remove(user_input)
                print(f"{user_input} has been removed from the list.")
                sleep(1)
                remove_file()
            else:
                print(f"{user_input} is not in the list.")
                sleep(1)
                remove_file()
    else:
        menu()

def dump_file(data):
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)

def add_file(name=None):
    global hotkey
    list_of_files()
    user_input = input('Add / Back: ')
    if 'add' in user_input:
        if not name:
                name = '_'.join(input("Input the folder's name: ").upper().split())
        link = input("Input the folder's path: ")
        if path.exists(link):
            files[name] = [f"lambda: webbrowser.open('file:///{link}')"]
            hotkey = input("Add hotkey, e.g -> shift+x: ")
            files[name].append(hotkey)
            dump_file(files)
            hotkeys.append(name)
            print(f"Name: {name}\nPath: {link}\nHotkey: {hotkey} has been added to the list.")
            sleep(1)
            menu()
        else:
            print("The path is not valid!")
            sleep(1)
            add_file(name)
    elif 'back' in user_input:
        menu()
    else:
        add_file()
        
def open_file():
        list_of_files()
        user_input = '_'.join(input('Select a file / Back: ').upper().split())
        print(user_input)
        if user_input in files:
            eval(files[user_input][0])()
        elif user_input != 'BACK' and user_input not in files:
                print(f"{user_input} is not in the list.")
                user_input = input('Do you want to add it to the list?: Y / N: ').lower()
                if user_input == 'y':
                    menu('add')
                else:
                    open_file()
        
        else:
            menu()
            


def menu(shortcut=None):
    CLEAR_SCREEN()
    load_files()
    if not shortcut:
        user_input = input("1. Open File\n2. Add/Remove File\n3. Quit\n\nYour input: ").lower()
        if 'open' in user_input:
            open_file()
        elif 'add' in user_input:
            add_file()
        elif 'remove' in user_input:
            remove_file()
        elif 'quit' in user_input:
            quit()
        else:
            menu()
    else:
        add_file()


if __name__ == '__main__':
    menu()
