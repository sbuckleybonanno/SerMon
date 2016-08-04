import serial
import serial.tools.list_ports as list
from serial.serialutil import SerialException
from threading import Thread

def ports():
    print("Found:")
    ports_list = list.comports()
    for port in ports_list:
        print(port.device)
    return ports_list

def foo():
    return None

def begin(port, baud=9600, ending="\n"):
    a = Sermon(port, baud, ending)

class Sermon(object):
    def __init__(self, port, baud, ending):
        self.ser = serial.Serial(port, baud)
        while True:
            send = input("")
            if send == "quit":
                break
            self.serial.write(bytes(send, "ascii"))
            response = self.serial.readline().strip().decode("ascii")
            print(response)
