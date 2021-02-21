#!/usr/bin/env python
#================================================================
# Write serial command to setup Thermocycle Program on Hitachi
# Author : JudyChen
# Date : Dec09, 2020
#================================================================

import time
import datetime
import serial
import os.path
import string
      
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

def writeCode(command):
    Command = command.upper()
    ser.write(Command+"\r")
    print(ser.readline())

# put Hitachi to setting mode and start setting steps from 1st step
def offset():
    #program setting mode
    writeCode("C3=P")
    #program No.
    writeCode("C4=1")
    writeCode("CE=1")
    
# set onestep of the program
# steptime format 0:00 or 00:00
def oneStep(stepnum, temp, steptime):
    writeCode("C5="+str(stepnum))
    writeCode("C6="+str(temp))
    writeCode("C8="+steptime)


# set cycles
# go : return from step No.go
# to : return to step No.to
def returnStep(go, to, repetition):
    writeCode("C5="+str(go))
    writeCode("C9="+str(to))
    writeCode("CA="+str(repetition))


# read user setting card
open_path = raw_input("Please enter filename of setting card in this dir\nOr the full path of the setting card\nEnter Here : ")
fopen = open(open_path, "r")

stepNum = []
setTemp = []
setTime = []

firstline = fopen.readline()
if firstline != None:
    cycle = firstline.split(",")
    goStep = cycle[1]
    toStep = cycle[2]
    repeat = cycle[3]

    for line in fopen:
        command = line.split(",")[3:]
        
        stepNum.append(command[0] + ",")
        setTemp.append(command[1] + ",")
        setTime.append(command[2] + ",")

    if ser.isOpen():
        offset()
    
        totSteps = stepNum.len()
        for step in range(totSteps):
            if setTime[step].find(":") != None:
                oneStep(stepNum[step], setTemp[step], setTime[step])

        writeCode("CB=2")
        returnStep(goStep, toStep, repeat)
        writeCode("CE=9")
        writeCode("C1=ON")




        
    
