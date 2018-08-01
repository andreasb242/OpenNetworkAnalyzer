#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
import OutputGraph
import DataModel;

# ================ Variable Definitions ===============================







SERIALPORT = "/dev/tty.usbmodem641" # For the Mac
#SERIALPORT = "COM5"
BAUD = 115200

resetSweep = FALSE
refReady = FALSE






class AnalyzerFrame(object):
	def __init__(self, settings):
		self.settings = settings
		self.model = DataModel.DataModel()
		self.initUi()


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

		b = ttk.Button(controlArea, text="+ Samples", width=10)#, command=BIncSampSweep)
		b.grid(column = 3, row = 0)

		b = ttk.Button(controlArea, text="- Samples", width=10)#, command=BDecSampSweep)
		b.grid(column = 3, row = 1)

		b = ttk.Button(controlArea, text="Set Freqs", width=10)#, command=BSetFreqs)
		b.grid(column = 4, row = 0)

		b = ttk.Button(controlArea, text="Calibrate", width=10)#, command=BCalibrate)
		b.grid(column = 5, row = 0)


	def run(self):
		self.root.mainloop()


	def windowClose(self):
		self.root.destroy()


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


	def buttonRrefLevelIncOne(self):
		self.model.refLevel = self.model.refLevel + 1

		if self.model.refLevel >= 20:
			self.model.refLevel = 20	

		self.graph.updateGraph()


	def buttonRrefLevelDecTen(self):
		self.model.refLevel = self.model.refLevel - 10

		if self.model.refLevel <= -60:
			self.model.refLevel = -60

		self.graph.updateGraph()


	def buttonRrefLevelDecOne(self):
		self.model.refLevel = self.model.refLevel - 1

		if self.model.refLevel <= -60:
			self.model.refLevel = -60

		self.graph.updateGraph()
























	


def BSetFreqs():
	prompt = "Set the sweep starting frequency (MHz):"
	retVal = simpledialog.askfloat("Set Start Frequency", prompt, parent = root, initialvalue = self.model.startFreq / 1000000, minvalue=0, maxvalue=72)
	if retVal is not None:
		startFreq = retVal*1000000

	prompt = "Set the sweep stopping frequency (MHz):"
	retVal = simpledialog.askfloat("Set Stop Frequency", prompt, parent=root, initialvalue=self.model.stopFreq / 1000000, minvalue=0, maxvalue=72)
	if retVal is not None:
		self.model.stopFreq = retVal * 1000000

	self.model.measMode = 0

	SetupArrays()
	UpdateGraph()

		
def BIncSampSweep():
	global numSamplesIndex

	if numSamplesIndex >= 5:
		numSamplesIndex = 5
	else:
		numSamplesIndex = numSamplesIndex + 1

	self.model.measMode = 0

	SetupArrays()
	UpdateGraph()

		
def BDecSampSweep():
	global numSamplesIndex

	if numSamplesIndex <= 0:
		numSamplesIndex = 0
	else:
		numSamplesIndex = numSamplesIndex - 1

	self.model.measMode = 0

	SetupArrays()
	UpdateGraph()


def BCalibrate():
	self.model.measMode = 2

	SetupArrays()

	txt = "Creating reference!"
	graph.create_text(graphWidth/2 + graphLeftBuffer, graphTopBuffer + graphHeight/2, text = txt, font=tkFont.Font(size=32), fill='Red')
	root.update()
	while refReady == FALSE:
		sleep(.001)

	reference[::] = readings[::]

	refReady = FALSE
	self.model.measMode = 1

	UpdateGraph()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
# ================ Call main routines ===============================
def Sweep():
	while (True):
		# UpdateGraph()
		MakeTrace()
		root.update_idletasks()
		root.update()

def BSetFreqs():
	global startFreq
	global stopFreq
	global measMode
	
	prompt = "Set the sweep starting frequency (MHz):"
	retVal = simpledialog.askfloat("Set Start Frequency", prompt, parent = root, initialvalue = startFreq/1000000, minvalue = 0, maxvalue = 72)
	if retVal is not None:
		startFreq = retVal*1000000
		
	prompt = "Set the sweep stopping frequency (MHz):"
	retVal = simpledialog.askfloat("Set Stop Frequency", prompt, parent = root, initialvalue = stopFreq/1000000, minvalue = 0, maxvalue = 72)
	if retVal is not None:
		stopFreq = retVal*1000000
	
	measMode = 0
	
	SetupArrays()
	UpdateGraph()
		
def BIncSampSweep():
	global numSamplesIndex
	global measMode
	
	if numSamplesIndex >= 5:
		numSamplesIndex = 5
	else:
		numSamplesIndex = numSamplesIndex + 1
	
	measMode = 0
	
	SetupArrays()
	UpdateGraph()
		
def BDecSampSweep():
	global numSamplesIndex
	global measMode
	
	if numSamplesIndex <= 0:
		numSamplesIndex = 0
	else:
		numSamplesIndex = numSamplesIndex - 1
	
	measMode = 0
	
	SetupArrays()
	UpdateGraph()
	
def BCalibrate():
	global measMode
	global refReady
	global reference
	global readings
	
	measMode = 2
		
	SetupArrays()
	
	txt = "Creating reference!"
	graph.create_text(graphWidth/2 + graphLeftBuffer, graphTopBuffer + graphHeight/2, text = txt, font=tkFont.Font(size=32), fill='Red')
	root.update()
	while refReady == FALSE:
		sleep(.001)
	
	reference[::] = readings[::]
	
	refReady = FALSE
	measMode = 1
	
	UpdateGraph()
	
# ================ Call main routines ===============================
def Sweep():
	while (True):
		# UpdateGraph()
		MakeTrace()
		root.update_idletasks()
		root.update()


