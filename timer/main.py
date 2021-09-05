from threading import Thread
from time import sleep
from datetime import timedelta
#from win10toast import ToastNotifier
from os import system
from pygame import mixer
import keyboard

CLEAR = lambda: system('cls')

class Timer:

    def __init__(self):
        self.seconds = 0
        self.timer = '9:00:60'
        self.resume = 0
        self.pointer = len(self.timer)-1
        self.flag = True

    def notifications(self):
        mixer.init()
        notif_popup = ToastNotifier()
        notif_sound = mixer.Sound('C:\\Users\\asd\\Desktop\\coding stuffs\\projects\\timer\\Assets\\notification.mp3')
        notif_sound.set_volume(0.4)
        notif_sound.play()
        notif_popup.show_toast("Timer", "Time's up!")


    def start_timer(self, seconds):
        self.timer = str(timedelta(seconds=seconds))
        while flag and seconds:
            if not int(self.timer[0]):
                self.timer = self.timer[2:]
            print(self.timer)
            seconds -= 1
            sleep(1)

        if seconds: self.resume = seconds

    def set_timer(self):
        timer_format = list(self.timer)
        while not self.seconds:
            CLEAR()
            length = len(self.timer)-1
            print(length)
            h = int(self.timer[0])
            m = int(self.timer[length-4:length-2])
            s = int(self.timer[length-1:length+1])
            if m >= 60:
                m = 0
                h += 1
                timer_format[2:4] = ['0','0']
                timer_format[0] = str(h)
            elif s >= 60:
                s = 0
                m += 1
                timer_format[5:7] = ['0','0']
                timer_format[2:4] = list(str(m)) if m >= 10 else ['0', str(m)]

            self.timer = ''.join(timer_format)
            try:
                add_number = str(int(timer_format[self.pointer]) + 1)
                subtract_number = str(int(timer_format[self.pointer]) - 1)
                if keyboard.is_pressed('left'):
                    if self.timer[self.pointer-1] == ':':
                        self.pointer -= 2
                    else:
                        self.pointer -= 1
                elif keyboard.is_pressed('right'):
                    if self.timer[self.pointer+1] == ':' and self.pointer != len(timer_format):
                        self.pointer += 2
                    else:
                        self.pointer += 1
                elif keyboard.is_pressed('up'):
                    if len(add_number) == 2 and self.pointer == 0:
                        timer_format[self.pointer:self.pointer+1] = [str(int(timer_format[self.pointer-1])
                                                                       +int(add_number[0])),'0']
                    elif len(add_number) == 1:
                        timer_format[self.pointer] = add_number
                elif keyboard.is_pressed('down'):
                    if timer_format[self.pointer] != '0':
                        timer_format[self.pointer] = subtract_number
                elif keyboard.is_pressed('enter'):
                    self.timer = ''
                    self.seconds = h*3600+m*60+s
            except:
                pass
            
            #timer_format = list(self.timer)
            print(self.timer+'\n{}-'.format(' '*self.pointer))
            
            #print("\nChange the value by pressing arrow up or down in the keyboard")
            #print("and arrow left or right to change the position, Press enter if you're done.")
            sleep(0.04)
  
        
if __name__ == '__main__':
	timer = Timer()
	timer.set_timer()