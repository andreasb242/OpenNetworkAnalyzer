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
	def __init__(self, settings, model):
		self.settings = settings
		self.hwhandler = HardwareHandler(settings, model)
		self.model = model

		# Default values, will be overwritten by the hardware
		self.minFreq = 1
		self.maxFreq = 10000000

		self.initUi()

		self.hwhandler.loadHardware()
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
			self.labelMinFreqStart.config(text='min ' + str(float(value) / 1000000))
			self.minFreq = int(value)

		if 'maxFrequence' == key:
			self.labelMaxFreqEnd.config(text='max ' + str(float(value) / 1000000))
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
		self.root = Tk(className='OpenNetworkAnalyzer')
		self.root.title('Scalar Network Analyzer')
		self.root.protocol("WM_DELETE_WINDOW", lambda p=self: AnalyzerFrame.windowClose(p))

		icon = ImageTk.PhotoImage(Image.open("icon/icon.png"))
		self.root.tk.call('wm', 'iconphoto', self.root._w, icon)  

		self.initToolbar()

		colorIndex = int(self.settings['view']['colorScheme'])
		self.graph = OutputGraph.OutputGraph(self.root, self.model, colorIndex)
		self.graph.graph.pack(fill=BOTH, expand=1)
		self.graph.updateGraph()
		
		# Update initial values
		self.updateSweepLabel()
		self.updateDbDiv()
		self.updateRefPoint()

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

		self.addToolbarSubPanel()

		self.dbPerDivLabel = Label(self.tbSubpanel, text='XXX db')
		self.dbPerDivLabel.grid(column=0, row=0)
		line = Frame(self.tbSubpanel, bd=1)
		line.configure(background='black')
		line.grid(column=0, row=1, sticky=E+W)
		label = Label(self.tbSubpanel, text='div')
		label.grid(column=0, row=2)

		self.addToolbarSpacer()

		self.addToolbarSubPanel()
		self.addToolButton("go-top-24.png", "Ref Level -10", lambda p=self: AnalyzerFrame.buttonRefLevelDecTen(p), subpanel=True)
		self.addToolButton("go-bottom-24.png", "Ref Level +10", lambda p=self: AnalyzerFrame.buttonRefLevelIncTen(p), subpanel=True)
		self.addToolButton("go-up-24.png", "Ref Level -1", lambda p=self: AnalyzerFrame.buttonRefLevelDecOne(p), subpanel=True)
		self.addToolButton("go-down-24.png", "Ref Level +1", lambda p=self: AnalyzerFrame.buttonRefLevelIncOne(p), subpanel=True)

		self.addToolButton("auto-vertical.png", "Auto Ref Level", lambda p=self: AnalyzerFrame.buttonRefLevelAuto(p))

		self.addToolbarSubPanel()

		self.refPointLabel1 = Label(self.tbSubpanel, text='XXX unit')
		self.refPointLabel1.grid(column=0, row=0)
		self.refPointLabel2 = Label(self.tbSubpanel, text='XXX unit')
		self.refPointLabel2.grid(column=0, row=1)


		self.addToolbarSpacer()

		self.addToolButton("sample-inc.png", "+ Samples", lambda p=self: AnalyzerFrame.buttonIncSampSweep(p))
		self.addToolButton("sample-dec.png", "- Samples", lambda p=self: AnalyzerFrame.buttonDecSampSweep(p))

		self.addToolbarSubPanel()

		self.sweepCountLabel = Label(self.tbSubpanel, text='XXX samples')
		self.sweepCountLabel.grid(column=0, row=0)
		line = Frame(self.tbSubpanel, bd=1)
		line.configure(background='black')
		line.grid(column=0, row=1, sticky=E+W)
		label = Label(self.tbSubpanel, text='sweep')
		label.grid(column=0, row=2)
		
		self.addToolbarSpacer()

		self.addToolbarSubPanel()

		label = Label(self.tbSubpanel, text='Sweep from')
		label.grid(column=0, row=0, sticky=E)
		label = Label(self.tbSubpanel, text='to')
		label.grid(column=0, row=1, sticky=E)

		label = Label(self.tbSubpanel, text='MHz, ')
		label.grid(column=2, row=0)
		label = Label(self.tbSubpanel, text='MHz, ')
		label.grid(column=2, row=1)

		self.labelMinFreqStart = Label(self.tbSubpanel, text='min ???.?')
		self.labelMinFreqStart.grid(column=3, row=0)
		self.labelMaxFreqEnd = Label(self.tbSubpanel, text='max ???.?')
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


		image = Image.open("icon/pause.png")
		self.pauseImage = ImageTk.PhotoImage(image)
		self.icons.append(self.pauseImage)
		image = Image.open("icon/play.png")
		self.playImage = ImageTk.PhotoImage(image)
		self.icons.append(self.pauseImage)

		self.buttonPlayPause = Button(self.tbSubpanel, image=self.pauseImage, relief=FLAT, command=lambda p=self: AnalyzerFrame.buttonPlayPause(p))
		self.buttonPlayPause.grid(column=4, row=0)
		CreateToolTip(self.buttonPlayPause, "Pause / Start running")


		self.addToolbarSpacer()

		self.addToolButton("calibrate.png", "Calibrate (e.g. connect output to input)", lambda p=self: AnalyzerFrame.buttonCalibrate(p))
		self.addToolbarSubPanel()
		self.addToolButton("edit-clear.png", "Clear Calibration", lambda p=self: AnalyzerFrame.buttonClearReference(p), subpanel=True)

		self.calibrationStateButton = self.addToolButton("not-calibrated.png", "Calibration state", None, subpanel=True)
		image = Image.open("icon/not-calibrated.png")
		self.calibrationNotCalibratedIcon = ImageTk.PhotoImage(image)
		image = Image.open("icon/calibrated.png")
		self.calibrationCalibratedIcon = ImageTk.PhotoImage(image)

		self.addToolbarSpacer()
		self.addToolbarSubPanel()
		self.addToolButton("refresh-line.png", "Show / Hide refresh line", lambda p=self: AnalyzerFrame.buttonShowHideRefreshLine(p), subpanel=True)
		self.styleButton = self.addToolButton("style.png", "Switch style", None, subpanel=True)
		self.initStyleMenu()

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


	def buttonShowHideRefreshLine(self):
		self.model.showMarkerLine = not self.model.showMarkerLine
		self.settings['view']['showMarker'] = str(self.model.showMarkerLine)


	def initStyleMenu(self):
		self.styleButton.bind("<Button-1>", lambda event, p=self: AnalyzerFrame.buttonSwitchStyle(p, event))


	def buttonSwitchStyle(self, event):
		popup = Menu(self.styleButton, tearoff=0, borderwidth=0)
		for i in range(0, len(self.graph.colorlist)):
			colors = self.graph.colorlist[i]
			popup.add_command(label=colors['_name'], command=lambda index=i, p=self: AnalyzerFrame.buttonSwitchStyleApply(p, index))

		# display the popup menu
		try:
			popup.tk_popup(event.x_root, event.y_root, 0)
		finally:
			# make sure to release the grab (Tk 8.0a1 only)
			popup.grab_release()


	def buttonSwitchStyleApply(self, index):
		self.graph.applyColorset(index)
		self.graph.updateGraph()
		self.settings['view']['colorScheme'] = str(self.graph.selectedColorSet)


	def buttonPlayPause(self):
		if self.model.pause:
			self.buttonPlayPause.config(image=self.pauseImage)
			self.model.pause = False
		else:
			self.buttonPlayPause.config(image=self.playImage)
			self.model.pause = True
			


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
		self.restartSweep()


	def loadFrequencies(self):
		self.txtStartFreqText.set(str(self.model.startFreq / 1000000.0))
		self.txtEndFreqText.set(str(self.model.stopFreq / 1000000.0))

	def run(self):
		self.root.mainloop()


	def windowClose(self):
		self.hwhandler.stop()
		self.root.destroy()
		print('Main window closed')


	def buttonClearReference(self):
		self.setModeAsolute()

		## Unit changed
		self.updateDbDiv()
		self.updateRefPoint()


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
		
		## Unit changed
		self.updateDbDiv()
		self.updateRefPoint()


	def buttonDecSampSweep(self):
		if self.model.numSamplesIndex == 0:
			# Nothing to do
			return

		if self.model.numSamplesIndex <= 0:
			self.model.numSamplesIndex = 0
		else:
			self.model.numSamplesIndex = self.model.numSamplesIndex - 1

		self.sweepSampleChanged()


	def buttonIncSampSweep(self):
		if self.model.numSamplesIndex == len(self.model.numSamplesList) - 1:
			# Nothing to do
			return

		self.model.numSamplesIndex = self.model.numSamplesIndex + 1
		if self.model.numSamplesIndex >= len(self.model.numSamplesList):
			self.model.numSamplesIndex = len(self.model.numSamplesList) - 1

		self.sweepSampleChanged()

	def restartSweep(self):
		if self.hwhandler.hardware != None:
			self.hwhandler.hardware.resetSweep = True
		

	def sweepSampleChanged(self):
		self.setModeAsolute()
		self.model.setupArrays()
		self.graph.updateGraph()
		self.restartSweep()
		self.updateSweepLabel()


	def updateSweepLabel(self):
		count = self.model.numSamplesList[self.model.numSamplesIndex]
		self.sweepCountLabel.config(text=str(count - 1) + ' samples')

	def buttonDBDivInc(self):
		if self.model.dBDivIndex == len(self.model.dBDivList) - 1:
			# Nothing to do
			return

		self.model.dBDivIndex = self.model.dBDivIndex + 1
		if self.model.dBDivIndex >= len(self.model.dBDivList):
			self.model.dBDivIndex = len(self.model.dBDivList) - 1

		self.updateDbDiv()


	def buttonDBDivDec(self):
		if self.model.dBDivIndex == 0:
			# Nothing to do
			return

		if self.model.dBDivIndex <= 0:
			self.model.dBDivIndex = 0
		else:
			self.model.dBDivIndex = self.model.dBDivIndex - 1

		self.updateDbDiv()

	def updateDbDiv(self):
		self.graph.updateGraph()


		if self.model.measMode == 0:
			units = " dBm"
		if self.model.measMode == 1:
			units = " dB"

		db = self.model.dBDivList[self.model.dBDivIndex]
		self.dbPerDivLabel.config(text=str(db) + units)


	def buttonRefLevelIncTen(self):
		self.model.refLevel = self.model.refLevel + 10

		if self.model.refLevel >= 20:
			self.model.refLevel = 20

		self.updateRefPoint()


	def buttonRefLevelIncOne(self):
		self.model.refLevel = self.model.refLevel + 1

		if self.model.refLevel >= 20:
			self.model.refLevel = 20

		self.updateRefPoint()


	def buttonRefLevelAuto(self):
		minV, maxV = self.model.getMinMaxValues()
		div = self.model.dBDivList[self.model.dBDivIndex]

		## Currently fixed, on rescaling the div size, but not the count changes
		divCount = 8
		center = minV + (maxV - minV) / 2

		# Round to div position
		pos = center // div * div

		self.model.refLevel = pos + (divCount / 2 * div)

		self.updateRefPoint()


	def buttonRefLevelDecTen(self):
		self.model.refLevel = self.model.refLevel - 10

		if self.model.refLevel <= -60:
			self.model.refLevel = -60

		self.updateRefPoint()


	def buttonRefLevelDecOne(self):
		self.model.refLevel = self.model.refLevel - 1

		if self.model.refLevel <= -60:
			self.model.refLevel = -60

		self.updateRefPoint()


	def updateRefPoint(self):
		self.graph.updateGraph()

		if self.model.measMode == 0:
			units = " dBm"
		if self.model.measMode == 1:
			units = " dB"

		# Top
		txt = str(self.model.refLevel) + units
		self.refPointLabel1.config(text=txt)
		
		# Bottom
		db = self.model.dBDivList[self.model.dBDivIndex]
		txt = str(self.model.refLevel - self.model.vDiv * db) + units
		self.refPointLabel2.config(text=txt)


	def setModeAsolute(self):
		self.model.measMode = 0
		self.calibrationStateButton.config(image=self.calibrationNotCalibratedIcon)


	def setModeRelative(self):
		self.model.measMode = 1
		self.calibrationStateButton.config(image=self.calibrationCalibratedIcon)


	def setModeReferencing(self):
		self.model.measMode = 2
		self.calibrationStateButton.config(image=self.calibrationNotCalibratedIcon)

