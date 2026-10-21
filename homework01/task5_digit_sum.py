number = int(input("Enter a 3-digit number: "))
digit_sum = number // 100 + (number % 100) // 10 + number % 10
print(f"Digit sum: {digit_sum}")
