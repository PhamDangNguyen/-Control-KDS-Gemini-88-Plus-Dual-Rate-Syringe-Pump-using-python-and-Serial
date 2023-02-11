
# Assuming that PySerial is installed:

import serial
import time

# Configure serial connection
ser = serial.Serial()
ser.port='COM1'
ser.baudrate=9600
ser.parity=serial.PARITY_ODD
ser.stopbits=serial.STOPBITS_TWO
ser.bytesize=serial.SEVENBITS
ser.isOpen()

input = 'run'
out = ''

# Send the input to the device
# Note the carriage return and line feed characters \r\n will depend on the device
ser.write(input + '\r\n')

# Wait 1 sec before reading output
time.sleep(1)
while ser.inWaiting() > 0:
    out += ser.read(1)

# Print the response
if out != '':
    print(out)