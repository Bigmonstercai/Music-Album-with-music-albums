from PIL import Image
import math


def quantifyImage(img, newQuan=8, netSize=50):
    # 重新量化图片，输入Image对象(img)、新的量化级数(newQuan)、网格大小(netSize)，返回量化好的Image对象
    # 新的图片长宽各为原图片大小的1/netSize，RGB三个通道各有newQuan种颜色
    img = img.resize((round(img.width * 5 / netSize), round(img.height * 5 / netSize)))

    for w in range(img.width):
        for h in range(img.height):
            oriValue = img.getpixel((w, h))
            # 利用map对oriValue的三个通道同时做量化
            newValue = tuple(map(lambda x: quantify(x, newQuan), oriValue))
            img.putpixel((w, h), newValue)

    return img


def quantify(RGB, levels=8):
    # 对输入的RGB值进行量化，将256均匀分成levels组，最高组间隔可能较小，每组量化值取该组中值
    gap = math.ceil(256 / levels)
    if (RGB // gap) == (levels - 1):
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
