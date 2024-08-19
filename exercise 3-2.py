cabin_class = input("please enter the cabin class:\n")
if cabin_class == "LUX":
    print("Your cabin class is upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Your cabin class is above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Your cabin class is windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Your cabin class is windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

