import os
from PIL import Image
import sys

CHARACTERS = ".,:'`\;~-_|/=\<+>?)*^(!}{v[I]rcVismYejopWnXtzux17lCFJLT3fSZ2a&@y4GOKMUwAP%k605Ed8Qb9NhBDHRq#g$"
rgb_values = []
ascii_image = []
image = 0

def resize_image():

    width, height = image.size

    new_size = (int(width + (width * 0.4)), height)

    resized_image = image.resize(new_size)
    return resized_image


def calculateCharacter(brightness):
    x = abs(len(CHARACTERS) / 255)
    return round(brightness * x)


def getAverage(r, g, b):
    return (r + g + b) / 3


def readImage():
    """
        Fills a list up with the RGB values of every pixel in the image
    """

    width, height = image.size
    px = image.load()
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


def printImage():
    width, height = image.size
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
                image = Image.open(sys.argv[1])
                image = resize_image()
                readImage()
                setCharacters()
                printImage()
            else:
                print(usage)
        else:
            print("the file you selected does not exist.")
    else:
        print(usage)

"""Resize the image, so it don´t look crushed"""



