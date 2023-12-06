import socket
import struct
import matplotlib.pyplot as plt
import matplotlib.image as image
from io import BytesIO


# 接收方
def Receiver():
    group_ip = '224.0.0.251'   #'239.255.255.250'  # 组地址 239.0.0.1
    group_port = 10000  # 端口号
    # 创建IPv4/UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 获取本地ip 先获取主机名，在通过主机名获取ip
    local_ip = socket.gethostbyname(socket.gethostname())
    print(local_ip)
    # 绑定端口
    sock.bind((local_ip, group_port))
    # socket.inet_aton  ip转为二进制
    # socket.INADDR_ANY 所有地址
    mreq = struct.pack("=4sl", socket.inet_aton(group_ip), socket.INADDR_ANY)
    # 加入组播组
    # 使用默认的IPV4组播接口
    print(socket.IPPROTO_IP)
    print(socket.IP_ADD_MEMBERSHIP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print('ok')

    while True:
        plt.clf()  # 清除上一幅图像
        data, addr = sock.recvfrom(655360)  # 接受数值大一点，防止被撑爆
        img = BytesIO(data)
        img = image.imread(img, format='jpeg')
        plt.imshow(img)
        plt.pause(0.05)  # 暂停0.05秒 这一句是实现动态更新的
        plt.ioff()  # 关闭画图的窗口


if __name__ == '__main__':
    Receiver()