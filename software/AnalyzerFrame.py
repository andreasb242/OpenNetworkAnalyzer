#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import simpledialog

import OutputGraph
import DataModel;

## TODO Remove
from time import sleep


refReady = FALSE






class AnalyzerFrame(object):
	def __init__(self, settings, hardware, model):
		self.settings = settings
		self.hardware = hardware
		self.model = model
		self.initUi()

		self.hardware.start(lambda p=self: AnalyzerFrame.updateData(p))		


	def initUi(self):
		self.root = Tk()
		self.root.resizable(False, False)
		self.root.title('Scalar Network Analyzer')

		window = ttk.Frame(self.root, padding=5)
		window.grid()
		window.grid_columnconfigure(0, weight=1)

		graphArea = ttk.Frame(window)
		graphArea.grid(column=0, row=0)

		self.graph = OutputGraph.OutputGraph(graphArea, self.model)
		self.graph.updateGraph()

		controlArea = ttk.LabelFrame(window, text="Controls", borderwidth=10)
		controlArea.grid(column=0, row=1, sticky=(N,E,S,W))

		b = ttk.Button(controlArea, text="dB/div +", width=10, command=lambda p=self: AnalyzerFrame.buttonDBDivInc(p))
		b.grid(column = 0, row = 0)

		b = ttk.Button(controlArea, text="dB/div -", width=10, command=lambda p=self: AnalyzerFrame.buttonDBDivDec(p))
		b.grid(column = 0, row = 1)

		b = ttk.Button(controlArea, text="Ref Lvl +10", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelIncTen(p))
		b.grid(column = 1, row = 0)

		b = ttk.Button(controlArea, text="Ref Lvl -10", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelDecTen(p))
		b.grid(column = 1, row = 1)

		b = ttk.Button(controlArea, text="Ref Lvl +1", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelIncOne(p))
		b.grid(column = 2, row = 0)

		b = ttk.Button(controlArea, text="Ref Lvl -1", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelDecOne(p))
		b.grid(column = 2, row = 1)

		b = ttk.Button(controlArea, text="+ Samples", width=10, command=lambda p=self: AnalyzerFrame.buttonIncSampSweep(p))
		b.grid(column = 3, row = 0)

		b = ttk.Button(controlArea, text="- Samples", width=10, command=lambda p=self: AnalyzerFrame.buttonDecSampSweep(p))
		b.grid(column = 3, row = 1)

		b = ttk.Button(controlArea, text="Set Freqs", width=10, command=lambda p=self: AnalyzerFrame.buttonSetFreqs(p))
		b.grid(column = 4, row = 0)

		b = ttk.Button(controlArea, text="Calibrate", width=10, command=lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		b.grid(column = 5, row = 0)


	## Callback for data updates, this method can be called from any thread
	def updateData(self):
		self.root.after(0, lambda p=self: AnalyzerFrame.updateDataUiThread(p))


	## Update the UI, this method should only be called in the UI Thread
	def updateDataUiThread(self):
		self.graph.makeTrace()


	def run(self):
		self.root.mainloop()


	def windowClose(self):
		self.root.destroy()


	def buttonCalibrate(self):
		measMode = 2
		
		SetupArrays()
	
		txt = "Creating reference!"
		graph.create_text(graphWidth / 2 + graphLeftBuffer, graphTopBuffer + graphHeight / 2, text=txt, font=tkFont.Font(size=32), fill='Red')
		self.root.update()
		
		## TODO Synchronisation!!!!
		while refReady == FALSE:
			sleep(.001)
	
		reference[::] = readings[::]
	
		refReady = FALSE
		measMode = 1
	
		self.graph.updateGraph()


	def buttonDecSampSweep(self):
		if self.model.numSamplesIndex <= 0:
			self.model.numSamplesIndex = 0
		else:
			self.model.numSamplesIndex = self.model.numSamplesIndex - 1

		self.model.measMode = 0

		self.model.setupArrays()
		self.graph.updateGraph()


	def buttonIncSampSweep(self):
		if self.model.numSamplesIndex >= 5:
			self.model.numSamplesIndex = 5
		else:
			self.model.numSamplesIndex = self.model.numSamplesIndex + 1

		self.model.measMode = 0

		self.model.setupArrays()
		self.graph.updateGraph()


	def buttonSetFreqs(self):
		prompt = "Set the sweep starting frequency (MHz):"
		retVal = simpledialog.askfloat("Set Start Frequency", prompt, parent=root, initialvalue=self.model.startFreq / 1000000, minvalue=0, maxvalue=72)
		if retVal is not None:
			startFreq = retVal * 1000000

		prompt = "Set the sweep stopping frequency (MHz):"
		retVal = simpledialog.askfloat("Set Stop Frequency", prompt, parent=root, initialvalue=self.model.stopFreq / 1000000, minvalue=0, maxvalue=72)
		if retVal is not None:
			self.model.stopFreq = retVal * 1000000

		self.model.measMode = 0

		self.model.setupArrays()
		self.graph.updateGraph()


	def buttonDBDivInc(self):
		if self.model.dBDivIndex >= 4:
			self.model.dBDivIndex = 4
		else:
			self.model.dBDivIndex = self.model.dBDivIndex + 1

		self.graph.updateGraph()


	def buttonDBDivDec(self):
		if self.model.dBDivIndex <= 0:
			self.model.dBDivIndex = 0
		else:
			self.model.dBDivIndex = self.model.dBDivIndex - 1

		self.graph.updateGraph()


	def buttonRefLevelIncTen(self):
		self.model.refLevel = self.model.refLevel + 10

		if self.model.refLevel >= 20:
			self.model.refLevel = 20

		self.graph.updateGraph()


	def buttonRefLevelIncOne(self):
		self.model.refLevel = self.model.refLevel + 1

		if self.model.refLevel >= 20:
			self.model.refLevel = 20	

		self.graph.updateGraph()


	def buttonRefLevelDecTen(self):
		self.model.refLevel = self.model.refLevel - 10

		if self.model.refLevel <= -60:
			self.model.refLevel = -60

		self.graph.updateGraph()


	def buttonRefLevelDecOne(self):
		self.model.refLevel = self.model.refLevel - 1

		if self.model.refLevel <= -60:
			self.model.refLevel = -60

		self.graph.updateGraph()




