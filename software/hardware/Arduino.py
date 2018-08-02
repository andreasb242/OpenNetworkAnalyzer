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


	# Read a single value, return True to continue, False to stop
	def readValue(self):
		if self.serialPort is None:
			return

		FTW = readings[self.n * 2].astype(int).astype(str) + '\n'

		# Send frequency command
		self.serialPort.write(FTW.encode())

		self.serialPort.write('p\n'.encode())
		
		self.adcValue = self.serialPort.readline().decode().strip()

		if len(self.adcValue) != 0:
			#0.0488 or 0.1953 - 83.998
			self.model.readings[self.n * 2 + 1] = float(self.adcValue) * .5*0.0488 - 90.5







