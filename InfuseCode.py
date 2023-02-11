import serial
import time
import realSerial
import realSerial2
input = 'condition Independent'
port = 'COM3'
# ser = realSerial2.StartSerial(port).initializationSerial()
# realSerial2.writeSerial(input,ser).Write()
ser = realSerial.StartSerial(port).initializationSerial()
realSerial.writeSerial(input,ser).Write()#gui lenh di
realSerial.readSerial(ser=ser).Read() # co nhu cau doc thong tin phan hoi thi bat lenh nay len
