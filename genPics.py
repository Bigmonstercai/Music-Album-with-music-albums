# -*- coding: utf-8 -*-

import os
import shutil
from readAPIC import readAPIC

path = 'E:\Bigmonstercai\Music'

for artist in os.listdir(path):
    if os.path.isdir(path + '\\' + artist):
        for album in os.listdir(path + '\\' + artist):
            if os.path.isdir(path + '\\' + artist + '\\' + album):
                # print((artist + album).encode('utf-8','ignore').decode('GB18030','ignore'))
                # readAPIC(path + '\\' + artist + '\\' + album + '\\' + os.listdir(path + '\\' + artist + '\\' + album)[0], artist, album)
                if os.path.exists(path + '\\' + artist + '\\' + album + '\\folder.jpg'):
                    shutil.copyfile(
                        path + '\\' + artist + '\\' + album + '\\folder.jpg', 'images\\' + artist + '-' + album + '.jpg')
                else:
                    readAPIC(path + '\\' + artist + '\\' + album + '\\' +
                             os.listdir(path + '\\' + artist + '\\' + album)[0], artist, album)
