#!/usr/bin/env python]        
      
import time
import datetime
import serial
import os.path
      
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
#ser.close()
#ser.open()

def writeCode(command):
    Command = command.upper()
    ser.write(Command+"\r".encode())
    print(ser.readline())
    
def offset():
    #program setting mode
    writeCode("C3=P")
    writeCode("CE=1")
    #program No.
    writeCode("C4=1")

#steptime format 0:00 or 00:00
def oneStep(stepnum, temp, steptime):
    writeCode("C5="+str(stepnum))
    writeCode("C6="+str(temp))
    writeCode("C8="+steptime)

# go : return from step No.go
# to : return to step No.to
def returnStep(go, to, repetition):
    writeCode("C5="+str(go))
    writeCode("C9="+str(to))
    writeCode("CA="+str(repetition))

### Start of command script ###
if ser.isOpen():
    
    # put in setting mode
    offset()

    # define steps
    writeCode("C1=OFF")
    
### End of command script ###
