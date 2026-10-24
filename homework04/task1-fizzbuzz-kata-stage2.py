for i in range(1, 101):
    is_fizz = i % 3 == 0 or i % 10 == 3 or i // 10 == 3
    is_buzz = i % 5 == 0 or i % 10 == 5 or i // 10 == 5

    if is_fizz and is_buzz:
        print("FizzBuzz")
    elif is_fizz:
        print("Fizz")
    elif is_buzz:
        print("Buzz")
    else:
        print(i)
