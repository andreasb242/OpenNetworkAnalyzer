#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
import numpy as np
from tkinter import font as tkFont


class OutputGraph(object):
	def __init__(self, parent, model):
		self.graphHeight = 500
		self.graphWidth = 1000
		
		self.graphRightBuffer = 20
		self.graphLeftBuffer = 50
		self.graphTopBuffer = 20
		self.graphBottomBuffer = 20

		graphAreaWidth = self.graphWidth + self.graphLeftBuffer + self.graphRightBuffer
		graphAreaHeight = self.graphHeight + self.graphTopBuffer + self.graphBottomBuffer
	
		self.graph = Canvas(parent, width=graphAreaWidth, height=graphAreaHeight, background='black')
		self.model = model;
		self.graph.bind("<Configure>", self.onResize)

		self.graphColor = 'Green'
		self.labelColor = 'White'
		self.traceColor = 'Red'
		self.scanColor = '#E1EC4F'
		self.textLabelColor = 'Yellow'
		self.titleColor = 'LightBlue'
		
		self.traceWidth = 1

		self.traceID = 0
		self.traceMakerID = 0


	def onResize(self, event):
		self.graphWidth = event.width - self.graphRightBuffer - self.graphLeftBuffer
		self.graphHeight = event.height - self.graphTopBuffer - self.graphBottomBuffer
		self.updateGraph()
		

	def updateGraph(self):
		graphItems = self.graph.find_all()
		for n in graphItems:
			self.graph.delete(n)

		self.makeGraph()
		self.makeTrace()


	## Add temporaray info text to center of the graph
	def addCenterInfoText(self, text):
		self.graph.create_text(self.graphWidth / 2 + self.graphLeftBuffer, self.graphTopBuffer + self.graphHeight / 2, text=text, font=tkFont.Font(size=32), fill='Red')


	def makeGraph(self):
		# Draw horizontal grid lines
		i = 0
		xL = self.graphLeftBuffer
		xR = self.graphLeftBuffer + self.graphWidth

		dB = self.model.refLevel
		dBStep = self.model.dBDivList[self.model.dBDivIndex]

		if self.model.measMode == 0:
			units = "dBm"
		if self.model.measMode == 1:
			units = "dB"

		while (i <= self.model.vDiv):
			y = self.graphTopBuffer + i * self.graphHeight / self.model.vDiv
			Dline = [xL, y, xR, y]
			self.graph.create_line(Dline, fill=self.graphColor)
			txt = str(dB) + units
			self.graph.create_text(self.graphLeftBuffer / 2, y - 4, text=txt, fill=self.labelColor)
			dB = dB - dBStep
			i = i + 1

		# Draw vertical grid lines
		i = 0
		yT = self.graphTopBuffer
		yB = self.graphTopBuffer + self.graphHeight

		freq = self.model.startFreq
		freqStep = (self.model.stopFreq - self.model.startFreq) / 10

		while (i <= self.model.hDiv):
			x = self.graphLeftBuffer + i * self.graphWidth / self.model.hDiv
			Dline = [x, yT, x, yB]
			self.graph.create_line(Dline, fill=self.graphColor)
			txt = str(np.round(freq / 1000000, 3)) + 'M'
			self.graph.create_text(x, self.graphTopBuffer + 10 + self.graphHeight, text=txt, fill=self.labelColor)
			freq = freq + freqStep
			i = i + 1


	def makeTrace(self):
		# Absoulute (0) or reference mesasure (2)
		if self.model.measMode == 0 or self.model.measMode == 2:
			self.model.trace[1::2] = self.graphTopBuffer + (self.model.refLevel - self.model.readings[1::2]) * (self.graphHeight / (self.model.vDiv * self.model.dBDivList[self.model.dBDivIndex]))
			np.clip(self.model.trace[1::2], self.graphTopBuffer, self.graphTopBuffer + self.graphHeight, out=self.model.trace[1::2])

			self.model.trace[::2] = self.graphLeftBuffer + (self.model.readings[::2] - self.model.startFreq) * (self.graphWidth / (self.model.stopFreq - self.model.startFreq))
			np.clip(self.model.trace[::2], self.graphLeftBuffer, self.graphLeftBuffer + self.graphWidth, out=self.model.trace[::2])

			tracePlot = self.model.trace.astype(int).tolist()

		# Relative to calibration reference
		if self.model.measMode == 1:
			self.model.trace[1::2] = self.graphTopBuffer + (self.model.refLevel - self.model.readings[1::2] + self.model.reference[1::2]) * (self.graphHeight / (self.model.vDiv * self.model.dBDivList[self.model.dBDivIndex]))
			np.clip(self.model.trace[1::2], self.graphTopBuffer, self.graphTopBuffer+self.graphHeight, out=self.model.trace[1::2])

			self.model.trace[::2] = self.graphLeftBuffer + (self.model.readings[::2] - self.model.startFreq) * (self.graphWidth / (self.model.stopFreq - self.model.startFreq))
			np.clip(self.model.trace[::2], self.graphLeftBuffer, self.graphLeftBuffer + self.graphWidth, out=self.model.trace[::2])

			tracePlot = self.model.trace.astype(int).tolist()

		# Marker for current scan
		self.graph.delete(self.traceMakerID)
		if self.model.showMarkerLine:
			x = self.graphLeftBuffer + self.model.lastUpdatedIndex * self.graphWidth / len(tracePlot) * 2
			Dline = [x, self.graphTopBuffer, x, self.graphTopBuffer + self.graphHeight]
			self.traceMakerID = self.graph.create_line(Dline, fill=self.scanColor)

		## Print Graph
		self.graph.delete(self.traceID)
		self.traceID = self.graph.create_line(tracePlot, fill=self.traceColor, width=self.traceWidth)









