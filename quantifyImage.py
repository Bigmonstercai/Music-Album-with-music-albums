from PIL import Image
import math


def quantifyImage(img, newQuan):
        # resize
    if img.height / 7 >= img.width / 13:
        img = img.resize((round(img.width / (img.height / 7)) * 20, 140))
    else:
        img = img.resize((260, round(img.height / (img.width / 13)) * 20))

    for w in range(img.width):
        for h in range(img.height):
            oriValue = img.getpixel((w, h))
            newValue = tuple(map(lambda x: quantify(x, newQuan), oriValue))
            img.putpixel((w, h), newValue)

    return img


def quantify(RGB, numbers=8):
    gap = math.ceil(256 / numbers)
    if (RGB // gap) == (numbers - 1):
        newRGB = (((RGB // gap) * gap + 256) // 2)
    else:
        newRGB = ((RGB // gap) * gap + gap // 2)
    return newRGB

if __name__ == '__main__':
    img = Image.open('images/动画片-brave heart.jpg')
    img1 = quantifyImage(img, 8)
    img.show()
    img.close()
    img1.show()
