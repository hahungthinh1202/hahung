#main
my_list = []
while True:
    number_string = input("Enter a number to add to list (empty string to exit): ")
    if number_string != "":
        my_list.append(int(number_string))
    elif number_string == "":
        my_list.sort(reverse=True)
        break
print("Five greatest numbers in your list is", my_list[0:5])