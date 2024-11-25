
from PIL import Image
import numpy as np

# Define the path to the PNG file
image_path = '1731986947592.png'

# Open the image file using PIL
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

print('Image array shape:', image_array.shape)
str = ''
index = 1
letter = ('-','x')

for i in image_array:
    for j in i:
        tempt = j.tolist()
        if sum(tempt) <=100:
            str += letter[index%2]
        else:
            str += letter[(index+1)%2]
    str += '\n'
    for j in i:
        tempt = j.tolist()
        if sum(tempt) >=100:
            str += letter[index%2]
        else:
            str += letter[(index+1)%2]
    str += '\n'
    index += 1

"""for i in image_array:
    for j in i:
        tempt = j.tolist()
        if tempt == [0,0,0,0]:
            str += '-'
        else:
            str += 'x'
    str += '\n'
"""
print(str)
import matplotlib.pyplot as plt
plt.imshow(image_array)
plt.show()