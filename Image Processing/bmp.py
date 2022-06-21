import os
import numpy as np
from PIL import Image
import matplotlib.image as mpimg


class Picture2Bmp(object):
    """将PNG转成BMP"""

    def __init__(self, pictureRoute="", folderRoute='', saveRoute=''):
        """
        初始化对象
        :param pictureRoute: 原始图片位置
        :param folderRoute: 文件夹路径
        :param saveRoute: 保存路径
        """

        self.pictureRoute = pictureRoute
        self.folderRoute = folderRoute
        self.saveRoute = saveRoute

    def __del__(self):
        pass

    def picture2Bmp(self, show=False, save=False):
        """
        将JPG转成BMP
        :param show: 是否显示
        :param save: 是否保存
        :return: 保存的BMP的路径
        """

        if self.pictureRoute != '':
            # 得到图片原始名字
            originalFillName = os.path.basename(self.pictureRoute)

            # 得到图片名字
            originalFillName_list = list(originalFillName)
            dirPointIndex = []
            for i in range(len(originalFillName_list)):
                if originalFillName_list[i] == '.':
                    dirPointIndex.append(i)
            originalFillName_list = originalFillName_list[:dirPointIndex[-1]]
            name = ''.join(originalFillName_list)

            img = Image.open(self.pictureRoute)
            if show:
                img.show()
            if save:
                bmpRoute = os.path.join(self.saveRoute, (name + '.bmp'))
                img.save(bmpRoute)
                return bmpRoute

        else:
            print('Picture2Bmp.jpg2Bmp ERROR 0')
            return None

    def pictures2Bmp_Folder(self, show=False, save=False):
        """
        将文件夹中的JPG转成BMP
        :param show: 是否显示
        :param save: 是否保存
        :return: 保存的BMP的路径（列表）
        """

        if self.folderRoute != '':
            saveRoute = []
            saveRouteIndex = 0
            for name in os.listdir(self.folderRoute):
                fileSuffix = os.path.splitext(name)[1]

                # 当文件有后缀名时
                if fileSuffix != '':
                    # 得到图片名字
                    name_list = list(name)
                    dirPointIndex = []
                    for i in range(len(name)):
                        if name_list[i] == '.':
                            dirPointIndex.append(i)
                    name_list = name_list[:dirPointIndex[-1]]
                    name = ''.join(name_list)

                    img = Image.open(os.path.join(self.folderRoute, (name + fileSuffix)))
                    if show:
                        img.show()
                    if save:
                        saveRoute.append(os.path.join(self.saveRoute, (name + '.bmp')))
                        img.save(saveRoute[saveRouteIndex])
                        saveRouteIndex += 1
                else:
                    print('Picture2Bmp.pictures2Bmp_Folder ERROR 1')
                    continue
            return saveRoute
        else:
            print('Picture2Bmp.pictures2Bmp_Folder ERROR 0')
            return None


class CutBmp(object):
    """裁剪BMP"""

    def __init__(self, bmpRoute='', folderRoute='', saveRoute=''):
        """
        初始化对象
        :param bmpRoute: BMP路径
        :param folderRoute: 文件夹路径
        :param saveRoute: 保存路径
        """

        self.bmpRoute = bmpRoute
        self.folderRoute = folderRoute
        self.saveRoute = saveRoute

    def __del__(self):
        pass

    def section(self, row, col, rowOffset, colOffset, show=False, save=False):
        """
        使用切片法将BMP图像裁剪为合适的大小
        :param row: 切片后行数
        :param col: 切片后列数
        :param rowOffset: 行偏移，取行正向为正
        :param colOffset: 列偏移，取列正向为正
        :param show: 是否显示
        :param save: 是否保存
        :return: 保存的BMP的路径
        """

        bmp_mat = mpimg.imread(self.bmpRoute)
        bmpRow = bmp_mat.shape[0]
        bmpCol = bmp_mat.shape[1]

        # 判断是否适合裁剪，若适合，则进行裁剪
        if (bmpRow >= row + abs(rowOffset)) and (bmpCol >= col + abs(colOffset)):
            rowCutFor = (bmpRow + 1 - row) // 2 + rowOffset
            colCutFor = (bmpCol + 1 - col) // 2 + colOffset
            newBmp_mat = bmp_mat[rowCutFor:rowCutFor + row, colCutFor:colCutFor + col]
        else:
            print('CutBmp.section ERROR 0')
            return None

        # 显示与保存
        newBmp_mat = Image.fromarray(newBmp_mat)
        if show:
            newBmp_mat.show()
        if save:
            saveRoute = os.path.join(self.saveRoute, os.path.basename(self.bmpRoute))
            newBmp_mat.save(saveRoute)
            return saveRoute


class Bmp2BWP(object):
    """将BMP转成黑白图"""

    def __init__(self, bmpRoute="", folderRoute='', saveRoute=''):
        """
        初始化对象
        :param bmpRoute: 原始图片位置
        :param folderRoute: 文件夹路径
        :param saveRoute: 保存路径
        """

        self.bmpRoute = bmpRoute
        self.folderRoute = folderRoute
        self.saveRoute = saveRoute

    def __del__(self):
        pass

    def bmp2BWP(self, flip=False, show=False, save=False):
        """
        将BMP转成黑白图
        :param flip: 是否黑白反转
        :param show: 是否显示
        :param save: 是否保存
        :return: 保存的BWP的路径
        """

        if self.bmpRoute != '':
            bmp_mat = mpimg.imread(self.bmpRoute)
            bmpRow = bmp_mat.shape[0]
            bmpCol = bmp_mat.shape[1]

            # 将图片处理成极黑极白
            for i in range(bmpRow):
                for j in range(bmpCol):
                    temp = 0
                    for k in range(3):
                        temp += bmp_mat[i, j][k]
                    temp /= 3
                    if temp > 128:
                        if flip:
                            bmp_mat[i, j] = [0, 0, 0]
                        else:
                            bmp_mat[i, j] = [255, 255, 255]
                    else:
                        if flip:
                            bmp_mat[i, j] = [255, 255, 255]
                        else:
                            bmp_mat[i, j] = [0, 0, 0]

            bmp_mat = Image.fromarray(bmp_mat)
            bmp_mat = bmp_mat.convert('L')  # 转成黑白图
            if show:
                bmp_mat.show()
            if save:
                saveRoute = os.path.join(self.saveRoute, os.path.basename(self.bmpRoute))
                bmp_mat.save(saveRoute)
                return saveRoute
        else:
            print('Bmp2BWP.bmp2BWP ERROR 0')
            return None

    def bmp2BWP_Folder(self, flip=False, show=False, save=False):
        """
        将BMP转成黑白图
        :param flip: 是否黑白反转
        :param show: 是否显示
        :param save: 是否保存
        :return: 保存的BWP的路径（列表）
        """

        if self.folderRoute != '':
            saveRoute = []
            saveRouteIndex = 0
            for name in os.listdir(self.folderRoute):
                fileSuffix = os.path.splitext(name)[1]

                if fileSuffix != '':
                    bmp_mat = mpimg.imread(os.path.join(self.folderRoute, name))
                    bmpRow = bmp_mat.shape[0]
                    bmpCol = bmp_mat.shape[1]

                    # 将图片处理成极黑极白
                    for i in range(bmpRow):
                        for j in range(bmpCol):
                            temp = 0
                            for k in range(3):
                                temp += bmp_mat[i, j][k]
                            temp /= 3
                            if temp > 128:
                                if flip:
                                    bmp_mat[i, j] = [0, 0, 0]
                                else:
                                    bmp_mat[i, j] = [255, 255, 255]
                            else:
                                if flip:
                                    bmp_mat[i, j] = [255, 255, 255]
                                else:
                                    bmp_mat[i, j] = [0, 0, 0]

                    bmp_mat = Image.fromarray(bmp_mat)
                    bmp_mat = bmp_mat.convert('L')  # 转成黑白图
                    if show:
                        bmp_mat.show()
                    if save:
                        saveRoute.append(os.path.join(self.saveRoute, name))
                        bmp_mat.save(saveRoute[saveRouteIndex])
                        saveRouteIndex += 1

                else:
                    print('Bmp2BWP.bmp2BWP_Folder ERROR 1')
                    continue
            return saveRoute
        else:
            print('Bmp2BWP.bmp2BWP_Folder ERROR 0')
            return None


class PrintText(object):
    """将黑白图输出成文本"""

    def __init__(self, bmpRoute='', saveRoute=''):
        """
        初始化对象
        :param bmpRoute: BMP路径
        :param saveRoute: 保存路径
        """

        self.bmpRoute = bmpRoute
        self.saveRoute = saveRoute

    def __del__(self):
        pass

    def printText(self, startPoint=(0, 0), txtPage=8, txtCol=128, txtPageBits=8, show=False, save=False):
        """
        将黑白图输出成十六进制文本
        :param startPoint: 起始取模坐标点，两个分量都大于零
        :param txtPage: 生成的TXT的页数
        :param txtCol: 生成的TXT的列数
        :param txtPageBits: 生成的TXT的每一页的位数
        :param show: 是否显示
        :param save: 是否保存
        :return: 保存的TXT的路径
        """

        if (startPoint[0] < 0) or (startPoint[1] < 0):
            print('PrintText.printText ERROR 3')
            return None

        if self.bmpRoute != '':
            fileSuffix = os.path.splitext(self.bmpRoute)[1]
            if fileSuffix != '':
                text = np.mat(np.random.randint(0, 1, (txtCol, txtPage)))  # 这个矩阵为了适合OLED，应竖着看
                bmp_mat = mpimg.imread(self.bmpRoute)
                bmpRow = bmp_mat.shape[0]
                bmpCol = bmp_mat.shape[1]

                if ((bmpRow < txtPage * txtPageBits + startPoint[1])
                        or (bmpCol < txtCol + startPoint[0])):
                    print('PrintText.printText ERROR 2')
                    return None

                # 计算得到对应的OLED图片数组
                for i in range(txtCol):  # 列
                    for j in range(txtPage):  # 页
                        for k in range(txtPageBits):  # 位
                            text[i, j] <<= 1
                            if bmp_mat[j*txtPageBits+k+startPoint[0], i+startPoint[1]] > 0:
                                text[i, j] += 1

                # 得到文件名字
                name = os.path.basename(self.bmpRoute)
                name_list = list(name)
                dirPointIndex = []
                for i in range(len(name_list)):
                    if name_list[i] == '.':
                        dirPointIndex.append(i)
                bmpName_list = name_list[:dirPointIndex[-1]]
                name = ''.join(bmpName_list)

                if show:
                    print(text)
                if save:
                    text = np.array(text)
                    saveRoute = os.path.join(self.saveRoute, (name + '.txt'))
                    np.savetxt(fname=saveRoute, X=text, fmt='\t0X%X',
                               delimiter=',', newline=',\n',
                               header='{', footer='\r}', comments='')
                    return saveRoute

            else:
                print('PrintText.printText ERROR 1')
                return None

        else:
            print('PrintText.printText ERROR 0')
            return None


if __name__ == '__main__':
    point = (1, 2)

    print(point, point[0], point[1])
