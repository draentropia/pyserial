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
Define colors in a dictionary
"""
red = {'r':255, 'g':0,'b':0}
green = {'r':0,'g':255,'b':0}
blue = {'r':0,'g':255,'b':0}
white = {'r':255, 'g':255, 'b':255}
"""
Define a dictionary of defined colors
"""
colors = {'red': red, 'green':green, 'blue':blue, 'white':white}
"""
Ask the colors
"""
color = raw_input('Which color?')
"""
Get the r,g,b from dict
"""
r = colors[color]['r']
g = colors[color]['g']
b = colors[color]['b']
"""
Prepare a string to send data to Arduino.
It contains the tree RGB values sepparated by a comma (standard Arduino input)
"""
colorLED = str(r) + ',' + str(g) + ',' + str(b) + '\n'
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