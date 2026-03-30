gender = input("Enter your gender (male/female): ")
hemoglobin = int(input("Enter your hemoglobin level (g/L): "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin is low.")
    elif hemoglobin > 155:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")

elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin is low.")
    elif hemoglobin > 167:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")

else:
    print("Invalid gender.")