digit_sum = 0
number = int(input("Number: "))

while number != 0:
    digit_sum += number % 10
    number //= 10

print(f"Digit sum: {digit_sum}")
