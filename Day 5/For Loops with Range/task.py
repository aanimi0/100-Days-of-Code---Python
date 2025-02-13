
rangeLimit = range(1,101)

total = 0
for number in rangeLimit:
    total += number
print(total)

for number in rangeLimit:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print(number)

