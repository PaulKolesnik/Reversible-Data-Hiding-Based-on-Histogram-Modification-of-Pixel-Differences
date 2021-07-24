from histograma import runHistograma
from PIL import Image

# Decode the data in the image
def decode():
    img = input("Enter image name (with extension): ")
    img = "images/" + img
    image = Image.open(img, 'r')

    data = ''
    imageData = iter(image.getdata())

    while True:
        pixels = [value for value in imageData.__next__()[:3] +
                  imageData.__next__()[:3] +
                  imageData.__next__()[:3]]

        # string of binary data
        binStr = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                binStr += '0'
            else:
                binStr += '1'

        data += chr(int(binStr, 2))

        if data == '':
            return 'No Data Encoded!'

        if pixels[-1] % 2 != 0:
            runHistograma(img)
            return data
