from PIL import Image
import numpy as np
from encode import encode



def encodeToWhiteAreas():
    orig_color = (255, 255, 255)
    replacement_color = (254, 254, 254)
    name = input("Enter image name(with extension - JPG ONLY): ")
    img = Image.open("images/" + name).convert('RGB')
    data = np.array(img)
    data[(data == orig_color).all(axis = -1)] = replacement_color
    img2 = Image.fromarray(data, mode='RGB')
    img2.save('images/removedWhiteBackground.jpg')
    print("The removed white background img has been saved.")
    encode("removedWhiteBackground.jpg")
