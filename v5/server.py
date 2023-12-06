import socket

# 文件接收端
sk = socket.socket()
# 定义连接的ip和port
ip_port = ('172.20.10.4', 9999)
# 绑定端口
sk.bind(ip_port)
# 最大连接数
sk.listen(5)
# 进入循环接收数据
conn, address = sk.accept()
print("文件接收开始")
while True:
    with open('file', 'ab') as f:
        # 接收数据
        data = conn.recv(1024)
        if data == b'quit':
            break
        # 写入文件
        f.write(data)
        # 接受完成标志
        conn.send('success'.encode())
print("文件接收完成")
# 关闭连接
sk.close()