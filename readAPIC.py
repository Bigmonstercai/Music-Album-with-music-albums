def readAPIC(filename, artist, album):
    fp = open(filename, 'rb')
    valid = 0
    pic = []

    while True:
        print(filename, artist, album)
        a = fp.read(2)
        print(a)
        if valid == 0:
            if a == b'\xFF\xD8':
                valid = 1
                pic.append(a)
            elif a == '':
                break
        elif valid == 1:
            pic.append(a)
            if a == b'\xFF\xD9':
                valid = 0
                break
            elif a == '':
                valid = 0
                break

    fp.close

    if pic == []:
        return False
    else:
        fo = open('images\\' + artist + '-' + album + '.jpg', 'wb')
        for i in pic:
            fo.write(i)
        fo.close
        return True
