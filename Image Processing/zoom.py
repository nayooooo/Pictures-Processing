import os
from PIL import Image


class ZoomPicts(object):
    """缩放图片"""

    def __init__(self, fileRoute='', saveRoute='', size=1):
        """
        初始化对象
        :param fileRoute: 文件路径
        :param size: 缩放倍数
        """

        self.fileRoute = fileRoute
        self.saveRoute = saveRoute
        self.size = size

    def zoomPicts(self, show=False, save=False):
        """
        缩放图片
        :param show: 是否展示
        :param save: 是否保存
        :return:
        """

        # 解构路径
        fileName = os.path.basename(self.fileRoute)
        # 处理图片
        img = Image.open(self.fileRoute)  # 读取图片
        row, col = img.size
        out = img.resize((row * self.size, col * self.size))
        if show:
            img.show()
        if save:
            out.save(os.path.join(self.saveRoute, fileName))


if __name__ == '__main__':
    picts = ZoomPicts(fileRoute='D:\\code\\Python Program\\Image Processing\\videos\\bailan\\pics\\4.jpg',
                      saveRoute='C:\\Users\\YEWAN\\Desktop',
                      size=10)
    picts.zoomPicts(show=False, save=True)
