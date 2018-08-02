#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


import configparser
import SettingsDialog
import AnalyzerFrame
import DataModel;

from hardware import Arduino
from hardware import Dummy

from tkinter import messagebox
from tkinter import *

class Startup(object):
	def __init__(self):
		## Configuration
		self.settings = configparser.ConfigParser()
		self.settings['settings'] = { 'version': '0' };
		self.settings['hardware'] = {};

		self.model = DataModel.DataModel()

	def readSettings(self):
		print("Read settings")
		self.settings.read('settings.ini')
		
		if self.settings['settings']['version'] != '1':
			print("First start with this version, show settings")
			settingsDialog = SettingsDialog.SettingsDialog(self.settings)
			settingsDialog.run()

	def storeSettings(self):
		print("Store settings")
		with open('settings.ini', 'w') as settingsfile:
			self.settings.write(settingsfile)

	def initHardware(self):
		self.hardware = None
		hwType = self.settings['hardware']['type']
		try:
			if hwType == 'dummy':
				self.hardware = Dummy.Dummy(self.settings, self.model)
			elif hwType == 'arduino':
				self.hardware = Arduino.Arduino(self.settings, self.model)
			else:
				return False

		except BaseException as e:
			s = str(e)
			messagebox.showinfo("Hardware Init Error", "Could not init Hardware Instance «" + hwType + "»\n" + s)
			return False
		
		return True

	def startup(self):
		# https://stackoverflow.com/questions/1406145/how-do-i-get-rid-of-python-tkinter-root-window#1407700
		self.mainRoot = Tk()
		self.mainRoot.overrideredirect(1)
		self.mainRoot.withdraw()

		while self.initHardware() == False:
			settingsDialog = SettingsDialog.SettingsDialog(self.settings)
			settingsDialog.run()
			if settingsDialog.stored == False:
				break
			
		if self.hardware is None:
			messagebox.showerror("Error", "Configured hardware unknown")
			return False
		else:
			frame = AnalyzerFrame.AnalyzerFrame(self.settings, self.hardware, self.model, self.mainRoot)
			frame.run()
			return frame.restart;

## Main entry point
if __name__ == '__main__':
	print("Starting up...")

	startup = Startup()
	startup.readSettings()


	if startup.settings['settings']['version'] == '1':
		print ("Startup application")
		
		# Restart to load new settings
		while startup.startup() == True:
			startup.storeSettings()

	else:
		print ('Settings not confirmed, quit now')

	startup.storeSettings()
	print("Finsihed")



