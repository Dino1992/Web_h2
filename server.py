import socket as s
import os.path

bind_address =('localhost',8000)
SizeOfBuffer = 2048
httpOK = """HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n"""

if __name__ == "__main__":
    socket = s.socket()
    socket.bind(bind_address)
    socket.listen(10)
    while True:
        c,a = socket.accept()
        buff = c.recv(SizeOfBuffer)
        filePath = ''
       
        res = buff.split('\n')[0].split(' ')[1]
        filePath = './' + res  
        if not os.path.isfile(filePath):
            filePath ='./index.html' 

        fd = open(filePath,'r')
        fileContent = httpOK + fd.read()
        c.send(fileContent)
        fd.close()
        c.close()
    socket.close()
            
