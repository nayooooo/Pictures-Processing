import serial
from time import sleep


class MySerial(object):
    """自己的串口类"""

    def __init__(self, port='com3', baudrate=115200, bytesize=8, stopbits=1, parity='N'):
        """
        对串口的参数进行配置
        :param port: 端口号
        :param baudrate: 波特率
        :param bytesize: 字长
        :param stopbits: 停止位
        :param parity: 奇偶校验
        """

        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.parity = parity
        self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesize,
                                 stopbits=self.stopbits, parity=self.parity)

    def __del__(self):
        pass

    def openPort(self):
        """对串口的参数进行配置"""

        if not self.ser.isOpen():
            self.ser.open()
        if self.ser.isOpen():  # isOpen()函数来查看串口的开闭状态
            print("串口打开成功！")
        else:
            print("串口打开失败！")

    def closePort(self):
        if self.ser.isOpen():
            self.ser.close()
        if self.ser.isOpen():
            print("串口关闭失败！")
        else:
            print("串口关闭成功！")

    def sendByte(self, send_data):
        """
        发送一个send_data
        :param send_data: 发送缓冲区
        """

        if self.ser.isOpen():
            self.ser.write(send_data.encode('utf-8'))  # 编码
            print("发送成功", send_data)
        else:
            print("串口未打开！")

    def sendBytes(self, buff: tuple):
        """
        发送任意长度的数组，大小为Byte
        :param buff: 发送缓冲区
        """

        if self.ser.isOpen():
            for i in range(len(buff)):
                if len(buff[i]) < 2:
                    temp = bytes.fromhex('0' + buff[i])
                else:
                    temp = bytes.fromhex(buff[i])
                self.ser.write(temp)
                print("发送成功", buff[i])
        else:
            print("串口未打开！")


if __name__ == '__main__':
    # data = list('0X80')
    # data = ''.join(data[2:])
    # print(bytes.fromhex(data))
    print('Done')
