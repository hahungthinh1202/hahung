from random import randint
def random_dice(max_value):
    return randint(1, max_value)

max_value = int(input("Enter the maximum value of your dice: "))
while True:
    print("Rolling dice ...")
    result = random_dice(max_value)
    if result == max_value:
        print("Result is ",result, "\nEnd program!")
        break
    else:
        print("Result is", result, ". Reroll until", max_value)
