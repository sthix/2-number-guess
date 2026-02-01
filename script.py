import random


def guess_number():
    correctly_answer: bool = False
    number_of_guesses: int = 0

    print("GUESS THE NUMBER!")
    guess_range: int = int(input("How big is your guessing range? "))

    random_number: int = random.randint(1, guess_range)

    guess: int = int(input(f"Now guess the random number between 1 and {guess_range}! "))

    while random_number != guess & correctly_answer == False:
        if guess > random_number:
            number_of_guesses += 1
            print("Smaller!")
            guess: int = int(input("Guess again! "))

        elif guess < random_number:
            number_of_guesses += 1
            print("Bigger!")
            guess: int = int(input("Guess again! "))

        else:
            number_of_guesses += 1
            print(f"You are right. The number was {random_number}!\n"
                  f"You needed {number_of_guesses} guesses.")
            correctly_answer = True


if __name__ == "__main__":
    guess_number()
    pass