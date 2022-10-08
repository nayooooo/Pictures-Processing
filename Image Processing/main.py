import os
import bmp
import serials
from time import sleep


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


def video2Pics(videoRoute='', saveRoute=''):
    """
    将mp4转成图片
    :param videoRoute: mp4路径
    :param saveRoute: 保存路径
    :return: 保存路径
    """

    video = bmp.Video2Picture(videoRoute=videoRoute, saveRoute=saveRoute, frameRate=4)
    video.video2Picture()
    return saveRoute


def jpeg2Txt_section(pictureRoute='', folderRoute='', saveRoute='',
                     flip=False, row=64, col=128, rowOffset=0, colOffset=0,
                     startPoint=(0, 0), txtPage=8, txtCol=128, txtPageBits=8,
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
    :param startPoint: 起始取模坐标点，两个分量都大于零
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
        TXTRoute = TXT.printText(startPoint=startPoint, txtCol=txtCol, txtPage=txtPage, txtPageBits=txtPageBits,
                                 show=showEveryStep | showTxt, save=saveEveryStep | saveTxt)
        if TXTRoute is not None:
            print('PrintText done')
            print('TXTRoute = {0}'.format(TXTRoute))
        else:
            print('PrintText ERROR')
        return TXTRoute


def jpeg2Txt_resize(pictureRoute='', folderRoute='', saveRoute='',
                     flip=False, row=64, col=128,
                     startPoint=(0, 0), txtPage=8, txtCol=128, txtPageBits=8,
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
    :param startPoint: 起始取模坐标点，两个分量都大于零
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
        if bmpRoute is None:
            print('Picture2Bmp ERROR')
            return None
        else:
            print('Picture2Bmp done')
            print('bmpRoute = {0}'.format(bmpRoute))
        # 裁剪BMP
        cutBMP = bmp.CutBmp(bmpRoute=bmpRoute, saveRoute=saveRoute)
        cutBMPRoute = cutBMP.resize(row=row, col=col,
                                     show=showEveryStep | showCutBmp, save=saveEveryStep | saveCutBmp)
        if cutBMPRoute is None:
            print('CutBmp ERROR')
            return None
        else:
            print('CutBmp done')
            print('cutBMPRoute = {0}'.format(cutBMPRoute))
        # BMP转成BWP
        BWP = bmp.Bmp2BWP(bmpRoute=cutBMPRoute, saveRoute=saveRoute)
        BWPRoute = BWP.bmp2BWP(flip=flip, show=showEveryStep | showBWP, save=saveEveryStep | saveBWP)
        if BWPRoute is None:
            print('Bmp2BWP ERROR')
            return None
        else:
            print('Bmp2BWP done')
            print('BWPRoute = {0}'.format(BWPRoute))
        # BWP转成TXT
        TXT = bmp.PrintText(bmpRoute=BWPRoute, saveRoute=saveRoute)
        TXTRoute = TXT.printText(startPoint=startPoint, txtCol=txtCol, txtPage=txtPage, txtPageBits=txtPageBits,
                                 show=showEveryStep | showTxt, save=saveEveryStep | saveTxt)
        if TXTRoute is None:
            print('PrintText ERROR')
            return None
        else:
            print('PrintText done')
            print('TXTRoute = {0}'.format(TXTRoute))
        return TXTRoute
    if folderRoute != '':
        # 图片格式转化
        BMP = bmp.Picture2Bmp(folderRoute=folderRoute, saveRoute=saveRoute)
        nextStepRoute, bmpRoute = BMP.pictures2Bmp_Folder(show=showEveryStep | showBmp, save=saveEveryStep | saveBmp)
        if bmpRoute is None:
            print('Picture2Bmp ERROR')
            return None
        else:
            print('Picture2Bmp done')
            print('bmpRoute = {0}'.format(bmpRoute))
        # 裁剪BMP
        cutBMP = bmp.CutBmp(folderRoute=nextStepRoute, saveRoute=saveRoute)
        nextStepRoute, cutBMPRoute = cutBMP.resize_Folder(row=row, col=col,
                                                          show=showEveryStep | showCutBmp, save=saveEveryStep | saveCutBmp)
        if cutBMPRoute is None:
            print('CutBmp ERROR')
            return None
        else:
            print('CutBmp done')
            print('cutBMPRoute = {0}'.format(cutBMPRoute))
        # BMP转成BWP
        BWP = bmp.Bmp2BWP(folderRoute=nextStepRoute, saveRoute=saveRoute)
        nextStepRoute, BWPRoute = BWP.bmp2BWP_Folder(flip=flip,
                                                     show=showEveryStep | showBWP, save=saveEveryStep | saveBWP)
        if BWPRoute is None:
            print('Bmp2BWP ERROR')
            return None
        else:
            print('Bmp2BWP done')
            print('BWPRoute = {0}'.format(BWPRoute))
        # BWP转成TXT
        TXT = bmp.PrintText(folderRoute=nextStepRoute, saveRoute=saveRoute)
        nextStepRoute, TXTRoute = TXT.printText_Folder(startPoint=startPoint,
                                                       txtCol=txtCol, txtPage=txtPage, txtPageBits=txtPageBits,
                                                       show=showEveryStep | showTxt, save=saveEveryStep | saveTxt)
        if TXTRoute is None:
            print('PrintText ERROR')
            return None
        else:
            print('PrintText done')
            print('TXTRoute = {0}'.format(TXTRoute))
        return TXTRoute


def communicationWithSingleChip(fileRoute='', folderRoute='', port='com3', baudrate=115200, bytesize=8, stopbits=1, parity='N'):
    """
    与单片机通信
    :param fileRoute: 文件路径
    :param folderRoute: 文件夹路径
    :param port: 端口号
    :param baudrate: 波特率
    :param bytesize: 字长
    :param stopbits: 停止位
    :param parity: 奇偶校验
    """

    if fileRoute != '':
        txt = open(fileRoute)
        txt_str = txt.read()

        data_list = []
        temp = ''
        recordFlag = 0  # 允许记录标志位
        for i in txt_str:
            if i == 'x' or i == 'X':
                recordFlag = 1
                continue
            if i == ',':
                recordFlag = 0
                data_list.append(temp)
                temp = ''
                continue
            if recordFlag:
                temp += i
        data_tuple = tuple(data_list)

        ser = serials.MySerial(port=port, baudrate=baudrate, bytesize=bytesize, stopbits=stopbits, parity=parity)
        ser.openPort()
        ser.sendBytes(data_tuple)
        ser.closePort()
    if folderRoute != '':
        numsOfPics = 99
        for k in range(numsOfPics):
            fileRoute = os.path.join(folderRoute, (str(k) + '.txt'))

            txt = open(fileRoute)
            txt_str = txt.read()

            data_list = []
            temp = ''
            recordFlag = 0  # 允许记录标志位
            for i in txt_str:
                if i == 'x' or i == 'X':
                    recordFlag = 1
                    continue
                if i == ',':
                    recordFlag = 0
                    data_list.append(temp)
                    temp = ''
                    continue
                if recordFlag:
                    temp += i
            data_tuple = tuple(data_list)

            ser = serials.MySerial(port=port, baudrate=baudrate, bytesize=bytesize, stopbits=stopbits, parity=parity)
            ser.openPort()
            ser.sendBytes(data_tuple)
            ser.closePort()
            print('成功发送第{0}张，剩余{1}张'.format(k, 98-k))
            k += 1
            sleep(0.005)


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
    # video2Pics(videoRoute='D:/code/Python Program/Image Processing/videos/bailan/video.mp4',
    #            saveRoute='D:/code/Python Program/Image Processing/videos/bailan/pics')
    # jpeg2Txt_resize(folderRoute='D:/code/Python Program/Image Processing/videos/bailan/pics',
    #                 saveRoute='D:/code/Python Program/Image Processing/videos/bailan/pics/txt',
    #                 flip=True, row=64, col=128,
    #                 startPoint=(0, 0), txtPage=8, txtCol=128, txtPageBits=8,
    #                 showEveryStep=False, saveEveryStep=True,
    #                 showBmp=False, showCutBmp=False, showBWP=False, showTxt=False,
    #                 saveBmp=False, saveCutBmp=False, saveBWP=False, saveTxt=False)
    # communicationWithSingleChip(folderRoute='D:/Python Program/Image Processing/videos/pics/txt',
    #                             port='com4', baudrate=115200)
    print('Done')
    return


if __name__ == '__main__':
    main()
