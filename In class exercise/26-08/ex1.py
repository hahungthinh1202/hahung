#main

letter = input('Enter a letter: ')

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("this is a vowel")
elif letter == "y":
    print("this is sometime a vowel, sometime not")
else:
    print("this is not a vowel")