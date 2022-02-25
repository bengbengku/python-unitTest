def fizzBuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return "Fizz Buzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i


