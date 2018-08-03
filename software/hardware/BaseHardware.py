#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


import threading


class BaseHardware(object):
	def __init__(self, settings, model):
		self.settings = settings
		self.model = model
		self.resetSweepFlag = False
		self.running = True
		
		## Current reading index
		self.n = 0
		
		self.endListener = None
		self.minFrequence = 1000000
		self.maxFrequence = 2000000


	def start(self, updateCallback, connectCallback):
		self.updateCallback = updateCallback
		self.connectCallback = connectCallback
		self.thread = threading.Thread(target=self.run)
		self.thread.daemon = True
		self.thread.start()


	def resetSweep(self):
		self.resetSweepFlag = True


	# Read a single value, return True to continue, False to stop
	def readValue(self):
		return False	


	def stop(self):
		self.running = False


	# Register a listener to get informed about the end, used for calibration
	# Invoked only once
	def registerEndListener(self, endListener):
		self.endListener = endListener


	# Initialize connection
	def initConnection(self):
		return False


	# Thread method
	def run(self):
		self.connectCallback('Connecting...')
		if self.initConnection() == False:
			self.connectCallback('Connection failed!')
			return
	
		self.n = 0

		while self.running:
			if self.resetSweep == True:
				self.resetSweep = False
				self.n = 0

			if self.readValue() == False:
				return
			
			if self.running == False:
				print('Hardware Thread stopped')
				return
			
			self.updateCallback()
			
			self.model.lastUpdatedIndex = self.n

			self.n = self.n + 1
			if self.n >= self.model.numSamplesList[self.model.numSamplesIndex]:
				self.n = 0
				
				if self.endListener is not None:
					self.endListener()
					self.endListener = None




