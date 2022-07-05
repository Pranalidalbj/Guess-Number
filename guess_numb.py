"""
Guessing Numbers in Python using try except
"""

import random

# x = 0
# num_of_guess = 1
print("Number of Guesses is limited to 9.")


def start_game():
    x = 0
    num_of_guess = 1
    try:
        # global num_of_guess, x
        # num_of_guess = 1
        # global x
        while num_of_guess <= 9:
            x = random.randint(0, 20)

            guessed_num = int(input("Guess the number: \n"))

            if guessed_num < x:
                print("You Entered less than the actual number. ")
            elif guessed_num > x:
                print("You Entered greater than the actual number. ")
            elif guessed_num == x:
                print("You Won. Congrats!!!!")
                print(f"{num_of_guess} no. of guesses you took to finish")
                break
            else:
                print("Please Enter Number within range!!!!")

            print(f"{9 - num_of_guess} no. of guesses is left to Finish.")
            num_of_guess = num_of_guess + 1




    except Exception as e:
        print("Invalid Input")
    finally:
        if num_of_guess > 9:
            print(f"The actual number was {x}")
            print("Game Over, You Lost")


if __name__ == '__main__':
    start_game()
    play_it_again = input("Would you like to Play it again('Enter Y/N'):")
    if play_it_again == 'Y' or play_it_again == 'y':
        start_game()
    elif play_it_again == 'N' or play_it_again == 'n':
        print(" Thank You for playing:) ")
    else:
        print("Wrong Input")
