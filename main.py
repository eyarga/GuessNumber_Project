from random import randint


def choose_level():
    level = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()

    while level != 'easy' or level != 'hard':
        if level == 'easy' or level == 'hard':
            break
        level = input(f"The difficulty must be 'easy' or 'hard'. Please retry: ").lower()

    if level == 'easy':
        return 10
    else:
        return 5


def check_answer(user_number, number_to_guess, lives):
    if user_number == number_to_guess:
        print("You guessed the number!")
        return
    elif user_number > number_to_guess:
        print("Too high.")
        print("Guess again.")
        return lives - 1
    else:
        print("Too low.")
        print("Guess again.")
        return lives - 1


def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = randint(1, 100)

    lives = choose_level()
    print("Make sure to guess a number between 1 and 100.")

    user_number = 0
    while number_to_guess != user_number:
        print(f"You have {lives} attempts remaining to guess the number.")

        # Get the user's guess
        while True:
            try:
                user_number = int(input("Make a guess: "))
                while user_number < 1 or user_number > 100:
                    print("The number must be between 1 and 100.")
                    user_number = int(input("Make a guess: "))
                break
            except ValueError:
                print("You must enter a number.")
                continue

        lives = check_answer(user_number, number_to_guess, lives)

        if lives == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {number_to_guess}.")
            return


start_game()
