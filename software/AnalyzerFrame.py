#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

import OutputGraph
import DataModel
import AboutDialog
import FooterFrame
from HardwareHandler import HardwareHandler
from hardware import BaseHardware

from CreateToolTip import CreateToolTip


class AnalyzerFrame(BaseHardware.HardwareListener):
	def __init__(self, settings, model, mainRoot):
		self.settings = settings
		self.hwhandler = HardwareHandler(settings, model)
		self.hwhandler.loadHardware()
		self.model = model
		self.mainRoot = mainRoot

		# Default values, will be overwritten by the hardware
		self.minFreq = 1
		self.maxFreq = 72000000

		self.model.startFreq = int(self.settings['view']['startFreq'])
		self.model.stopFreq = int(self.settings['view']['stopFreq'])

		self.initUi()

		# Connect the Hardware now
		self.hwhandler.start(self)


	## BaseHardware.HardwareListener
	## Callback for data updates, this method can be called from any thread
	def hwDataRead(self):
		self.root.after(0, lambda p=self: AnalyzerFrame.updateDataUiThread(p))


	## BaseHardware.HardwareListener
	## Callback for connection state, this method can be called from any thread
	def hwUpdateConnectionState(self, text, error=False):
		self.root.after(0, lambda text=text, p=self: AnalyzerFrame.updateConnectionStateUiThread(p, text, error))


	## BaseHardware.HardwareListener
	## Callback for HW Info, this method can be called from any thread
	def hwUpdateInfo(self, key, value):
		self.root.after(0, lambda key=key, value=value, p=self: AnalyzerFrame.updateInfoUiThread(p, key, value))


	## Update additional infos, this method should only be called in the UI Thread
	def updateInfoUiThread(self, key, value):
		if 'minFrequence' == key:
			self.labelMinFreqStart.config(text='min ' + str(float(value) / 1000000) + 'MHz')
			self.minFreq = int(value)

		if 'maxFrequence' == key:
			self.labelMaxFreqEnd.config(text='max ' + str(float(value) / 1000000) + 'MHz')
			self.maxFreq = int(value)

		if self.validateFrequencies() == True:
			self.applyFrequencies()

		self.model.startFreq = int(float(self.txtStartFreq.get()) * 1000000)
		self.model.stopFreq = int(float(self.txtEndFreq.get()) * 1000000)


	## Validate frequencies, return True if changed
	def validateFrequencies(self):
		freqChanged = False

		if self.model.startFreq < self.minFreq:
			self.model.startFreq = self.minFreq
			freqChanged = True

		if self.model.startFreq > self.maxFreq:
			self.model.startFreq = self.maxFreq
			freqChanged = True

		if self.model.stopFreq < self.minFreq:
			self.model.stopFreq = self.minFreq
			freqChanged = True

		if self.model.stopFreq > self.maxFreq:
			self.model.stopFreq = self.maxFreq
			freqChanged = True

		# Prevent division by zero in UI
		if self.model.stopFreq == self.model.startFreq:
			self.model.stopFreq = self.model.stopFreq + 0.001
			freqChanged = True

		if freqChanged == True:
			self.loadFrequencies()

		return freqChanged


	## Update Connection State, this method should only be called in the UI Thread
	def updateConnectionStateUiThread(self, text, error):
		self.footer.setDeviceState(text, error)


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

		self.initFooter()


	def initFooter(self):
		self.footer = FooterFrame.FooterFrame(self.root, self.settings, self.hwhandler)
		self.footer.frame.pack(fill=X)


	## Init Toolbar Buttons
	def initToolbar(self):
		self.toolbar = Frame(self.root, bd=1)
		self.toolbar.pack(fill=X)
		self.tbid = 0

		# Icons need to be kept, else the garbage collector deletes them
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

		label = Label(self.tbSubpanel, text='MHz, ')
		label.grid(column=2, row=0)
		label = Label(self.tbSubpanel, text='MHz, ')
		label.grid(column=2, row=1)

		self.labelMinFreqStart = Label(self.tbSubpanel, text='min ???MHz')
		self.labelMinFreqStart.grid(column=3, row=0)
		self.labelMaxFreqEnd = Label(self.tbSubpanel, text='max ???MHz')
		self.labelMaxFreqEnd.grid(column=3, row=1)

		self.txtStartFreqText = StringVar()
		self.txtStartFreq = Entry(self.tbSubpanel, width=6, textvariable=self.txtStartFreqText)
		self.txtStartFreq.grid(column=1, row=0)

		self.txtEndFreqText = StringVar()
		self.txtEndFreq = Entry(self.tbSubpanel, width=6, textvariable=self.txtEndFreqText)
		self.txtEndFreq.grid(column=1, row=1)
		self.loadFrequencies()

		image = Image.open("icon/apply-24.png")
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		button = Button(self.tbSubpanel, image=icon, relief=FLAT, command=lambda p=self: AnalyzerFrame.applyFrequencies(p))
		button.grid(column=4, row=1)
		CreateToolTip(button, "Apply sweep frequencies")

		self.addToolbarSpacer()

		self.addToolButton("calibrate.png", "Calibrate", lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		self.addToolbarSubPanel()
		self.addToolButton("edit-clear.png", "Clear Calibration", lambda p=self: AnalyzerFrame.buttonClearReference(p), subpanel=True)

		self.calibrationStateButton = self.addToolButton("not-calibrated.png", "Calibration state", None, subpanel=True)
		image = Image.open("icon/not-calibrated.png")
		self.calibrationNotCalibratedIcon = ImageTk.PhotoImage(image)
		image = Image.open("icon/calibrated.png")
		self.calibrationCalibratedIcon = ImageTk.PhotoImage(image)

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

		return button


	def applyFrequencies(self):
		self.model.startFreq = int(float(self.txtStartFreq.get()) * 1000000)
		self.model.stopFreq = int(float(self.txtEndFreq.get()) * 1000000)
		self.validateFrequencies()

		self.setModeAsolute()

		self.settings['view']['startFreq'] = str(self.model.startFreq)
		self.settings['view']['stopFreq'] = str(self.model.stopFreq)

		self.model.setupArrays()
		self.graph.updateGraph()
		self.loadFrequencies()


	def loadFrequencies(self):
		self.txtStartFreqText.set(str(self.model.startFreq / 1000000.0))
		self.txtEndFreqText.set(str(self.model.stopFreq / 1000000.0))

	def run(self):
		self.root.mainloop()


	def windowClose(self):
		self.hwhandler.stop()
		self.root.destroy()
		self.mainRoot.destroy()
		print('Main window closed')


	def buttonClearReference(self):
		self.setModeAsolute()


	def buttonShowAbout(self):
		about = AboutDialog.AboutDialog(self.root)
		about.run()


	def buttonCalibrate(self):
		self.setModeReferencing()

		self.model.setupArrays()

		self.graph.addCenterInfoText('Calibration running...')
		self.root.update()


		self.hwhandler.startCalibration(lambda p=self: AnalyzerFrame.calibrationEndListener(p))


	# This can be called from any thread
	def calibrationEndListener(self):
		self.root.after(0, lambda p=self: AnalyzerFrame.calibrationEndListenerUiThread(p))


	# Call only from UI Thread!
	def calibrationEndListenerUiThread(self):
		self.model.reference[::] = self.model.readings[::]

		self.setModeRelative()
		self.graph.updateGraph()


	def buttonDecSampSweep(self):
		if self.model.numSamplesIndex <= 0:
			self.model.numSamplesIndex = 0
		else:
			self.model.numSamplesIndex = self.model.numSamplesIndex - 1

		self.setModeAsolute()

		self.model.setupArrays()
		self.graph.updateGraph()


	def buttonIncSampSweep(self):
		self.model.numSamplesIndex = self.model.numSamplesIndex + 1
		if self.model.numSamplesIndex >= len(self.model.numSamplesList):
			self.model.numSamplesIndex = len(self.model.numSamplesList) - 1

		self.setModeAsolute()

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

		## Currently fixed, on rescaling the div size, but not the count changes
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


	def setModeAsolute(self):
		self.model.measMode = 0
		self.calibrationStateButton.config(image=self.calibrationNotCalibratedIcon)


	def setModeRelative(self):
		self.model.measMode = 1
		self.calibrationStateButton.config(image=self.calibrationCalibratedIcon)


	def setModeReferencing(self):
		self.model.measMode = 2
		self.calibrationStateButton.config(image=self.calibrationNotCalibratedIcon)
