
airports = {}

while True:
    print("\n1 = Enter new airport")
    print("2 = Get airport info")
    print("3 = Quit")

    choice = input("Choose: ")

    if choice == "1":
        # Add new airport
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":
        # Get airport by ICAO code
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")