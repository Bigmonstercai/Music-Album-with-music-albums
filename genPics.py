# -*- coding: utf-8 -*-

import os
from readAPIC import readAPIC

path = 'E:\Bigmonstercai\Music'

for artist in os.listdir(path):
    if os.path.isdir(path + '\\' + artist):
        for album in os.listdir(path + '\\' + artist):
            if os.path.isdir(path + '\\' + artist + '\\' + album):
                i = 0
                while True:
                    try:
                        firstfile = os.listdir(
                            path + '\\' + artist + '\\' + album)[i]
                        filename = path + '\\' + artist + \
                            '\\' + album + '\\' + firstfile
                        filetype = os.path.splitext(firstfile)[1]
                        if readAPIC(filename, artist, album, filetype):
                            break
                        else:
                            i = i + 1
                    except IndexError:
                        print(path + '\\' + artist + '\\' + album)
