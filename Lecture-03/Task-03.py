
user_input = input("Enter a number (blank to stop): ")


if user_input != "":
    number = float(user_input)

    smallest = number
    largest  = number

    while True:
        user_input = input("Enter a number (blank to stop): ")

        if user_input == "":
            break

        number = float(user_input)

        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")