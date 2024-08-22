def list_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print("Create list")
my_list = []
while True:
    number = input("Enter list number (enter empty string to exit): ")
    if number == "":
        break
    else:
        my_list.append(int(number))

print("The sum of your list is",list_sum(my_list))
