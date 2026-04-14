import random

count = int(input("How many dice do you want to roll? "))
total = 0

for i in range(count):
    roll = random.randint(1, 6)
    print(f"Dice {i + 1}: {roll}")
    total += roll

print(f"Total sum: {total}")