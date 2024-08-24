def list_remove_odd_number(list):
    remove_list = []
    for i in list:
        if i%2 != 0:
            remove_list.append(i)
    for i in remove_list:
        list.remove(i)
    return list

#main
print("Create list")
my_list = []
while True:
    number = input("Enter list number (enter empty string to exit): ")
    if number == "":
        break
    else:
        my_list.append(int(number))
        
print("Old list:",my_list)
print("New list:",list_remove_odd_number(my_list))