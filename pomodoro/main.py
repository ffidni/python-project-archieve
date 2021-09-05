from os import system
CLEAR = lambda: print("\033[H\033[J")
RESIZE = lambda: system("MODE 70, 30")
RESIZE()
CLEAR()
from pygame import mixer
CLEAR()
from time import sleep
from datetime import timedelta
from functions import *
from threading import Thread
from win10toast import ToastNotifier

TAB = "\t"+" "
LINE = "\n"*8
WORK = 1500
SHORT_BREAK = 300
LONG_BREAK = 600
return_values = {'user_input':0,'seconds':0,'timer_name':'',
                 'work_count':0}
timer = ""
flag = True

if __name__ == '__main__':
    RESIZE()
    main()
