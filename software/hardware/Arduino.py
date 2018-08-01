#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware

class Arduino(BaseHardware.BaseHardware):
	def __init__(self, settings):
		super().__init__(settings)



## TODO !!!!!!!!
class SerialReader(object):
	
	def __init__(self):
		self.adcValue = 0
		global BAUD
		global SERIALPORT
		
		try:
			self.serialPort = serial.Serial(SERIALPORT, BAUD, timeout=1)
			thread = threading.Thread(target=self.run)
			thread.daemon = True
			thread.start()
		except:
			messagebox.showinfo("Oh no!","Serial comms aren't working.")

	def run(self):
		global resetSweep
		global readings
		global refReady
		global measMode
		
		self.n = 0
		
		while True:			
			if resetSweep == TRUE:
				resetSweep = FALSE
				self.n = 0
									
			FTW = readings[self.n*2].astype(int).astype(str)+'\n'
			self.serialPort.write(FTW.encode()) 						# Send frequency command
			
			self.serialPort.write('p\n'.encode())						
			self.adcValue = self.serialPort.readline().decode().strip()

			if len(self.adcValue) != 0:
				readings[self.n*2+1] = float(self.adcValue) * .5*0.0488 - 90.5 #0.0488 or 0.1953 - 83.998
				self.n = self.n + 1
			
			if self.n >= numSamplesList[numSamplesIndex]:
				self.n = 0
				if measMode == 2:
					refReady = TRUE
					print("REF READY!")



