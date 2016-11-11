#!/usr/bin
import socket
import time
import mraa

def connect():
    global s
    HOST = '144.214.146.211'  # Symbolic name meaning the local host
    PORT = 4202  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
connect()
ip_address =s.getsockname()[0]

#Uart
# Initialize UART
u=mraa.Uart(0)
# Set UART parameters
u.setBaudRate(115200)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
#u.setFlowcontrol(False, False)

while True:
    data_all = ''
    try:
        data_all = u.readStr(100)
        s.send(data_all)

    except socket.error:
        # s.close()
        while True:
            try:
                connect()
                break
            except socket.error:
                pass
                print 'socket error'
                time.sleep(2)
