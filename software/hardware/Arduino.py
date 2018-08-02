#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware
import serial

# TODO List serial ports
# python -c "import serial.tools.list_ports;print serial.tools.list_ports.comports()"

class Arduino(BaseHardware.BaseHardware):
	def __init__(self, settings, model):
		super().__init__(settings, model)

		self.adcValue = 0
		baud = settings['hardware']['arduino.baud']
		serialport = settings['hardware']['arduino.serialport']

		self.serialPort = None
		self.serialPort = serial.Serial(serialport, baud, timeout=1)

		self.serialPort.write('i\n'.encode())
		result = self.serialPort.readline().decode().strip()
		
		## TODO Parse min / Max frequency, and check for error!
		print('Arduino Hardware Info: ' + result)


	# Read a single value, return True to continue, False to stop
	def readValue(self):
		if self.serialPort is None:
			return

		# Send frequency command
		freq = self.model.readings[self.n * 2].astype(int).astype(str)
		command = 'f' + freq + '\n'
		self.serialPort.write(command.encode())
		result = self.serialPort.readline().decode().strip()
		
		if result[:2] != 'O:':
			print('Error setting frequency to ' + freq + ', Error ' + result)
			return

		self.serialPort.write('r\n'.encode())
		result = self.serialPort.readline().decode().strip()

		if result[:2] != 'O:':
			print('Error reading Value: ' + result)
			return
		
		self.adcValue = result[2:]

		if len(self.adcValue) != 0:
			#0.0488 or 0.1953 - 83.998
			self.model.readings[self.n * 2 + 1] = float(self.adcValue) * .5*0.0488 - 90.5







