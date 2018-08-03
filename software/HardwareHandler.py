#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import Arduino
from hardware import Dummy
from hardware import NoHardware

from tkinter import messagebox

class HardwareHandler(object):
	def __init__(self, settings, model):
		self.settings = settings
		self.model = model
		self.hardware = None


	def start(self, listener):
		self.listener = listener
		self.hardware.start(listener)		
		

	def getHwImplementationNames(self):
		return ('None', 'Random values', 'Arduino')


	def hasSerial(self, index):
		if index == 2:
			return True
		else:
			return False


	def getImplementationNameByIndex(self, index):
		if index == 1:
			return 'dummy'
		elif index == 2:
			return 'arduino'
		else:
			return 'none'


	def selectImplementationByIndex(self, index):
		self.settings['hardware']['type'] = self.getImplementationNameByIndex(index)

		self.stop()
		self.loadHardware()
		self.hardware.start(self.listener)


	def getSelectedHwImplementationIndex(self):
		hwType = self.settings['hardware']['type']
		if hwType == 'dummy':
			return 1
		elif hwType == 'arduino':
			return 2
		else:
			return 0


	def loadHardware(self):
		self.stop()
		
		hwType = self.settings['hardware']['type']
		try:
			if hwType == 'dummy':
				self.hardware = Dummy.Dummy(self.settings, self.model)
			elif hwType == 'arduino':
				self.hardware = Arduino.Arduino(self.settings, self.model)
			else:
				self.hardware = NoHardware.NoHardware(self.settings, self.model)

		except BaseException as e:
			s = str(e)
			messagebox.showinfo("Hardware Init Error", "Could not init Hardware Instance «" + hwType + "»\n" + s)
			self.hardware = NoHardware.NoHardware(self.settings, self.model)
		
		return self.hardware


	def startCalibration(self, endListener):
		self.hardware.n = 0
		self.hardware.registerEndListener(endListener)


	def stop(self):
		if self.hardware is not None:
			self.hardware.stop()
			self.hardware = None





