import random
import getpass

LIFE = 3

def computer_guess():
    global LIFE

    print("Welcome to the game!\nTo play, simply just input a number and computer/friend will try to guess it.\
           \nThe computer itself has 3 life, if it guess it wrong the life will be shorten, otherwise they will win!")

    num = int(input("Input the number: "))
    guessNum = [i for i in range(1,num+1)]
    l,r = 0, len(guessNum) - 1

    while LIFE > 0:
        mid = l + (r - l) // 2
        feedback = input(f"Is {guessNum[mid]} too high? / too low? / or correct?: ").lower()

        if feedback == 'high':
            LIFE -= 1
            r = mid - 1
            print(f"Incorrect! Computer's live is now shorten to {LIFE}.")
        elif feedback == 'low':
            LIFE -= 1
            l = mid + 1
            print(f"Incorrect! Computer's live is now shorten to {LIFE}.")
        else:
            return f"The computer guessed it correctly!, {num} is the answer!."
    
    return f"Incorrect! Computer's life shorten to 0 which mean computer has lost."

def guess():
    global LIFE

    print("Welcome to the game!\nTo play, simply just input a number and your friend will try to guess it.\
           \nYour friend has 3 life, if they guess it wrong the life will be shorten, otherwise they will win!")

    num = int(getpass.getpass("Input the number to guess: "))
    guess = int(input("A Player has entered the number\nInput your guess: "))
    
    while True:
        if LIFE == 0:
            return "Incorrect! Your friend has lost!"
        elif guess > num:
            print(f"Incorrect! Friend's life shorten to {LIFE}")
            guess = int(input("Too high! Guess another number: "))
            LIFE -= 1
        elif guess < num:
            print(f"Incorrect! Friend's life shorten to {LIFE}")
            guess = int(input("Too low! Guess another number: "))
            LIFE -= 1
        else:
            return f"Congratulations! You guessed it corretcly. The answer is {num}"


if __name__ == '__main__':
    menu = input("Welcome to Guessing Number!\nWhat do u wanna play?\nPlay Against Bot (b) or Play Against Your Friend! (f): ")
    if menu == 'b':
        print(computer_guess())
    else:
        print(guess())
