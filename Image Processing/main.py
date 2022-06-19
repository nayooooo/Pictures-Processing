import bmp

__name__ = '__main__'


def main():
    picture = bmp.PictureToBmp(pictureRoute='D:/Python Program/Image Processing/pictures/可达鸭斜着.jpeg',
                               saveRoute='D:/Python Program/Image Processing/pictures/processed',
                               folderRoute='D:/Python Program/Image Processing/pictures')
    picture.jpegToBmp_Folder()
    print('Done')
    return


if __name__ == '__main__':
    main()
