from cli import *
 
def notifications(name):
    name = ' '.join(name.lower().split('_'))
    mixer.init()
    notif_sound = mixer.Sound('C:\\Users\\asd\\Desktop\\coding-stuffs\\projects\\pomodoro\\Assets\\notification.mp3')
    notif_sound.set_volume(0.4)
    notif_sound.play()
    toaster = ToastNotifier()
    toaster.show_toast("Pomocrastination",f"Time to {'work' if name == 'work' else f'take a {name}'}!")

def pomodoro_timer(timer_name, seconds=0):
    global timer

    if not seconds: globals()[timer_name]
    while flag and seconds:
        timer = str(timedelta(seconds=seconds))[2:]
        show_menu(timer_name, 'RUNNING_')
        sleep(1)
        seconds -= 1

    if not seconds:
        print(timer_name)
        if timer_name == 'WORK':
            return_values['work_count'] += 1
            if return_values['work_count'] == 3:
                timer_name = 'LONG_BREAK'
            else:
                timer_name = 'SHORT_BREAK'
        else:
            timer_name = 'WORK'

        return_values['seconds'] = 0
        return_values['timer_name'] = timer_name
        timer = str(timedelta(seconds=globals()[timer_name]))[2:]
        show_menu(timer_name, 'START_')
        notifications(timer_name)
    
    else : return_values['seconds'] = seconds+1

def pomodoro_input():
    return_values['user_input'] = input("\t\t\tYour Input : ")

def show_menu(name=False, condition=0):
    global timer
    CLEAR()
    if name in ('WORK', 'SHORT_BREAK', 'LONG_BREAK') and condition:
        if not timer or timer == "00:00":
            timer = str(timedelta(seconds=globals()[name]))[2:]
            print(globals()[condition+name].format(line=LINE, tab=TAB, timer=timer))
        else:
            print(globals()[condition+name].format(line=LINE, tab=TAB, timer=timer))  
    elif name == 'SETTINGS':
        print(SETTINGS.format(line=LINE, tab=TAB))
    else:
        print(MENU.format(line=LINE, tab=TAB))

def main_menu():
    show_menu('MENU')
    user_input = '_'.join(input("\t\t\tYour Input : ").upper().split())
    if user_input in ("WORK", "SHORT_BREAK", "LONG_BREAK"):
        return_values['timer_name'] = user_input
    else:
        main_menu()

def timer_reset():
    global seconds
    global timer
    return_values['seconds'] = 0
    return_values['work_count'] = 0
    seconds, timer = 0, ''

def main(timer_name=False, seconds=0): #TODO: Update input agar menjadi a key pressed input instead of a word input.
    global flag
    global timer
    
    main_menu()
    second_reset = False
    while True:
        print(seconds)
        if return_values['timer_name']: 
            timer_name = return_values['timer_name']

        if second_reset:
            user_input = 'start'
        else:
            show_menu(timer_name, 'START_')
            user_input = input("\t\t\tYour Input : ").lower()


        if not return_values['seconds']:
            seconds = globals()[timer_name]
        
        if user_input == 'start':
            second_reset = False
            t1 = Thread(target=pomodoro_timer, args=(timer_name,seconds))
            t2 = Thread(target=pomodoro_input)
            t1.start()
            t2.start()
            t2.join()
            flag = False
            sleep(1)
            if return_values['user_input'] == 'back':
                timer_reset()
                main_menu()
            elif return_values['user_input'] == 'stop':
                if seconds: seconds = return_values['seconds']
            elif return_values['user_input'] == 'start':
                timer_name = return_values['timer_name']
                second_reset = True
            elif return_values['user_input'] == 'settings':
                show_menu('SETTINGS')
                timer_name = return_values['timer_name']
                input('\t\t\tYour Input : ')
            flag = True
        elif user_input == 'settings':
            show_menu('SETTINGS')
            input("\t\t\tYour Input : ").lower()
        elif user_input == 'back':
            timer_reset()
            main_menu()
