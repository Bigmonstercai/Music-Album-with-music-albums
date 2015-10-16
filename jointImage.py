from quantifyImage import quantifyImage
from PIL import Image
from PIL import ImageFilter
import random


def jointImage(img, imgdict, newQuan=8, netSize=50, alpha=0.6):
    # 拼接图像函数，输入为待拼接图像(img)，资源图像字典(imgdict)，
    # 量化级数(newQuan)，网格大小(netSize)和透明度(alpha)
    # 首先将源图像量化为长宽各为源图像大小的1/netSize，RGB三个通道各有newQuan种颜色
    # 新图片与源图像大小相同，划分为若干网格，每个网格大小为netSize*netSize
    # 然后对每一个网格，先填充量化图像对应像素点的颜色
    # 接下来在资源图像字典中寻找特征颜色与该像素点颜色最接近的图片
    # 最后将该图片与背景色按照透明度混合(该图片透明度为alpha)
    img = quantifyImage(img, newQuan, netSize)
    # img = img.filter(ImageFilter.SMOOTH_MORE) # 对于比较复杂的图像，可以先加滤镜镜像模糊
    new_width = netSize * img.width
    new_height = netSize * img.height
    new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))

    for w in range(img.width):
        for h in range(img.height):
            oriRGB = img.getpixel((w, h))
            new_width = netSize * w
            new_height = netSize * h
            new_img = fillBG(new_img, new_width, new_height, netSize, oriRGB)

            try:
                components = imgdict[oriRGB]
            except KeyError:
                components = find_nearest(imgdict, oriRGB)

            c_img = random.sample(components, 1)[0]
            m_img = Image.new('RGB', (c_img.width, c_img.height), oriRGB)
            c_img = Image.blend(c_img.convert('RGB'), m_img, alpha)

            if c_img.width >= c_img.height:
                new_x = new_width
                new_y = round(new_height + (netSize - c_img.height) / 2)
            else:
                new_x = round(new_width + (netSize - c_img.width) / 2)
                new_y = new_height

            new_img.paste(c_img, (new_x, new_y))

    return new_img


def fillBG(img, x, y, netSize, RGB):
    # 对输入图像对(x,y)为左上角，大小为netSize*netSize的区域以RGB填充
    img.paste(RGB, (x, y, x + netSize, y + netSize))
    return img


def cal_distance(RGB1, RGB2):
    # 计算两个颜色之间的欧几里得距离
    delta_R = RGB1[0] - RGB2[0]
    delta_G = RGB1[1] - RGB2[1]
    delta_B = RGB1[2] - RGB2[2]
    distance = delta_R ** 2 + delta_G ** 2 + delta_B ** 2
    return distance


def find_nearest(imgdict, RGB):
    # 找到资源图像字典中键值与给定RGB颜色最接近的项
    min_distance = 3 * (256 ** 2)
    min_RGB = (255, 255, 255)
    for keys in imgdict:
        distance = cal_distance(keys, RGB)
        if(distance < min_distance):
            min_distance = distance
            min_RGB = keys
    return imgdict[min_RGB]
