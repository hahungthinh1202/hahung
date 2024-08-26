class complex_number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def sum_number(self, x, y):
        return x + y
#main
x = complex_number(1,2)
print(x.real)
print(x.sum_number(4,6))