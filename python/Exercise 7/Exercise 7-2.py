#main
my_list = set()
while True:
    name = input("Enter a name to add to set (empty string to exit): ")
    if name != "":
        if name in my_list:
            print("Existing name")
        else:
            print("New name")
            my_list.add(name)
    else:
        break
print("Set of name: ")
for item in my_list:
    print(item)