my_list = []
while True:
    number_string = input("Enter a number: ")
    if number_string != "":
        my_list.append(int(number_string))
    elif number_string == "":
        my_list.sort(reverse=True)
        break

print("five greatest numbers is", my_list[0:5])