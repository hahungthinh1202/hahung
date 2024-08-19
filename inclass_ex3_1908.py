day = int(input("How many times a week do you "
                "eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))

grocery = float(input("How much money do you spend on groceries"
                      "in a week? "))
print("average food expenditure:\n"
      "Daily:"
      f" {(lunch_price * day + grocery)/7:.1f} euros\n"
      "Weekly:"
      f" {(lunch_price * day + grocery):.1f} euros\n"
      )

