
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter your choice: ")

match choice:
    case "1":
        f = float(input("Enter Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print("Celsius:", c)

    case "2":
        c = float(input("Enter Celsius: "))
        f = (c * 9 / 5) + 32
        print("Fahrenheit:", f)

    case _:
        print("Invalid choice!")

