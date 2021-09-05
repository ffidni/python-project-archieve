from time import sleep
from threading import Thread
from os import system
import random
import keyboard


class Game:

    def __init__(self):
        self.ROCKET = '-'
        self.BALL = '*'
        self.HEIGHT,self.WIDTH = 20,50
        self.rocket_x, self.rocket_y = 25, 18
        self.ball_x, self.ball_y = 25, 1
        self.flag = True
        self.map = []

    def map_generator(self):
        for i in range(self.HEIGHT): 
            if i == 0:
                self.map.append(['_' for i in range(self.WIDTH)])
            elif i == 19:
                self.map.append(['_' if i != 0 and i != self.WIDTH-1 else '|' for i in range(50)])
            else:
                self.map.append([' ' if i != 0 and i != self.WIDTH-1 else '|' for i in range(50)])
    
    def display_screen(self):
        CLEAR()
        for i in self.map:
            print(''.join(i))

        print(f"Rocket Pos: ({self.rocket_x}, {self.rocket_y}) Ball Pos: ({self.ball_x}, {self.ball_y})")
        
    def entity_generator(self):
        self.map[self.ball_y][self.ball_x] = self.BALL
        self.map[self.rocket_y][self.rocket_x] = self.ROCKET

    def ball_movement(self):
        """TODO: 
        1. Add random ball spawn.
        2. Add diagonal ball movement."""
        con = '+'
        while self.flag:
            sleep(0.4)
            if con == '+':
                if self.map[self.ball_y+1][self.ball_x] == ' ': 
                    self.map[self.ball_y][self.ball_x] = ' '
                    self.ball_y += 1
            else:
                if self.map[self.ball_y-1][self.ball_x] == ' ':
                    self.map[self.ball_y][self.ball_x] = ' '
                    self.ball_y -= 1
            self.map[self.ball_y][self.ball_x] = self.BALL

            if self.map[self.ball_y+1][self.ball_x] == self.ROCKET:
                con = '-'
            elif self.map[self.ball_y-1][self.ball_x] == '_':
                con = '+'
            elif self.map[self.ball_y+1][self.ball_x] == '_':
                break


    def rocket_movement(self):
        while self.flag:
            temp_x,temp_y = self.rocket_x, self.rocket_y
            if keyboard.is_pressed('left'):
                if self.map[temp_y][temp_x-1] != '|':
                    self.map[temp_y][temp_x] = ' '
                    self.rocket_x -= 1
            elif keyboard.is_pressed('right'):
                if self.map[temp_y][temp_x+1] != '|':
                    self.map[temp_y][temp_x] = ' '
                    self.rocket_x += 1

            self.map[self.rocket_y][self.rocket_x] = self.ROCKET
            sleep(0.08)

    def start_thread(self):
        t1 = Thread(target=game.rocket_movement)
        t2 = Thread(target=game.ball_movement)
        t3 = Thread(target=game.main)
        t1.start()
        t2.start()
        t3.start()
        t2.join()
        self.flag = False

    
    def main(self):
        game.map_generator()
        game.entity_generator()
        while self.flag:
            game.display_screen()
            sleep(0.03)
        print("Game Over!")
        


if __name__ == '__main__':
    CLEAR = lambda: system('cls')
    game = Game()
    game.start_thread()