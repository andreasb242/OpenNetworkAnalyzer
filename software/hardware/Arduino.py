#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware
from tkinter import messagebox
import serial


## TODO !!!!!!!!
SERIALPORT = "/dev/tty.usbmodem641" # For the Mac
#SERIALPORT = "COM5"
BAUD = 115200

class Arduino(BaseHardware.BaseHardware):
	def __init__(self, settings, model):
		super().__init__(settings, model)

		self.adcValue = 0
		global BAUD
		global SERIALPORT

		try:
			self.serialPort = serial.Serial(SERIALPORT, BAUD, timeout=1)
		except:
			messagebox.showinfo("Serial Error", "Could not open serial Port «" + SERIALPORT + "»")


	# Read a single value, return True to continue, False to stop
	def readValue(self):
		FTW = readings[self.n*2].astype(int).astype(str)+'\n'
		self.serialPort.write(FTW.encode()) 						# Send frequency command

		self.serialPort.write('p\n'.encode())
		self.adcValue = self.serialPort.readline().decode().strip()

		if len(self.adcValue) != 0:
			readings[self.n*2+1] = float(self.adcValue) * .5*0.0488 - 90.5 #0.0488 or 0.1953 - 83.998







