#!/usr/bin/python
#========================================================
# Write serial command to setup Thermocycle Program on Hitachi
# Program step  1cycle
# 20C To -40C cycle

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
    Command = command+"\r"
    ser.write(Command.encode())
    data = ser.readline()
    print(data.decode("utf-8"))
    
def offset():
    #program setting mode
    writeCode("C3=P")
    #program No.
    writeCode("C4=1")
    writeCode("CE=1")

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
    oneStep(1, 20, "3:00")
    oneStep(2, 0, "0:20")
    oneStep(3, 0, "0:10")
    oneStep(4, 0, "3:00")
    oneStep(5, -20, "0:20")
    oneStep(6, -20, "0:10")
    oneStep(7, -40, "0:20")
    oneStep(8, -40, "3:00")
    oneStep(9, -20, "0:10")
    oneStep(10, -20, "3:00")
    oneStep(11, 0, "0:10")
    oneStep(12, 0, "3:00")
    oneStep(13, 20, "0:10")
    oneStep(14, 20, "99:00")
    writeCode("CB=2")
    writeCode("C1=ON")
    writeCode("C2")
    
### End of command script ###

