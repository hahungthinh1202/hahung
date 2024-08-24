def price_calculator(diameter, price):
    radius = (diameter / 100) / 2
    return price/(radius*radius*3.14)

#main
d1 = float(input("Enter diameter of first pizze (in cm): "))
p1 = float(input("Enter Price of first pizza (in euro): "))

d2 = float(input("Enter diameter of second pizze (in cm): "))
p2 = float(input("Enter Price of second pizza (in euro): "))

pizza1_price = price_calculator(d1, p1)
pizza2_price = price_calculator(d2, p2)

if pizza1_price > pizza2_price:
    print(f"pizza 2 ({pizza2_price:.2f} euro/m2) is cheaper than pizza 1 ({pizza1_price:.2f} euro/m2) ")
else:
    print(f"pizza 1 ({pizza1_price:.2f} euro/m2) is cheaper than pizza 2 ({pizza2_price:.2f} euro/m2) ")
