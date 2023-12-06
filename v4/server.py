import socket
import time
import win32api, win32con
from PIL import ImageGrab
from io import BytesIO
import tkinter


# 发送方
def Sender():
    group_ip = '224.0.0.251'     #'239.255.255.250'
    group_port = 10000
    # 创建IPv4/UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 获取当前分辨率下的屏幕尺寸
    win = tkinter.Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    #width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    #height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    # 压缩时，大小变为一半
    w = width // 2
    h = height // 2
    while True:
        # 截屏 bbox=None表示截取全屏
        img = ImageGrab.grab(bbox=None)
        #img = ImageGrab.grab(bbox=(0, 0, width, height))
        img.thumbnail((w, h))
        # 图像压缩
        output_buffer = BytesIO()  # 建立二进制对象,在内存中读写
        # RGB格式压缩为JPEG格 式,quality: 保存图像的质量,1(最差)~100
        img.save(output_buffer, format='JPEG', quality=80)
        frame = output_buffer.getvalue()  # 获取二进制数据
        #print(len(frame))
        # 发送文件
        sock.sendto(frame, (group_ip, group_port))
        #sock.send(frame, (group_ip, group_port))
        time.sleep(0.05)  # 加点延时更稳定。


if __name__ == "__main__":
    Sender()