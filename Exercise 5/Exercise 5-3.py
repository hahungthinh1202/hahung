from math import sqrt

#main
number = int(input("what number do you want to prime check? "))
upper_limit = int(sqrt(number))
if number == 1:
    print("not prime")
else:
    for i in range(2,upper_limit+1):
        if number % i == 0:
            print(number,"is not prime!")
            break
        elif i == upper_limit:
            print(number, "is prime")
            break


