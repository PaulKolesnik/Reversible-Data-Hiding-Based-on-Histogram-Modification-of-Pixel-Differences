import cv2 as cv
import cv2
from PIL import Image
from histograma import runHistograma


def removeWhiteNoise():
    img = input("Enter image name(with extension - JPG ONLY): ")
    img = "images/" + img
    runHistograma(img)

    Image.open(img, 'r')
    img1 = cv.imread(img, cv.IMREAD_GRAYSCALE)
    output = cv.medianBlur(img1, 3)
    print("Close Images To Continue")
    cv.imshow("input", img1)
    cv.imshow("output", output)
    cv.waitKey(0)
    saveImageName = input("Enter the name of new image(with extension): ")
    saveImageName = "images/" + saveImageName
    cv2.imwrite(saveImageName, output)
