import random

secret = random.randint(1, 10)


guess = None

while guess != secret:
    user_input = input("Guess a number between 1 and 10: ")

    # convert to int
    guess = int(user_input)

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! You guessed it!")