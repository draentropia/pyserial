# -*- coding: utf-8 -*-
"""
Created on 8th April 2018
@author: PyLadiesBCN (@PyLadiesBCN), E. Ortega-Carrasco (@draentropia)
"""

"""
Very first hands on Arduino and its connection to Python through PySerial.
Write data to Arduino example.

Ensure that your Arduino board is connected to the right port and has the
ledRGB_writeData project loaded.
"""

"""
Importing library "serial" from PySerial (pip install pyserial),
and library time (already installed).
"""
import serial, time
"""
Instanciate "arduino" variable as PySerial object
"""
arduino = serial.Serial('COM3', 9600)

"""
Let some time to the board to connect (2seconds)
"""
time.sleep(2)
"""
Ask the colors
"""
red = raw_input('Red color (from 0 to 255):')
try:
	int(red)
except ValueError:
	print "the value has to be an integer"
	exit()
if (red>255 or red<0):
	print 'value has to be between 0 and 255'
	exit()
	
green = raw_input('Green color (from 0 to 255):')
try:
	int(green)
except ValueError:
	print "the value has to be an integer"
	exit()
if (green>255 or green<0):
	print 'value has to be between 0 and 255'
	exit()

blue = raw_input('Blue color (from 0 to 255):')
try:
	int(blue)
except ValueError:
	print "the value has to be an integer"
	exit()
if (blue>255 or blue<0):
	print 'value has to be between 0 and 255'
	exit()
"""
Prepare a string to send data to Arduino.
It contains the tree RGB values sepparated by a comma (standard Arduino input)
"""
colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
"""
Shows on the screen the color we coded
"""
print(colorLED)
"""
Write chosen color to the serial port in ascii codification
and closes the connection
"""
arduino.write(colorLED.encode('ascii')) 
arduino.close()