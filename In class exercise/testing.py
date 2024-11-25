class Alphabet:
    def __init__(self, valuee):
        self._value = valuee

    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value

    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value

    valuee = property(getValue, setValue,delValue)

    @property
    def value(self):
        return self._value


# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

