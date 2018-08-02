#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


import numpy as np


class DataModel(object):
	def __init__(self):
		self.refLevel = 10;

		self.dBDivList = [1, 2, 3, 5, 10]
		self.dBDivIndex = 4

		self.numSamplesList = [51, 101, 501, 1001]
		self.numSamplesIndex = 0

		## 0 for absolute, 1 for relative, 2 for create reference
		self.measMode = 0
		
		self.hDiv = 10
		self.vDiv = 8

		self.startFreq = 1000000
		self.stopFreq = 72000000
		
		## Last updated index by hardware
		self.lastUpdatedIndex = 0

		self.setupArrays()

	def setupArrays(self):
		fStep = (self.stopFreq - self.startFreq) / (self.numSamplesList[self.numSamplesIndex] - 1)
	
		self.readings = np.zeros(2 * self.numSamplesList[self.numSamplesIndex])
		self.readings[::2] = np.arange(self.numSamplesList[self.numSamplesIndex]) * (fStep) + self.startFreq
	
		self.trace = np.zeros(2 * self.numSamplesList[self.numSamplesIndex])
	
		if self.measMode == 2:
			reference = np.zeros(2 * self.numSamplesList[self.numSamplesIndex])
	
		resetSweep = True


