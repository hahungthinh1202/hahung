from random import randint
def random_dice():
    return randint(1,6)

while True:
    print("Rolling dice ...")
    result = random_dice()
    if result == 6:
        print("Result is ",result, "\nEnd program!")
        break
    else:
        print("Result is", result, ". Reroll until 6")



