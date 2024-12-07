from random import randint

def random_dice():


    return randint(1,6)



#main
while True:
    print("Rolling dice ...")
    result = random_dice() #4 => result =4
    if result == 6:
        print("Result is ",result, "\nEnd program!")
        break
    else:
        print("Result is", result, ". Reroll until 6")



