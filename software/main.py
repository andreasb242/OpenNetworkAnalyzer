#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


import configparser
import AnalyzerFrame
import DataModel;

from tkinter import *

class Startup(object):
	def __init__(self):
		## Configuration
		self.settings = configparser.ConfigParser()
		self.settings['settings'] = {};
		self.settings['hardware'] = { 'type': 'none' };
		self.settings['view'] = { 'startFreq': '1000000', 'stopFreq': '72000000'};

		self.model = DataModel.DataModel()


	def readSettings(self):
		print("Read settings")
		self.settings.read('settings.ini')

		self.model.startFreq = int(self.settings['view']['startFreq']);
		self.model.stopFreq = int(self.settings['view']['stopFreq']);
		self.model.setupArrays()


	def storeSettings(self):
		print("Store settings")
		with open('settings.ini', 'w') as settingsfile:
			self.settings.write(settingsfile)


	def startup(self):
		# https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window#1407700
		self.mainRoot = Tk()
		self.mainRoot.overrideredirect(1)
		self.mainRoot.withdraw()

		frame = AnalyzerFrame.AnalyzerFrame(self.settings, self.model, self.mainRoot)
		frame.run()


## Main entry point
if __name__ == '__main__':
	print("Starting up...")

	startup = Startup()
	startup.readSettings()


	print ("Startup application")
	startup.startup()

	startup.storeSettings()
	print("Finsihed")



