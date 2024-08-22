from math import sqrt
number = int(input("what number do you want to prime check? "))
upper_limit = int(sqrt(number))
for i in range(2,upper_limit+1):
    if number % i == 0:
        print(number,"is not prime!")
        break
    elif i == upper_limit:
        print(number, "is prime")
        break
    else:
        i += 1
