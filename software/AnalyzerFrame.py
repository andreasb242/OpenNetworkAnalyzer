#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

import OutputGraph
import DataModel;
import SettingsDialog
import AboutDialog

from CreateToolTip import CreateToolTip


class AnalyzerFrame(object):
	def __init__(self, settings, hardware, model, mainRoot):
		self.settings = settings
		self.hardware = hardware
		self.model = model
		self.mainRoot = mainRoot
		self.restart = False
		self.initUi()

		self.hardware.start(lambda p=self: AnalyzerFrame.updateData(p))		


	## Callback for data updates, this method can be called from any thread
	def updateData(self):
		self.root.after(0, lambda p=self: AnalyzerFrame.updateDataUiThread(p))


	## Update the UI, this method should only be called in the UI Thread
	def updateDataUiThread(self):
		self.graph.makeTrace()


	def initUi(self):
		self.root = Toplevel()
		self.root.title('Scalar Network Analyzer')
		self.root.protocol("WM_DELETE_WINDOW", lambda p=self: AnalyzerFrame.windowClose(p))

		self.initToolbar()

		self.graph = OutputGraph.OutputGraph(self.root, self.model)
		self.graph.graph.pack(fill=BOTH, expand=1)
		self.graph.updateGraph()


	## Init Toolbar Buttons
	def initToolbar(self):
		self.toolbar = Frame(self.root, bd=1)
		self.toolbar.pack(fill=X)
		self.tbid = 0
		
		# Icons need to be kept, else the garbage collactor deletes them
		self.icons = []

		image = Image.open("icon/separator.png")
		self.separatorIcon = ImageTk.PhotoImage(image)


		self.addToolButton("zoom-out.png", "dB/div +", lambda p=self: AnalyzerFrame.buttonDBDivInc(p))
		self.addToolButton("zoom-in.png", "dB/div -", lambda p=self: AnalyzerFrame.buttonDBDivDec(p))
		self.addToolbarSpacer()

		self.addToolbarSubPanel()
		self.addToolButton("go-top-24.png", "Ref Level -10", lambda p=self: AnalyzerFrame.buttonRefLevelDecTen(p), subpanel=True)
		self.addToolButton("go-bottom-24.png", "Ref Level +10", lambda p=self: AnalyzerFrame.buttonRefLevelIncTen(p), subpanel=True)
		self.addToolButton("go-up-24.png", "Ref Level -1", lambda p=self: AnalyzerFrame.buttonRefLevelDecOne(p), subpanel=True)
		self.addToolButton("go-down-24.png", "Ref Level +1", lambda p=self: AnalyzerFrame.buttonRefLevelIncOne(p), subpanel=True)
		
		self.addToolButton("auto-vertical.png", "Auto Ref Level", lambda p=self: AnalyzerFrame.buttonRefLevelAuto(p))
		
		self.addToolbarSpacer()

		self.addToolButton("sample-inc.png", "+ Samples", lambda p=self: AnalyzerFrame.buttonIncSampSweep(p))
		self.addToolButton("sample-dec.png", "- Samples", lambda p=self: AnalyzerFrame.buttonDecSampSweep(p))
		self.addToolbarSpacer()

		self.addToolbarSubPanel()

		label = Label(self.tbSubpanel, text='Start sweep')
		label.grid(column=0, row=0)
		label = Label(self.tbSubpanel, text='End sweep')
		label.grid(column=0, row=1)

		label = Label(self.tbSubpanel, text='MHz')
		label.grid(column=2, row=0)
		label = Label(self.tbSubpanel, text='MHz')
		label.grid(column=2, row=1)

		self.txtStartFreqText = StringVar();
		self.txtStartFreq = Entry(self.tbSubpanel, width=6, textvariable=self.txtStartFreqText)
		self.txtStartFreq.grid(column=1, row=0)

		self.txtEndFreqText = StringVar();
		self.txtEndFreq = Entry(self.tbSubpanel, width=6, textvariable=self.txtEndFreqText)
		self.txtEndFreq.grid(column=1, row=1)
		self.loadFrequencies()

		image = Image.open("icon/apply-24.png")
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		button = Button(self.tbSubpanel, image=icon, relief=FLAT, command=lambda p=self: AnalyzerFrame.applyFrequencies(p))
		button.grid(column=3, row=1)
		CreateToolTip(button, "Apply sweep frequencies")

		self.addToolbarSpacer()

		self.addToolButton("settings.png", "Settings", lambda p=self: AnalyzerFrame.buttonShowSettings(p))
		self.addToolButton("calibrate.png", "Calibrate", lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		self.addToolbarSpacer()

		self.addToolbarSubPanel()
		self.addToolButton("info-24.png", "About", lambda p=self: AnalyzerFrame.buttonShowAbout(p), subpanel=True)
		self.addToolButton("exit-24.png", "Quit Application", lambda p=self: AnalyzerFrame.windowClose(p), subpanel=True)


	def addToolbarSubPanel(self):
		self.tbSubpanel = Frame(self.toolbar, bd=1)
		self.tbSubpanel.pack(side=LEFT, padx=2, pady=2)
		
		self.tbSubX = 0
		self.tbSubY = 0


	def addToolbarSpacer(self):
		spacer = Label(self.toolbar, text=' ', image=self.separatorIcon)
		spacer.pack(side=LEFT, padx=2, pady=2)


	def addToolButton(self, icon, tooltip, command, subpanel=False):
		image = Image.open("icon/" + icon)
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		if subpanel == True:
			button = Button(self.tbSubpanel, image=icon, relief=FLAT, command=command)
			button.grid(column=self.tbSubX, row=self.tbSubY)
			self.tbSubY = self.tbSubY + 1
			if self.tbSubY >= 2:
				self.tbSubY = 0
				self.tbSubX = self.tbSubX + 1
		else:
			button = Button(self.toolbar, image=icon, relief=FLAT, command=command)
			button.pack(side=LEFT, padx=2, pady=2)

		CreateToolTip(button, tooltip)


	def applyFrequencies(self):
		self.model.startFreq = int(float(self.txtStartFreq.get()) * 1000000)
		self.model.stopFreq = int(float(self.txtEndFreq.get()) * 1000000)
		self.model.measMode = 0
		
		self.settings['view']['startFreq'] = str(self.model.startFreq);
		self.settings['view']['stopFreq'] = str(self.model.stopFreq);

		self.model.setupArrays()
		self.graph.updateGraph()
		self.loadFrequencies()


	def loadFrequencies(self):
		self.txtStartFreqText.set(str(self.model.startFreq / 1000000.0))
		self.txtEndFreqText.set(str(self.model.stopFreq / 1000000.0))

	def run(self):
		self.root.mainloop()


	def windowClose(self):
		self.hardware.stop()
		self.root.destroy()
		self.mainRoot.destroy()
		print('Main window closed')


	def buttonShowSettings(self):
		settingsDialog = SettingsDialog.SettingsDialog(self.settings, self.root)
		settingsDialog.run()
		if settingsDialog.stored == True:
			print('Restart application to apply changes...')
			self.restart = True
			self.windowClose()


	def buttonShowAbout(self):
		about = AboutDialog.AboutDialog(self.root)
		about.run()


	def buttonCalibrate(self):
		self.model.measMode = 2
		
		self.model.setupArrays()
	
		self.graph.addCenterInfoText('Calibration running...')
		self.root.update()
		
		self.hardware.n = 0
		self.hardware.registerEndListener(lambda p=self: AnalyzerFrame.calibrationEndListener(p))


	# This can be called from any thread
	def calibrationEndListener(self):
		self.root.after(0, lambda p=self: AnalyzerFrame.calibrationEndListenerUiThread(p))


	# Call only from UI Thread!
	def calibrationEndListenerUiThread(self):
		self.model.reference[::] = self.model.readings[::]
	
		self.model.measMode = 1
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


	def buttonRefLevelAuto(self):
		minV, maxV = self.model.getMinMaxValues()
		div = self.model.dBDivList[self.model.dBDivIndex]

		#TODO Depending on size, needs to be calculated if resizeable!
		divCount = 8
		center = minV + (maxV - minV) / 2
		
		# Round to div position
		pos = center // div * div

		self.model.refLevel = pos + (divCount / 2 * div)
	
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
		print('self.model.refLevel=' + str(self.model.refLevel))




