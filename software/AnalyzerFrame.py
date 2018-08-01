#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

import OutputGraph
import DataModel;
from CreateToolTip import CreateToolTip

## TODO Remove
from time import sleep


refReady = FALSE



#style.map("Checkbox.Treeview",
#fieldbackground=[("disabled", '#E6E6E6')],
#foreground=[("disabled", 'gray40')],
#background=[("disabled", '#E6E6E6')])


class AnalyzerFrame(object):
	def __init__(self, settings, hardware, model):
		self.settings = settings
		self.hardware = hardware
		self.model = model
		self.initUi()

		self.hardware.start(lambda p=self: AnalyzerFrame.updateData(p))		


	def initUi(self):
		self.root = Tk()
		self.root.title('Scalar Network Analyzer')

		self.window = ttk.Frame(self.root, padding=5)
		self.window.grid()
		self.window.grid_columnconfigure(0, weight=1)

		self.initToolbar()

		graphArea = ttk.Frame(self.window)
		graphArea.grid(column=0, row=2)

		self.graph = OutputGraph.OutputGraph(graphArea, self.model)
		self.graph.updateGraph()
		
		self.initButtonList()


	def initButtonList(self):
		controlArea = ttk.LabelFrame(self.window, text="Controls", borderwidth=10)
		controlArea.grid(column=0, row=1, sticky=(N, E, S, W))

		b = ttk.Button(controlArea, text="dB/div +", width=10, command=lambda p=self: AnalyzerFrame.buttonDBDivInc(p))
		b.grid(column=0, row=0)

		b = ttk.Button(controlArea, text="dB/div -", width=10, command=lambda p=self: AnalyzerFrame.buttonDBDivDec(p))
		b.grid(column=0, row=1)

		b = ttk.Button(controlArea, text="Ref Lvl +10", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelIncTen(p))
		b.grid(column=1, row=0)

		b = ttk.Button(controlArea, text="Ref Lvl -10", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelDecTen(p))
		b.grid(column=1, row=1)

		b = ttk.Button(controlArea, text="Ref Lvl +1", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelIncOne(p))
		b.grid(column=2, row=0)

		b = ttk.Button(controlArea, text="Ref Lvl -1", width=10, command=lambda p=self: AnalyzerFrame.buttonRefLevelDecOne(p))
		b.grid(column=2, row=1)

		b = ttk.Button(controlArea, text="+ Samples", width=10, command=lambda p=self: AnalyzerFrame.buttonIncSampSweep(p))
		b.grid(column=3, row=0)

		b = ttk.Button(controlArea, text="- Samples", width=10, command=lambda p=self: AnalyzerFrame.buttonDecSampSweep(p))
		b.grid(column=3, row=1)

		b = ttk.Button(controlArea, text="Set Freqs", width=10, command=lambda p=self: AnalyzerFrame.buttonSetFreqs(p))
		b.grid(column=4, row=0)

		b = ttk.Button(controlArea, text="Calibrate", width=10, command=lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		b.grid(column=5, row=0)


	## Init Toolbar Buttons
	def initToolbar(self):
		self.toolbar = Frame(self.window, bd=1)
		self.tbid = 0
		
		# Icons need to be kept, else the garbage collactor deletes them
		self.icons = []

		self.addToolButton("exit.png", "dB/div +", lambda p=self: AnalyzerFrame.buttonDBDivInc(p))
		self.addToolButton("exit.png", "dB/div -", lambda p=self: AnalyzerFrame.buttonDBDivDec(p))
		self.addToolButton("exit.png", "Ref Lvl +10", lambda p=self: AnalyzerFrame.buttonRefLevelIncTen(p))
		self.addToolButton("exit.png", "Ref Lvl -10", lambda p=self: AnalyzerFrame.buttonRefLevelDecTen(p))
		self.addToolButton("exit.png", "Ref Lvl +1", lambda p=self: AnalyzerFrame.buttonRefLevelIncOne(p))
		self.addToolButton("exit.png", "Ref Lvl -1", lambda p=self: AnalyzerFrame.buttonRefLevelDecOne(p))
		self.addToolButton("exit.png", "+ Samples", lambda p=self: AnalyzerFrame.buttonIncSampSweep(p))
		self.addToolButton("exit.png", "- Samples", lambda p=self: AnalyzerFrame.buttonDecSampSweep(p))
		self.addToolButton("exit.png", "Set Freqs", lambda p=self: AnalyzerFrame.buttonSetFreqs(p))
		self.addToolButton("exit.png", "Calibrate", lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		self.addToolButton("exit.png", "Quit Application", lambda p=self: AnalyzerFrame.windowClose(p))

		self.toolbar.grid(column=0, row=0, sticky=(N, E, S, W))
	
	
	def addToolButton(self, icon, tooltip, command):
		image = Image.open("icon/" + icon)
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		button = Button(self.toolbar, image=icon, relief=FLAT, command=command)
		button.pack(side=LEFT, padx=2, pady=2)

		CreateToolTip(button, tooltip)


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




