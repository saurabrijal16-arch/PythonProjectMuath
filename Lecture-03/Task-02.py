INCH_TO_CM = 2.54

inches = float(input("Enter inches (negative number to stop): "))

while inches >= 0:
    centimeters = inches * INCH_TO_CM
    print(inches, "inches =", centimeters, "cm")

    inches = float(input("Enter inches (negative number to stop): "))