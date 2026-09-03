import random

def play_game():
    lucky_number = random.randint(1, 100)
    attempts=0
    max_attempts=6

    while attempts < max_attempts:
        user_number = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_number < lucky_number:
            print("It is smaller than the lucky number")
        elif user_number > lucky_number:
            print("It is greater than the lucky number")
        else:
            print("Congratulations! You guessed the lucky number!")
            break
    else:
        print("You have reached the maximum number of attempts.")
play_game()    