import random

def roll_die():
    return random.randint(1, 6)

while True:
    result = roll_die()
    print(result)
    if result == 6:
        break