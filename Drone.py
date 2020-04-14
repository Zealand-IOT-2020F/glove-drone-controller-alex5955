import socket
import sys
import time

class Drone(object):

    def __init__(self, ip,port):
        self.TelloIp = ip
        print("ip: " + ip)
        self.TelloPort = port
        
        # Create a UDP socket
        self.Host =""
        self.HostPort = 9000
        self.locaddr = (self.Host,self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.tello_address = ('192.168.10.1', 8889)
        self.tello_address = (ip, port)
        self.sock.bind(self.locaddr)

    def sendCommand(self,TelloMessage):
        # print Command recived
        print("send message "+ TelloMessage +" end")
        msg = TelloMessage.encode(encoding="utf-8")

        # Sends / Recives data from drone
        sent = self.sock.sendto(msg,self.tello_address)
        data, server = self.sock.recvfrom(1518)
        
        # Return data to caller
        print(data.decode(encoding="utf-8"))
        return "from sendmessage " + TelloMessage + " end "

    def connect(self):
        print("Connect")
        result = self.sendCommand("command")
        print (result)

    def takeOff(self):
        self.sendCommand("takeoff")

    def land(self):
        self.sendCommand("land")

    def battery(self):
        bat = self.sendCommand("battery?")
        return bat

    def end(self):
        print("close")
        self.sock.close()
        
    def forward(self, amount):
        self.sendCommand("forward " + str(amount))

    def back(self, amount):
        self.sendCommand("back " + str(amount))

    def rotateCW(self,amount):
        self.sendCommand("cw" + str(amount))

    def rotateCCW(self,amount):
        self.sendCommand("ccw" + str(amount))

    def up(self, amount):
        result = self.sendCommand("up " + str(amount)) 

    def down(self, amount):
        result = self.sendCommand("down " + str(amount)) 

    def printinfo(self):
        print("Hallo Drone at : IP:" + str(self.TelloIp) + " Port: " + str(self.TelloPort))

    def left(self, amount):
        self.sendCommand("left " + str(amount))
    
    def right(self, amount):
        self.sendCommand("right " + str(amount))
