

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))
weight_gram = talents*20*32*13.3 + pounds*32*13.3 +lots*13.3
weight_kilo = int(weight_gram/1000)
weight_remainder = weight_gram%1000
print("The weight in modern units:\n",weight_kilo," kilograms and ", f"{weight_remainder:3.2f}"," grams")

