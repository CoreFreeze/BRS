import datetime
import socketserver
import threading
from time import sleep

HOST = '127.0.0.1'
PORT = 9090

class chatTCPHandler(socketserver.BaseRequestHandler):
    casterList = None
    running = None

    def setup(self) -> None:
        chatTCPHandler.running = True
        self.server.addClients(self)
        return super().setup()

    def finish(self) -> None:
        self.server.removeClients(self)
        return super().finish()

    def broadcast(self, message):
        print(message)
        self.server.broadcast(message)

    def handle(self):
        try:
            message = self.request.recv(1024).decode('utf-8')
        except:
            return

        currentLocation = str(message).split('&')

        if currentLocation[0] == message:
            return
        
        self.server.addLocation(self, currentLocation[0])
        
        self.request.send(self.getBasicInfo().encode('utf-8'))
        
        while chatTCPHandler.running:
            try:
                message = self.request.recv(1024).decode('utf-8')
                print(message)
                # 서버에 표시
                splitedMessage = message.split('&')
                if splitedMessage[0] == '1':
                    self.setMessageUI(splitedMessage[1:])
                    sendMessage = message
                else:
                    sendMessage = message
                    self.server.bridge.messageSig.emit(sendMessage)
                self.broadcast(sendMessage)
            except NameError:
                # clinet 종료 시 recv 에러 발생
                #print('{self.client_address[0]} got an error {e}')
                break
            except Exception as err:
                #print(err)
                break

    def getBasicInfo(self):
        basicInfo = ['0']

        for index, user in enumerate(self.server.present_user):
            basicInfo.append(user)
            basicInfo.append(str(self.server.present_ready[index]))

        nameList = []
        for caster in chatTCPHandler.casterList:
            if caster != '' or caster is None:
                nameList.append(caster)

        basicInfo.append(str(len(nameList)))
        basicInfo = basicInfo + nameList

        message = '&'.join(basicInfo)
        
        return message

    def setMessageUI(self, message):
        index = int(message[0])
        self.server.present_user[index] = message[1]
        self.server.present_ready[index] = message[2] == 'True'
        self.server.bridge.setReadySig.emit(index, self.server.present_ready[index])
        self.server.bridge.setNameSig.emit(index, message[1])

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    request_queue_size = 15
    daemon_threads = True

    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass,True)
        self.clients = []
        self.locations = {}
        self.present_user = ['','','']
        self.present_ready = [False,False,False]
        thread = threading.Thread(target=self.timeChecker)
        thread.daemon = True
        thread.start()

    def setLocationList(self, locationList):
        self.locationList = locationList

    def addClients(self, client):
        self.clients.append(client)

    def addLocation(self, clientAddress,location):
        self.locations[clientAddress]=location
        #print(self.locations)

    def removeClients(self, client):
        self.clients.remove(client)
        location = self.locations.pop(client, '')
        #print(self.locations)
        if location != '':
            self.leaveChatMessage(location)

    def broadcast(self, message):
        data = message.encode('utf-8')
        for client in self.clients:
            try:
                client.request.send(data)
            except Exception as err:
                #print(err)
                pass

    def leaveChatMessage(self, location):
        op = ['1']
        if location == self.locationList[0]:
            index = 0
        elif location == self.locationList[1]:
            index = 1
        elif location == self.locationList[2]:
            index = 2
        else:
            return
        op.append(str(index))
        op.append('- - -')
        op.append(str(False))
        self.present_ready[index] = False
        self.present_user[index] = ''
        self.bridge.setReadySig.emit(index, False)
        self.bridge.setNameSig.emit(index, '')

        self.broadcast('&'.join(op))

    def timeChecker(self):
        while True:
            min = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            if min == 17 or min == 32 or min == 47 or min == 59:
                if sec == 0 or sec == 3:
                    self.broadcast('3&')
                    for index in range(0,3):
                        self.present_ready[index] = False
                        self.bridge.setReadySig.emit(index, False)
            sleep(1)