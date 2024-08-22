i = 1
while True:
    number_string = input("Enter a number: ")
    if i == 1 and number_string != "":
        number_float = float(number_string)
        largest_number = smallest_number = number_float
        i+=1
    elif i == 1 and number_string == "":
        print("No number entered")
        break
    elif i != 1 and number_string == "":
        print("largest number", largest_number)
        print("smallest number", smallest_number)
        break
    else:
        i += 1

    if number_float > largest_number:
        largest_number = number_float
    if number_float < smallest_number:
        smallest_number = number_float




