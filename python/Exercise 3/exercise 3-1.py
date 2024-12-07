#main
zander_length = float(input("Enter your fish length (in cm): "))
if zander_length < 42:
    print(f"Your fish is {42-zander_length:.2f} cm short, please release the fish back!")
else:
    print("you can take the fish")