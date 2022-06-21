import bmp
import os

__name__ = '__main__'


def demo_0(pictureRoute='', folderRoute='', saveRoute='', show=False, save=False):
    """
    将图片转成BMP
    :param pictureRoute: 图片路径
    :param folderRoute: 文件夹路径
    :param saveRoute: 保存路径
    :param show: 是否显示
    :param save: 是否保存
    """

    if pictureRoute != '':
        BMP = bmp.Picture2Bmp(pictureRoute=pictureRoute, saveRoute=saveRoute)
        BMP.picture2Bmp(show=show, save=save)
    if folderRoute != '':
        BMP = bmp.Picture2Bmp(folderRoute=folderRoute, saveRoute=saveRoute)
        BMP.picture2Bmp(show=show, save=save)
    print('demo_1 done')


def demo_1(bmpRoute='', folderRoute='', saveRoute='', flip=False, show=False, save=False):
    """
    将BMP转成黑白图
    :param bmpRoute: BMP路径
    :param folderRoute: 文件夹路径
    :param saveRoute: 保存路径
    :param flip: 是否黑白反转
    :param show: 是否显示
    :param save: 是否保存
    """

    if bmpRoute != '':
        BMP = bmp.Bmp2BWP(bmpRoute=bmpRoute, saveRoute=saveRoute)
        BMP.bmp2BWP(flip=flip, show=show, save=save)
    if folderRoute != '':
        BMP = bmp.Bmp2BWP(folderRoute=folderRoute, saveRoute=saveRoute)
        BMP.bmp2BWP_Folder(flip=flip, show=show, save=save)


def demo_2(bmpRoute='', saveRoute='', row=64, col=128, rowOffset=0, colOffset=0, show=False, save=False):
    """
    裁剪BMP
    :param bmpRoute: BMP路径
    :param saveRoute: 保存路径
    :param row: 裁剪后的行数
    :param col: 裁剪后的列数
    :param rowOffset: 行偏移
    :param colOffset: 列偏移
    :param show: 是否显示
    :param save: 是否保存
    """

    if bmpRoute != '':
        BMP = bmp.CutBmp(bmpRoute=bmpRoute, saveRoute=saveRoute)
        BMP.section(row=row, col=col, rowOffset=rowOffset, colOffset=colOffset, show=show, save=save)


def demo_3(bmpRoute='', saveRoute='', show=False, save=False):
    """
    将黑白图保存成十六进制TXT
    :param bmpRoute: BMP路径
    :param saveRoute: 保存路径
    :param show: 是否显示
    :param save: 是否保存
    """

    if bmpRoute != '':
        BMP = bmp.PrintText(bmpRoute=bmpRoute, saveRoute=saveRoute)
        BMP.printText(show=show, save=save)


def jpeg2Txt(pictureRoute='', folderRoute='', saveRoute='',
             flip=False, row=64, col=128, rowOffset=0, colOffset=0,
             txtPage=8, txtCol=128, txtPageBits=8,
             showEveryStep=False, saveEveryStep=False,
             showBmp=False, showCutBmp=False, showBWP=False, showTxt=False,
             saveBmp=False, saveCutBmp=False, saveBWP=False, saveTxt=False):
    """
    将图片转成TXT
    :param pictureRoute: 原始图片路径
    :param folderRoute: 原始图片所在现在文件夹路径
    :param saveRoute: 最终保存路径
    :param flip: 反转显示
    :param row: 裁剪后的行数
    :param col: 裁剪后的列数
    :param rowOffset: 裁剪时的行偏移
    :param colOffset: 裁剪时的列偏移
    :param txtPage: 页数
    :param txtCol: 列数
    :param txtPageBits: 每一页的位数
    :param showEveryStep: 显示每一次转化
    :param saveEveryStep: 保存每一步转化
    :param showBmp: 显示BMP
    :param showCutBmp: 显示裁剪后的BMP
    :param showBWP: 显示BWP
    :param showTxt: 显示TXT
    :param saveBmp: 保存BMP
    :param saveCutBmp: 保存裁剪后的BMP
    :param saveBWP: 保存BWP
    :param saveTxt: 保存TXT
    :return: TXT路径
    """

    if pictureRoute != '':
        # 图片格式转化
        BMP = bmp.Picture2Bmp(pictureRoute=pictureRoute, saveRoute=saveRoute)
        bmpRoute = BMP.picture2Bmp(show=showEveryStep | showBmp, save=saveEveryStep | saveBmp)
        if bmpRoute is not None:
            print('Picture2Bmp done')
            print('bmpRoute = {0}'.format(bmpRoute))
        else:
            print('Picture2Bmp ERROR')
        # 裁剪BMP
        cutBMP = bmp.CutBmp(bmpRoute=bmpRoute, saveRoute=saveRoute)
        cutBMPRoute = cutBMP.section(row=row, col=col, rowOffset=rowOffset, colOffset=colOffset,
                                     show=showEveryStep | showCutBmp, save=saveEveryStep | saveCutBmp)
        if cutBMPRoute is not None:
            print('CutBmp done')
            print('cutBMPRoute = {0}'.format(cutBMPRoute))
        else:
            print('CutBmp ERROR')
        # BMP转成BWP
        BWP = bmp.Bmp2BWP(bmpRoute=cutBMPRoute, saveRoute=saveRoute)
        BWPRoute = BWP.bmp2BWP(flip=flip, show=showEveryStep | showBWP, save=saveEveryStep | saveBWP)
        if BWPRoute is not None:
            print('Bmp2BWP done')
            print('BWPRoute = {0}'.format(BWPRoute))
        else:
            print('Bmp2BWP ERROR')
        # BWP转成TXT
        TXT = bmp.PrintText(bmpRoute=BWPRoute, saveRoute=saveRoute)
        TXTRoute = TXT.printText(txtCol=txtCol, txtPage=txtPage, txtPageBits=txtPageBits,
                                 show=showEveryStep | showTxt, save=saveEveryStep | saveTxt)
        if TXTRoute is not None:
            print('PrintText done')
            print('TXTRoute = {0}'.format(TXTRoute))
        else:
            print('PrintText ERROR')
        return TXTRoute


def main():

    # demo_0(pictureRoute='D:/Python Program/Image Processing/pictures/可达鸭抱头.jpeg',
    #        saveRoute='D:/Python Program/Image Processing/pictures/processed',
    #        show=True, save=False)
    # demo_1(folderRoute='D:/Python Program/Image Processing/pictures/processed',
    #        saveRoute='D:/Python Program/Image Processing/pictures/processed/BWP',
    #        flip=True, show=True, save=True)
    # demo_2(bmpRoute='D:/Python Program/Image Processing/pictures/processed/BWP/可达鸭抱头.bmp',
    #        saveRoute='D:/Python Program/Image Processing/pictures/processed/BWP/cut',
    #        row=64, col=128, rowOffset=-50, colOffset=-20,
    #        show=True, save=True)
    # demo_3(bmpRoute='D:/Python Program/Image Processing/pictures/processed/BWP/cut/可达鸭抱头.bmp',
    #        saveRoute='D:/Python Program/Image Processing/pictures/processed/BWP/cut/txt',
    #        show=True, save=True)
    jpeg2Txt(pictureRoute='D:/Python Program/Image Processing/pictures/可达鸭斜着（小图）.jpg',
             saveRoute='D:/Python Program/Image Processing/pictures/processed',
             flip=True, row=733, col=700, rowOffset=0, colOffset=0,
             txtPage=91, txtCol=700, txtPageBits=8,
             showEveryStep=False, saveEveryStep=True,
             showBmp=False, showCutBmp=False, showBWP=False, showTxt=False,
             saveBmp=False, saveCutBmp=False, saveBWP=False, saveTxt=False)
    print('Done')
    return


if __name__ == '__main__':
    main()
