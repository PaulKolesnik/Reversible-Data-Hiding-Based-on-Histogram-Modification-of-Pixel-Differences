import PIL
from encode import encode
from PIL import Image

def imageOffset(horizontal_X, vertical_Y):
    img = input("Enter image name(with extension - JPG ONLY): ")
    img = "images/" + img
    image = Image.open(img, 'r')

    a = PIL.ImageChops.offset(image, horizontal_X, vertical_Y)
    a.save('images/imageCropped.jpg')
    print("The cropped image has been saved before encoded.")
    encode("imageCropped.jpg")
