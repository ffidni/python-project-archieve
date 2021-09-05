from time import sleep
from os import system
from datetime import timedelta
from threading import Thread
from ctypes import windll



flag = True
RESIZE = lambda: system('MODE 30, 8')
CLEAR = lambda: system('cls')
return_values = {'user_input':0,'stopwatch':0}


def start_stopwatch(seconds=0):
    while flag:
        CLEAR()
        print(f'\n\n\n\t   {str(timedelta(seconds=seconds))}\n\t[Stop] [Close]\t\n')
        seconds += 1
        sleep(1)

    return_values['stopwatch'] = seconds - 1

def stop_stopwatch():
    CLEAR()
    user_input = input(f'\n\n\n\t   {str(timedelta(seconds=return_values["stopwatch"]))}\n   [Resume] [Close] [Reset]\t\n\n').lower()
    return user_input

def resume_stopwatch():
    global flag
    CLEAR()
    resume = return_values['stopwatch']
    flag = True
    return resume

def reset_stopwatch():
    CLEAR()
    return_values['stopwatch'] = 0
    user_input = input(f'\n\n\n\t   {str(timedelta(seconds=return_values["stopwatch"]))}\n\t[Start] [Close]\t\n\n').lower()
    return user_input

def get_input():
    return_values['user_input'] = input('').lower()

def main(resume=0):
    global flag

    RESIZE()
    user_input = input(f'\n\n\n\t   {str(timedelta(seconds=return_values["stopwatch"]))}\n\t[Start] [Close]\t\n\n').lower()
    if user_input:
        while return_values['user_input'] != 'close' and user_input != 'close':
            t1 = Thread(target=start_stopwatch, args=(resume,))
            t2 = Thread(target=get_input)
            t1.start()
            t2.start()

            t2.join()
            flag = False
            sleep(1)
        
            if return_values['user_input'] == 'stop':
                user_input = stop_stopwatch()
                if user_input == 'resume':
                    resume = resume_stopwatch()
                elif user_input == 'reset':
                    user_input = reset_stopwatch()
                    if user_input == 'start':
                        resume = 0
                        flag = True


if __name__ == '__main__':
    windll.kernel32.SetConsoleTitleW("Stopwatch")
    main()
