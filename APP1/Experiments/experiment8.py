try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    amount = value / total_value * 100
    print(f"{amount}%")

except ValueError:
    print("You neer to enter a number.run the program again")
