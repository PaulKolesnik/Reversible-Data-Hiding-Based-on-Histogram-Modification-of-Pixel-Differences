from improvements.whiteNoise import removeWhiteNoise
from encode import encode
from decode import decode
from improvements.whiteBackground import encodeToWhiteAreas
from improvements.offsetImage import imageOffset


def main():
    print(":: Welcome to Steganography ::")
    a = 0
    while a != 6:
        a = int(input(
            "\nChoice your action:\n1. Encode\n2. Decode\n3. Crop and encode\n4. Remove white background\n5. Remove white noise\n6. Exit\n"))
        if a == 1:
            encode()
        elif a == 2:
            print("Decoded Word : " + decode())
        elif a == 3:
            imageOffset(1, 1)
        elif a == 4:
            encodeToWhiteAreas()
        elif a == 5:
            removeWhiteNoise()
        elif a == 6:
            print("Good bye!")
            return
        else:
            print("Try Again!\nEnter correct input\n ")


if __name__ == '__main__':
    # Calling main function
    main()
