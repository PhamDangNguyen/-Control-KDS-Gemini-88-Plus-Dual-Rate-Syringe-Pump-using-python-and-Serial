import serial
import time

#Setup thong so cho port 
class StartSerial:
    def __init__(self, port):
        self.port = port
    def initializationSerial(self):
        self.ser = serial.Serial(
            port=self.port,
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )
        self.ser.isOpen()
        return self.ser

#tao lop truyen di
class writeSerial:
    def __init__(self,input,ser):
        self.ser = ser
        self.input = input.encode()
    def Write(self):
        self.ser.write(self.input+'\r\n'.encode())#truyen lenh qua port COM
        time.sleep(1)
        return True

#tao lop doc tra ve
class readSerial:
    def __init__(self,ser):
        self.ser = ser
    def Read(self):
        self.out =''
        while self.ser.inWaiting()>0:
            self.out += self.ser.read(1).decode()
        if self.out != '':
            print(self.out)
        return True