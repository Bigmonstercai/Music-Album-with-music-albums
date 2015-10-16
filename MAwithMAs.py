from PIL import Image
from imageColor import imageColor
from jointImage import jointImage
import os
import random
import pickle
import time
import sys


def gen_dict(path, newQuan=8, netSize=50):
    # 生成目标路径下所有图片的特征色字典，键值为特征RGB, 内容为对应图片的缩略图
    # 缩略图大小为netSize*netSize
    imgdict = {}
    for pic in os.listdir(path):
        img = Image.open(path + pic)
        if img.width >= img.height:
            new_width = netSize
            new_height = round(img.height * netSize / img.width)
        else:
            new_width = round(img.width * netSize / img.height)
            new_height = netSize
        img1 = img.resize((new_width, new_height))
        RGB = imageColor(img1, newQuan)
        if RGB in imgdict:
            imgdict[RGB] = imgdict[RGB] + [img1]
        else:
            imgdict[RGB] = [img1]
        img.close()

    return imgdict


def MAwithMAs():
    # 主函数，先生成资源图像字典，再拼出原图像
    # 若有参数，则拼指定图片，否则拼随机图片
    # 若path、newQuan或netSize修改过，需删掉images.dict重新生成
    # 若拼出来的图片分辨率太低，可增加quantifyImage函数中resize里乘的系数
    print('start:%s' % time.clock())
    path = 'photos/'
    newQuan = 8
    netSize = 50
    alpha = 0.6

    if os.path.exists('images.dict'):
        f = open('images.dict', 'rb')
        imgDict = pickle.load(f)
        f.close()
    else:
        f = open('images.dict', 'wb')
        print('begin gen_dict:%s' % time.clock())
        imgDict = gen_dict(path, newQuan, netSize)
        print('end gen_dict:%s' % time.clock())
        pickle.dump(imgDict, f)
        f.close()

    if len(sys.argv) == 1:
        filelist = os.listdir(path)
        imgpath = random.sample(filelist, 1)[0]
    elif len(sys.argv) == 2:
        imgpath = sys.argv[1]
    else:
        imgpath = sys.argv[1]
        for arg in sys.argv[2:]:
            imgpath = imgpath + ' ' + arg

    img = Image.open(path + imgpath)
    print(imgpath)
    print('begin jointImage:%s' % time.clock())
    result = jointImage(img, imgDict, newQuan, netSize, alpha)
    print('end jointImage:%s' % time.clock())
    result.show()
    img.close()
    result.save('result.jpg')
    print('over:%s' % time.clock())


if __name__ == '__main__':
    MAwithMAs()
