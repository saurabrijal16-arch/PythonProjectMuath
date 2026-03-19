import random

digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
code3 = str(digit1) + str(digit2) + str(digit3)


digit4 = random.randint(1, 6)
digit5 = random.randint(1, 6)
digit6 = random.randint(1, 6)
digit7 = random.randint(1, 6)
code4 = str(digit4) + str(digit5) + str(digit6) + str(digit7)

# Print codes
print("3-digit code (0-9):", code3)
print("4-digit code (1-6):", code4)