def readAPIC(filename, artist, album, filetype):
    fp = open(filename, 'rb')
    if filetype == '.m4a':
        covr = b'\x63\x6F\x76\x72'
    elif filetype == '.mp3':
        covr = b'ID3'
    else:
        return False
    imagetype = '.png'
    start = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'  # 默认为png,因为png的文件头长，误匹配到的概率低
    end = b'\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82'
    a = fp.read()
    covr_num = a.find(covr)
    a = a[covr_num: -1]
    start_num = a.find(start)
    end_num = a.find(end)
    if start_num == -1:  # 不为png则为jpg
        start = b'\xFF\xD8'
        end = b'\xFF\xD9'
        start_num = a.find(start)
        end_num = a.find(end)
        imagetype = '.jpg'

    if imagetype == '.jpg':
        pic = a[start_num: end_num + 2]
        while pic[2: -1].find(start) != -1:
            pic = pic[pic[2: -1].find(start) + 2:-1]
    elif imagetype == '.png':
        pic = a[start_num: end_num + 12]
        while pic[8: -1].find(start) != -1:
            pic = pic[pic[8: -1].find(start) + 8:-1]

    fo = open('images/' + artist + '-' + album + imagetype, 'wb')
    fo.write(pic)

    fp.close()
    fo.close()
    return True
