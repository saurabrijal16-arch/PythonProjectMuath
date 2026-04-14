numbers = []

while True:
    user_input = input("Enter a number (empty to quit): ")
    if user_input == "":
        break
    numbers.append(int(user_input))

numbers.sort(reverse=True)
print("Five greatest numbers:")
for i in range(min(5, len(numbers))):
    print(numbers[i])