from PIL import Image
from imageColor import imageColor
from jointImage import jointImage
import os
import random
import pickle
import time
import sys


def gen_dict(path):
    imgdict = {}

    for pic in os.listdir(path):
        img = Image.open(path + pic)
        RGB = imageColor(img, 4)
        img.close()
        if RGB in imgdict:
            imgdict[RGB] = imgdict[RGB] + [pic]
        else:
            imgdict[RGB] = [pic]

    return imgdict

print('start:%s' % time.clock())
path = 'images/'
if os.path.exists('images.dict'):
    f = open('images.dict', 'rb')
    imgDict = pickle.load(f)
    f.close()
else:
    f = open('images.dict', 'wb')
    print('begin gen_dict:%s' % time.clock())
    imgDict = gen_dict(path)
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
result = jointImage(img, imgDict)
print('end jointImage:%s' % time.clock())
img.close()
result.save('result.jpg')
print('over:%s' % time.clock())
result.show()
