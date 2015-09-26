from PIL import Image
from quantifyImage import quantify


def imageColor(img, newQuan):
    maxcnt = 0
    mostRGB = (0, 0, 0)
    totalcnt = 0
    totalRGB = (0, 0, 0)
    for count, RGB in img.getcolors(img.size[0] * img.size[1]):
        if len(RGB) == 3:
            r, g, b = RGB
        else:
            r, g, b, a = RGB
        if count > maxcnt:
            maxcnt = count
            mostRGB = (r, g, b)
        totalcnt = totalcnt + count
        totalRGB = (totalRGB[0] + r, totalRGB[1] + g, totalRGB[2] + b)
    aveRGB = (totalRGB[0] / totalcnt, totalRGB[1] /
              totalcnt, totalRGB[2] / totalcnt)
    resRGB = (round(mostRGB[0] * 0.9 + aveRGB[0] * 0.1), round(mostRGB[1]
                                                               * 0.9 + aveRGB[1] * 0.1), round(mostRGB[2] * 0.9 + aveRGB[2] * 0.1))
    resRGB = (quantify(resRGB[0], newQuan), quantify(
        resRGB[1], newQuan), quantify(resRGB[2], newQuan))

    return resRGB


if __name__ == '__main__':
    img = Image.open('images/DJ OKAWARI-Mirror.jpg')
    RGB = imageColor(img)
    img.close()
