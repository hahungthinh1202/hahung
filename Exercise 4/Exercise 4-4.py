from random import randint

#main
number  = randint(1,10)
guess   = 0
while guess != number:
    guess = int(input("Please guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! The number is", number)
    elif guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
