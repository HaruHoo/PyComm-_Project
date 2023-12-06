import socket
import tkinter as tk
from tkinter import filedialog

# 文件发送端
sk = socket.socket()
# 定义连接的ip和port
ip_port = ('172.20.10.4', 9999)
# 服务器连接
sk.connect(ip_port)
# 文件上传
# 打开文件
# 获取选择文件路径
root = tk.Tk()
root.withdraw()

# 获取文件夹路径
f_path = filedialog.askopenfilename()
print('\n获取的文件地址：', f_path)

with open(f_path, 'rb') as f:
    # 按每一段分割文件上传
    for i in f:
        sk.send(i)
        # 等待接收完成标志
        data = sk.recv(1024)
        # 判断是否真正接收完成
        if data != b'success':
            break
# 给服务端发送结束信号
sk.send('quit'.encode())