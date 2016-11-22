import socket
import time
import mraa


HOST = '144.214.146.211'
PORT = 4202


def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            return s
        except socket.error:
            print 'socket error'
            time.sleep(2)


def get_u():
    u=mraa.Uart(0)
    u.setBaudRate(115200)
    u.setMode(8, mraa.UART_PARITY_NONE, 1)
    return u


def read_and_send(s, u):
    while True:
        try:
            data_all = u.readStr(100)
            s.send(data_all)
        except:
            s = connect()


if __name__ == "__main__":
    s = connect()
    u = get_u()
    read_and_send(s, u)
