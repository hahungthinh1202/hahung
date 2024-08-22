number = 0
while number >= 0:
    number = float(input("Please enter distance in inches: "))
    if number != 1 and number >=0:
        print(number, "inches equal", number * 2.54, "cm")
    elif number == 1:
        print("1 inch equal 2.54 cm")
    else:
        print("Negative input, script ends!")