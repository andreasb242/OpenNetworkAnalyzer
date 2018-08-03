#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware
import serial


class Arduino(BaseHardware.BaseHardware):
	def __init__(self, settings, model):
		super().__init__(settings, model)

		self.adcValue = 0
		baud = settings['hardware']['arduino.baud']
		serialport = settings['hardware']['arduino.serialport']

		self.serialPort = None
		self.serialPort = serial.Serial(serialport, baud, timeout=1)
		self.lastError = False


	# Initialize connection
	def initConnection(self):
		for i in range(0, 10):
			self.serialPort.write(b'i\n')
			result = self.serialPort.readline().decode().strip()
			
			if len(result) > 0:
				if result[:2] != 'O:':
					self.connectCallback('Connected, Error=' + result)
					return False
				else:
					result = result[2:]
					for s in result.split(","):
						key, value = s.split('=')
						
						if key == 'MINFREQ':
							self.minFrequence = int(value)
						if key == 'MAXFREQ':
							self.maxFrequence = int(value)

					self.connectCallback('Connected, min frequency: ' + str(self.minFrequence) + 'Hz, max frequency: ' + str(self.maxFrequence) + 'Hz')
					return True
		
		return False


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
			self.connectCallback('Error setting frequency to ' + freq + ', Error ' + result)
			self.lastError = True
			return

		self.serialPort.write('r\n'.encode())
		result = self.serialPort.readline().decode().strip()

		if result[:2] != 'O:':
			self.connectCallback('Error reading Value: ' + result)
			self.lastError = True
			return
		
		self.adcValue = result[2:]

		if len(self.adcValue) != 0:
			#0.0488 or 0.1953 - 83.998
			self.model.readings[self.n * 2 + 1] = float(self.adcValue) * .5*0.0488 - 90.5


		if self.lastError == True:
			self.lastError = False
			self.connectCallback('Connected, no error anymore')





