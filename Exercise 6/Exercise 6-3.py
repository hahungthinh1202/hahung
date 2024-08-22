def gallon_to_litre(i):
    return i*4.54609

while True:
    gal = float(input("Enter volume in gallon you want to convert (negative value to exit): "))
    if(gal<0):
        break
    else:
        print(gal,f"gallons equal {gallon_to_litre(gal):.2f} litre")