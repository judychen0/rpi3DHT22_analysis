#!/usr/bin/env python
          
      
import time
import serial
import datetime
          
      
ser = serial.Serial(
    
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS,
    xonxoff=False,
    rtscts=False,
    writeTimeout=None,
    dsrdtr=False,
    interCharTimeout=None,
    timeout=0.5
)
      
while 1:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S "))
    command = "C2\r"
    ser.write(command.encode()) #python3
    data = ser.readline()
    decode_data = data.decode("utf-8") 
    print(data)
    time.sleep(9)

    
