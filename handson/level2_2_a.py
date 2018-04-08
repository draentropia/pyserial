# -*- coding: utf-8 -*-
"""
Created on 8th April 2018
@author: PyLadiesBCN (@PyLadiesBCN), E. Ortega-Carrasco (@draentropia)
"""

"""
Very first hands on Arduino and its connection to Python through PySerial.
Read data from Arduino example.

Ensure that your Arduino board is connected to the right port and has the
level2_2_a project loaded.
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
Read the output from Arduino until the user stops the script
"""
while 1:
	pot = arduino.readline()
	print(pot)
arduino.close()