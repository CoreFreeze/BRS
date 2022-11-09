import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

class Client:
    def __init__(self, location, locationIndex):
        self.location = location
        self.locationIndex = locationIndex
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = 2
    
    def connect(self, host, port):
        try:
            self.sock.connect((host, port))
            self.status = 1
        except Exception as err:
            self.bridge.connectError.emit()
            return

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status

    def start(self):
        if self.status == 1:
            self.status = 0
            recieve_thread = threading.Thread(target=self.receive)
            recieve_thread.daemon = True
            recieve_thread.start()

    def getLocationIndex(self):
        return self.locationIndex

    def write(self, message):
        if self.status == 0:
            data=f"{message}"
            self.sock.send(data.encode('utf-8'))

    def stop(self):
        if self.status == 1 or self.status == 0:
            self.status = 2
            self.sock.close()

    def receive(self):
        self.write(self.location+'&')
        while self.status == 0:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                splitMessages = message.split('&')
                if splitMessages[0] == '3':
                    self.bridge2.setSuspendSig.emit()
                elif splitMessages[0] == '2':
                    pass
                elif splitMessages[0] == '1':
                    index = int(splitMessages[1])
                    self.bridge2.setNameSig.emit(index, splitMessages[2])
                    self.bridge2.setReadySig.emit(index, splitMessages[3]=='True')
                elif splitMessages[0] == '0':
                    self.bridge2.setBasicSig.emit(message)
                    self.bridge2.messageSig.emit('서버와 연결되었습니다.')
                else:
                    self.bridge2.messageSig.emit(message)
            except Exception as err:
                self.bridge.connectError.emit()
                self.sock.close()
                break
        
