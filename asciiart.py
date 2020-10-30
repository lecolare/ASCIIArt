import os
from PIL import Image
import sys

CHARACTERS = ".,:'`\;~-_|/=\<+>?)*^(!}{v[I]rcVismYejopWnXtzux17lCFJLT3fSZ2a&@y4GOKMUwAP%k605Ed8Qb9NhBDHRq#g$"
rgb_values = []
ascii_image = []

"""Resize the image, so it dont look crushed"""


def resize_image(input_image_path):
    original_image = Image.open(input_image_path)
    width, height = original_image.size

    new_size = (600, height)

    resized_image = original_image.resize(new_size)
    return resized_image


def calculateCharacter(brightness):
    x = abs(len(CHARACTERS) / 255)
    return round(brightness * x)


def getAverage(r, g, b):
    return (r + g + b) / 3


def readImage(path):
    """
        Fills a list up with the RGB values of every pixel in the image
    """

    img = resize_image(path)
    width, height = img.size
    px = img.load()
    for y in range(height):
        for x in range(width):
            # print(x, "", y)
            rgb_values.append(px[x, y])


def setCharacters():
    """
    Iterate over the image's rgb values and calculate their character and add it to the list

    """
    for pixel in rgb_values:
        ascii_image.append(CHARACTERS[calculateCharacter(getAverage(pixel[0], pixel[1], pixel[2])) - 1])


def printImage(path):
    img = resize_image(path)
    width, height = img.size
    count = 1
    for i in ascii_image:
        if count % width == 0:  # After every x-line print a line-break
            print(i, end='\n')
            count = 0
        else:
            print(i, end='')
        count = count + 1


usage = "Wrong Usage! \n Usage: asciiart.py <filePath> -<light/dark>\n   The 2nd option is to specify your terminal " \
        "background color so it will print correctly "
if __name__ == '__main__':

    arguments = len(sys.argv) - 1
    if arguments == 2:
        if os.path.isfile(sys.argv[1]):
            if sys.argv[2] == "-light" or sys.argv[2] == "-dark":
                if sys.argv[2] == "-light":
                    CHARACTERS = CHARACTERS[::-1]
                readImage(sys.argv[1])
                setCharacters()
                printImage(sys.argv[1])
            else:
                print(usage)
        else:
            print("the file you selected does not exist.")
    else:
        print(usage)
