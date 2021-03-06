#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


import threading
import traceback
import time


class HardwareListener(object):
	## Callback for data updates, this method can be called from any thread
	def hwDataRead(self):
		pass

	## Callback for connection state, this method can be called from any thread
	def hwUpdateConnectionState(self, text, error=False):
		pass

	## Callback for HW Info, this method can be called from any thread
	def hwUpdateInfo(self, key, value):
		pass


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

		## Hardware Information
		self.boardType = 'Unknown'
		self.boardVersion = 'Unknown'

	def start(self, listener):
		self.listener = listener
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


	def incrementCount(self):
		self.n = self.n + 1
		if self.n >= self.model.numSamplesList[self.model.numSamplesIndex]:
			self.n = 0
	
			if self.endListener is not None:
				self.endListener()
				self.endListener = None


	# Thread method
	def run(self):
		self.listener.hwUpdateConnectionState('Connecting...')

		if self.initConnection() == False:
			self.listener.hwUpdateConnectionState('Connection failed!', True)
			return


		self.listener.hwUpdateInfo('minFrequence', self.minFrequence)
		self.listener.hwUpdateInfo('maxFrequence', self.maxFrequence)

		self.n = 0

		while self.running:
			if self.model.pause:
				time.sleep(0.1)
				continue

			if self.resetSweep == True:
				self.resetSweep = False
				self.n = 0

			try:
				if self.readValue() == False:
					return
			
				if self.running == False:
					print('Hardware Thread stopped')
					return
			
				self.listener.hwDataRead()
			
				self.model.lastUpdatedIndex = self.n

				self.incrementCount()
			except BaseException as e:
				# Here should be a synchronisation, as the array size
				# May be changed in the UI Thread, but this works also...
				traceback.print_exc()
				self.n = 0


