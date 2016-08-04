import serial
import serial.tools.list_ports as list
from serial.serialutil import SerialException
from threading import Thread

def ports():
    ports_list = list.comports()
    title = "Found " + str(len(ports_list)) + " port"
    if len(ports_list) != 1:
        title += "s"
    title += ":"
    print(title)
    print("")
    for port in ports_list:
        print(port.name)
        print("Path: " + port.device)
        print("Description: " + port.description)
        print("Specs: " + port.description)
        print("")
    return ports_list

def begin(ports_list = None, baud=9600, ending="\n"):
    a = Sermon(ports_list, baud, ending)

class Sermon(object):
    def __init__(self, ports_list, baud, ending):
        serials = []
        if ports_list == None:
            ports_list = ports()
        for port in ports_list:
            if str(port.pid) != "None":
                serials.append(serial.Serial(port.device, baud))
        while True:
            send = input("--> ") + ending
            if send == "":
                continue
            for i in range(len(serials)):
                ser = serials[i]
                if send.strip() == "end\n":
                    for ser in serials:
                        ser.close()
                    break
                pigeon = MessengerPigeon(send, ser)
                pigeon.start()

class MessengerPigeon(Thread):
    def __init__(self, message, serial):
        Thread.__init__(self)
        global response
        self.message = message
        self.serial = serial

    def run(self):

        self.serial.write(bytes(self.message, "ascii"))

        # read response and strip extrenous space and split it
        global response
        response = self.serial.readline().strip().decode("ascii")
        print(response)
