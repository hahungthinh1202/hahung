from random import randint

#main
attempt = int(input("How many time you want to roll the dice: "))
sum = 0
for i in range(1,attempt+1):
    i = randint(1,6)
    sum += i
print("The sum of", attempt, "dices is", sum)