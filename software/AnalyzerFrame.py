#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

import OutputGraph
import DataModel;
import SettingsDialog

from CreateToolTip import CreateToolTip

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
		self.root.title('Scalar Network Analyzer')

		self.window = ttk.Frame(self.root, padding=5)
		self.window.grid()
		self.window.grid_columnconfigure(0, weight=1)

		self.initToolbar()

		graphArea = ttk.Frame(self.window)
		graphArea.grid(column=0, row=2)

		self.graph = OutputGraph.OutputGraph(graphArea, self.model)
		self.graph.updateGraph()


	## Init Toolbar Buttons
	def initToolbar(self):
		self.toolbar = Frame(self.window, bd=1)
		self.tbid = 0
		
		# Icons need to be kept, else the garbage collactor deletes them
		self.icons = []

		image = Image.open("icon/separator.png")
		self.separatorIcon = ImageTk.PhotoImage(image)


		self.addToolButton("zoom-out.png", "dB/div +", lambda p=self: AnalyzerFrame.buttonDBDivInc(p))
		self.addToolButton("zoom-in.png", "dB/div -", lambda p=self: AnalyzerFrame.buttonDBDivDec(p))
		self.addToolbarSpacer()
		self.addToolButton("go-bottom.png", "Ref Lvl +10", lambda p=self: AnalyzerFrame.buttonRefLevelIncTen(p))
		self.addToolButton("go-top.png", "Ref Lvl -10", lambda p=self: AnalyzerFrame.buttonRefLevelDecTen(p))
		self.addToolButton("go-down.png", "Ref Lvl +1", lambda p=self: AnalyzerFrame.buttonRefLevelIncOne(p))
		self.addToolButton("go-up.png", "Ref Lvl -1", lambda p=self: AnalyzerFrame.buttonRefLevelDecOne(p))
		self.addToolbarSpacer()
		self.addToolButton("sample-inc.png", "+ Samples", lambda p=self: AnalyzerFrame.buttonIncSampSweep(p))
		self.addToolButton("sample-dec.png", "- Samples", lambda p=self: AnalyzerFrame.buttonDecSampSweep(p))
		self.addToolbarSpacer()
		
		self.frequency = Frame(self.toolbar, bd=1)

		label = Label(self.frequency, text='Start sweep')
		label.grid(column=0, row=0)
		label = Label(self.frequency, text='End sweep')
		label.grid(column=0, row=1)

		label = Label(self.frequency, text='MHz')
		label.grid(column=2, row=0)
		label = Label(self.frequency, text='MHz')
		label.grid(column=2, row=1)

		self.txtStartFreqText = StringVar();
		self.txtStartFreq = Entry(self.frequency, width=6, textvariable=self.txtStartFreqText)
		self.txtStartFreq.grid(column=1, row=0)

		self.txtEndFreqText = StringVar();
		self.txtEndFreq = Entry(self.frequency, width=6, textvariable=self.txtEndFreqText)
		self.txtEndFreq.grid(column=1, row=1)
		self.loadFrequencies()

		self.frequency.pack(side=LEFT, padx=2, pady=2)

		image = Image.open("icon/apply-24.png")
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		button = Button(self.frequency, image=icon, relief=FLAT, command=lambda p=self: AnalyzerFrame.applyFrequencies(p))
		button.grid(column=3, row=1)
		CreateToolTip(button, "Apply sweep frequencies")

		self.addToolbarSpacer()

		self.addToolButton("settings.png", "Settings", lambda p=self: AnalyzerFrame.buttonShowSettings(p))
		self.addToolButton("calibrate.png", "Calibrate", lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		self.addToolbarSpacer()
		self.addToolButton("info.png", "About", lambda p=self: AnalyzerFrame.buttonShowAbout(p))
		self.addToolButton("exit.png", "Quit Application", lambda p=self: AnalyzerFrame.windowClose(p))

		self.toolbar.grid(column=0, row=0, sticky=(N, E, S, W))


	def addToolbarSpacer(self):
		spacer = Label(self.toolbar, text=' ', image=self.separatorIcon)
		spacer.pack(side=LEFT, padx=2, pady=2)


	def addToolButton(self, icon, tooltip, command):
		image = Image.open("icon/" + icon)
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		button = Button(self.toolbar, image=icon, relief=FLAT, command=command)
		button.pack(side=LEFT, padx=2, pady=2)

		CreateToolTip(button, tooltip)


	def applyFrequencies(self):
		self.model.startFreq = float(self.txtStartFreq.get()) * 1000000
		self.model.stopFreq = float(self.txtEndFreq.get()) * 1000000
		self.model.measMode = 0
		self.model.setupArrays()
		self.graph.updateGraph()
		self.loadFrequencies()


	def loadFrequencies(self):
		self.txtStartFreqText.set(str(self.model.startFreq / 1000000.0))
		self.txtEndFreqText.set(str(self.model.stopFreq / 1000000.0))


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


	def buttonShowSettings(self):
		settingsDialog = SettingsDialog.SettingsDialog(self.settings)
		settingsDialog.run()
		## TODO restart hardware interface!


	def buttonShowAbout(self):
		## TODO !!!!!!!!!
		pass


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




