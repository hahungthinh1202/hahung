from random import randint


print("your 3-digit code combinations is: ", randint(100,999))

a = randint(1,6)
b = randint(1,6)
c = randint(1,6)
d = randint(1,6)

four_digit_combinations = a*1000+b*100+c*10+d

print("your 4-digit code combinations is: ", four_digit_combinations)

