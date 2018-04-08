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
Iterate over all colors
"""
red = 0;
green = 0;
blue = 0;
for red in range(0,255,50):
	"""
	Prepare a string to send data to Arduino.
	It contains the tree RGB values sepparated by a comma (standard Arduino input)
	"""
	colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
	"""
	Shows on the screen the color we coded
	"""
	print(colorLED)

	arduino.write(colorLED.encode('ascii')) 
	time.sleep(0.1)

for red in range (255, 0, -50):
	"""
	Prepare a string to send data to Arduino.
	It contains the tree RGB values sepparated by a comma (standard Arduino input)
	"""
	colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
	"""
	Shows on the screen the color we coded
	"""
	print(colorLED)

	arduino.write(colorLED.encode('ascii')) 
	time.sleep(0.1)

for green in range(0,255,50):
	"""
	Prepare a string to send data to Arduino.
	It contains the tree RGB values sepparated by a comma (standard Arduino input)
	"""
	colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
	"""
	Shows on the screen the color we coded
	"""
	print(colorLED)

	arduino.write(colorLED.encode('ascii')) 
	time.sleep(0.1)

for green in range(255,0,-50):
	"""
	Prepare a string to send data to Arduino.
	It contains the tree RGB values sepparated by a comma (standard Arduino input)
	"""
	colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
	"""
	Shows on the screen the color we coded
	"""
	print(colorLED)

	arduino.write(colorLED.encode('ascii')) 
	time.sleep(0.1)

for blue in range(0, 255,50):
	"""
	Prepare a string to send data to Arduino.
	It contains the tree RGB values sepparated by a comma (standard Arduino input)
	"""
	colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
	"""
	Shows on the screen the color we coded
	"""
	print(colorLED)

	arduino.write(colorLED.encode('ascii')) 
	time.sleep(0.1)

for blue in range (255,0,-50):
	"""
	Prepare a string to send data to Arduino.
	It contains the tree RGB values sepparated by a comma (standard Arduino input)
	"""
	colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
	"""
	Shows on the screen the color we coded
	"""
	print(colorLED)
	arduino.write(colorLED.encode('ascii')) 
	time.sleep(0.1)

red = 0
green = 0
blue = 0
"""
Prepare a string to send data to Arduino.
It contains the tree RGB values sepparated by a comma (standard Arduino input)
"""
colorLED = str(red) + ',' + str(green) + ',' + str(blue) + '\n'
"""
Shows on the screen the color we coded
"""
print(colorLED)
arduino.write(colorLED.encode('ascii')) 
time.sleep(0.1)

arduino.close()