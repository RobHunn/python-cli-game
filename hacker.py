from PIL import Image, ImageDraw, ImageFont
import math
import argparse

parser = argparse.ArgumentParser(
    description="Turn any photo into ascii art from the Command Line."
)
parser.add_argument(
    "image", type=str, help="The image to convert to ascii art. Required."
)
parser.add_argument(
    "--output",
    type=str,
    help='The name of the file to save the png and text output. Eg - img1. Optional (default is "output")',
)

args = {k: v for k, v in vars(parser.parse_args()).items() if v != None}

# This file i got from:  Raphson
# https://www.youtube.com/watch?v=2fZBLPk-T2Y&list=LL19PJgf0W2Eq6lV-QVnDt2A&index=3&t=917s
# did some minor tweaks...
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength / 256

scaleFactor = 0.09

oneCharWidth = 10
oneCharHeight = 18


def getChar(inputInt):
    return charArray[math.floor(inputInt * interval)]


def ascii_art(image=None, output="output", output_txt="output"):
    if not image:
        return
    text_file = open(f"{output}.txt", "w")

    im = Image.open(image)
    # You may have to chage this line to a font on your system too work this is my relative path
    fnt = ImageFont.truetype("arial.ttf", 15)

    width, height = im.size
    im = im.resize(
        (
            int(scaleFactor * width),
            int(scaleFactor * height * (oneCharWidth / oneCharHeight)),
        ),
        Image.NEAREST,
    )
    width, height = im.size
    pix = im.load()

    outputImage = Image.new(
        "RGB", (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0)
    )
    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text(
                (j * oneCharWidth, i * oneCharHeight),
                getChar(h),
                font=fnt,
                fill=(r, g, b),
            )

        text_file.write("\n")

    outputImage.save(f"{output}.png")


if __name__ == "__main__":
    ascii_art(**args)
