import os
from PIL import Image


class PictureToBmp(object):
    """将PNG转成BMP"""

    def __init__(self, pictureRoute="", pictureFormat="", folderRoute='', saveRoute=''):
        """
        初始化对象
        :param pictureRoute: 原始图片位置
        :param pictureFormat: 图片格式
        """

        self.pictureRoute = pictureRoute
        self.pictureFormat = pictureFormat
        self.folderRoute = folderRoute
        self.saveRoute = saveRoute

    def __del__(self):
        pass

    def jpegToBmp(self):
        """将JPEG转成BMP"""

        if self.pictureRoute != '':
            if os.path.splitext(self.pictureRoute)[1] == '.jpeg':
                originalFileRoute = self.pictureRoute
                originalFileRoute_list = list(originalFileRoute)

                # 得到图片名字
                dirIndex = []
                for i in range(len(originalFileRoute)):
                    if originalFileRoute_list[i] == '/':
                        dirIndex.append(i)
                dirPointIndex = []
                for i in range(len(originalFileRoute)):
                    if originalFileRoute_list[i] == '.':
                        dirPointIndex.append(i)
                name = originalFileRoute_list[dirIndex[-1]+1:dirPointIndex[-1]]
                name = ''.join(name)

                img = Image.open(self.pictureRoute)
                img.save(self.saveRoute+'/'+name+'.bmp')

    def jpegToBmp_Folder(self):
        """将文件夹中的JPEG转成BMP"""

        if self.folderRoute != '':
            for name in os.listdir(self.folderRoute):
                if os.path.splitext(name)[1] == '.jpeg':
                    # 得到图片名字
                    name_list = list(name)
                    dirPointIndex = []
                    for i in range(len(name)):
                        if name_list[i] == '.':
                            dirPointIndex.append(i)
                    name = name_list[0:dirPointIndex[-1]]
                    name = ''.join(name)

                    img = Image.open(self.folderRoute+'/'+name+'.jpeg')
                    img.save(self.saveRoute+'/'+name+'.bmp')


if __name__ == '__main__':
    pass
