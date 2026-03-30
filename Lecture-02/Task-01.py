length = int(input("Enter the length of the zander in centimeters: "))

if length < 42:
    print("Release the zander back into the lake!")
    print("The fish is", 42 - length, "centimeters short of the legal limit.")
else:
    print("You can keep the zander!")