#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware
import serial
import traceback


class Arduino(BaseHardware.BaseHardware):
	def __init__(self, settings, model):
		super().__init__(settings, model)

		self.adcValue = 0
		baud = settings['hardware']['arduino.baud']
		serialport = settings['hardware']['arduino.serialport']

		self.serialPort = None
		self.serialPort = serial.Serial(serialport, baud, timeout=1)
		self.lastError = False


	## Read Information from Board
	def readInformation(self, cmd):
		try:
			self.serialPort.write(cmd)
			result = self.serialPort.readline().decode().strip()
			if len(result) > 0:
				if result[:2] != 'O:':
					self.listener.hwUpdateConnectionState('Connected, Error=' + result, True)
					return False
				else:
					result = result[2:]
					data = {}
					for s in result.split(","):
						key, value = s.split('=')
						data[key] = value

					return data
			else:
				return False
					
		except BaseException as e:
			self.listener.hwUpdateConnectionState('Connection lost: ' + str(e), True)
			traceback.print_exc()
			return False


	## Initialize connection
	def initConnection(self):
		for i in range(0, 10):
			values = self.readInformation(b'i\n')
			
			if values == False:
				continue
			
			self.minFrequence = int(values['MINFREQ'])
			self.maxFrequence = int(values['MAXFREQ'])
			self.listener.hwUpdateConnectionState('Board connected')

			values = self.readInformation(b'v\n')
			if values != False:
				self.boardType = values['BOARD']
				self.boardVersion = values['FW']

			return True
		
		return False

	def formatFrequence(self, hz):
		if hz < 1000:
			return str(hz) + 'Hz'

		if hz < 1000000:
			return str(hz / 1000.0) + 'kHz'

		if hz < 1000000000:
			return str(hz / 1000000.0) + 'MHz'


	## Read a single value, return True to continue, False to stop
	def readValue(self):
		if self.serialPort is None:
			return False
		
		try:
			# Send frequency command
			freq = self.model.readings[self.n * 2].astype(int).astype(str)
			command = 'f' + freq + '\n'
			self.serialPort.write(command.encode())
			result = self.serialPort.readline().decode().strip()
		
			if result[:2] != 'O:':
				self.listener.hwUpdateConnectionState('Error setting frequency to ' + freq + ', Error ' + result, True)
				self.lastError = True
				return False

			self.serialPort.write('r\n'.encode())
			result = self.serialPort.readline().decode().strip()
		except BaseException as e:
			self.listener.hwUpdateConnectionState('Connection lost: ' + str(e), True)
			traceback.print_exc()
			return False

		if result[:2] != 'O:':
			self.listener.hwUpdateConnectionState('Error reading Value: ' + result, True)
			self.lastError = True
			return False
		
		self.adcValue = result[2:]

		if len(self.adcValue) != 0:
			#0.0488 or 0.1953 - 83.998
			self.model.readings[self.n * 2 + 1] = float(self.adcValue) * .5 * 0.0488 - 90.5


		if self.lastError == True:
			self.lastError = False
			self.listener.hwUpdateConnectionState('Connected, no error anymore')

		return True




