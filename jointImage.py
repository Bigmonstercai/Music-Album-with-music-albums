from quantifyImage import quantifyImage
from PIL import Image
from PIL import ImageFilter
import random
import time


def jointImage(img, imgdict):
    img = quantifyImage(img, 8)
    #img = img.filter(ImageFilter.SMOOTH_MORE)
    netSize = 3
    new_img = Image.new(
        'RGB', (netSize * img.width, netSize * img.height), (255, 255, 255))
    for w in range(img.width):
        for h in range(img.height):
            oriRGB = img.getpixel((w, h))
            # print('begin fillBG:%s' % time.clock())
            new_img = fillBG(
                new_img, netSize * w, netSize * h, netSize, oriRGB)
            # print('end fillBG:%s' % time.clock())
            try:
                components = imgdict[oriRGB]
            except KeyError:
                # print('begin find_nearest:%s' % time.clock())
                components = find_nearest(imgdict, oriRGB)
                # print('end find_nearest:%s' % time.clock())
            c_img = random.sample(components, 1)[0]
            m_img = Image.new('RGB', (c_img.width, c_img.height), oriRGB)
            c_img = Image.blend(c_img.convert('RGB'), m_img, 0.8)
            #print('begin paste:%s' % time.clock())
            if c_img.width >= c_img.height:
                new_img.paste(
                    c_img, (netSize * w, round(netSize * h + (netSize - c_img.height)
                                               / 2)))
            else:
                new_img.paste(
                    c_img, (round(netSize * w + (netSize - c_img.width) / 2), netSize
                            * h))
            # print('end paste:%s' % time.clock())

    return new_img


def fillBG(img, x, y, netSize, RGB):
    img.paste(RGB, (x, y, x + netSize, y + netSize))
    return img


def cal_distance(RGB1, RGB2):
    distance = (RGB1[0] - RGB2[0]) ** 2 + \
        (RGB1[1] - RGB2[1]) ** 2 + (RGB1[2] - RGB2[2]) ** 2
    return distance


def find_nearest(imgdict, RGB):
    min_distance = 3 * (256 ** 2)
    min_RGB = (255, 255, 255)
    for keys in imgdict:
        distance = cal_distance(keys, RGB)
        if(distance < min_distance):
            min_distance = distance
            min_RGB = keys
    return imgdict[min_RGB]
