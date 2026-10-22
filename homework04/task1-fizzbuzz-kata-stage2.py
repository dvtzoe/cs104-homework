for i in range(1, 101):
    is_fizz = False
    is_buzz = False

    if i % 3 == 0 or i % 10 == 3 or i // 10 == 3:
        is_fizz = True
    if i % 5 == 0 or i % 10 == 5 or i // 10 == 5:
        is_buzz = True

    if is_fizz and is_buzz:
        print("FizzBuzz")
    elif is_fizz:
        print("Fizz")
    elif is_buzz:
        print("Buzz")
    else:
        print(i)
