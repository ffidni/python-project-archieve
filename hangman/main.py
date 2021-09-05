from os import system
from time import sleep
from random import randint
from json import load

CLEAR = lambda: system('cls')

def get_word():
    with open('words.json') as f:
        return load(f)['words'][randint(0,2466)].upper()

def main():
    word = get_word()
    hidden_word = ['_' for i in range(len(word))]
    misses_word = []
    life = 5
    while ''.join(hidden_word) != word and life > 0:
        CLEAR()
        print("Life : {}".format(life))
        print(' '.join(hidden_word))
        print('Misses: {}'.format(','.join(misses_word)))
        user_input = input("Please input a letter from A-Z : ").upper()
        word_indices = [i for i,j in enumerate(word) if j == user_input]
        if user_input:
            if user_input in word and user_input not in hidden_word:
                print("Correct!")
                if len(word_indices) > 1:                    
                    for i in word_indices:
                        hidden_word[i] = user_input
                else:
                    hidden_word[word_indices[0]] = user_input

            else:   
                if user_input not in misses_word:
                    life -= 1
                    print("Incorrect! You have {} lifes left.".format(life))
                    misses_word.append(user_input)
                    
        else:
            print("Please input a valid letter.")
        sleep(0.8)

    if life != 0:
        print("Congratulations! You won the game.") 
    else:
        print("You have lost the game!")
        
    print("The answer is {}".format(word))
    user_input = input("Play Again? (Y / N) : ").lower()
    if user_input == 'y':
        main()
    
if __name__ == '__main__':
    main()