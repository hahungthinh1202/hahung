

number_float = largest_number = smallest_number = 0
while True:
    number_string = input("Enter a number: ")
    if number_string == "": #next state exit
        print("largest number", largest_number)
        print("smallest number", smallest_number)
        break
    else:   #next state
        number_float = float(number_string)
        if number_float > largest_number:
            largest_number = number_float
        if number_float < smallest_number:
            smallest_number = number_float