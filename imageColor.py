from PIL import Image
from quantifyImage import quantify


def imageColor(img, newQuan):
    # 寻找图片的特征色，采用数量最多的颜色*0.9+平均颜色*0.1
    maxcnt = 0
    mostRGB = (0, 0, 0)
    totalcnt = 0
    totalRGB = (0, 0, 0)
    for count, RGB in img.getcolors(img.size[0] * img.size[1]):
        if type(RGB) == int:
            if RGB == 0:
                r, g, b = 255, 255, 255
            else:
                r, g, b = 0, 0, 0
        elif len(RGB) == 3:
            r, g, b = RGB
        else:
            r, g, b, a = RGB
        if count > maxcnt:
            maxcnt = count
            mostRGB = (r, g, b)
        totalcnt = totalcnt + count
        totalRGB = (totalRGB[0] + r, totalRGB[1] + g, totalRGB[2] + b)
    aveRGB = list(map(lambda x: x / totalcnt, totalRGB))
    resRGB = list(map(lambda x, y: x * 0.9 + y * 0.1, mostRGB, aveRGB))
    resRGB = tuple(map(lambda x: quantify(x, newQuan), resRGB))

    return resRGB


if __name__ == '__main__':
    img = Image.open('images/DJ OKAWARI-Mirror.jpg')
    RGB = imageColor(img)
    img.close()
