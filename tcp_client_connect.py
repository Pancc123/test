#导入socket 库
from socket import *

#创建一个socket:
s=socket(AF_INET,SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#b'' 转换为bytes类型
buffer=[]
while True:
	#每次最多接受1k字节
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
		
		
data=b''.join(buffer)


s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
#把接受的数据写入文件：
with open('tcp.html','wb') as f:
	f.write(html)