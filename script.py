import random


def guess_number():
    guess_range: int = int(input("How big is your guessing range? "))

    random_number: int = random.randint(1, guess_range)

    guess: int = int(input(f"Now guess the random number between 1 and {guess_range}! "))

    if guess > random_number:
        print("Smaller!")

    elif guess < random_number:
        print("Bigger!")

    else:
        print(f"You are right! The number was {random_number}")

if __name__ == "__main__":
    guess_number()
    pass