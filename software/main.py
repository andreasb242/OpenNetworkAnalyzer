#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


import configparser
import SettingsDialog
import AnalyzerFrame

from hardware import Arduino
from hardware import Dummy

from tkinter import messagebox

## Configuration
settings = configparser.ConfigParser()
settings['settings'] = { 'version': '0' };
settings['hardware'] = {};

## Main entry point
if __name__ == '__main__':
	print("Starting up...")

	print("Read settings")
	settings.read('settings.ini')

	if settings['settings']['version'] != '1':
		print("First start with this version, show settings")
		settingsDialog = SettingsDialog.SettingsDialog(settings)
		settingsDialog.run()

	if settings['settings']['version'] == '1':
		print ("Startup application")
		
		hardware = None
		if settings['hardware']['type'] == 'dummy':
			hardware = Dummy.Dummy(settings)
		if settings['hardware']['type'] == 'arduino':
			hardware = Arduino.Arduino(settings)

		if hardware is None:
			messagebox.showerror("Error", "Configured hardware unknown")
		else:
			frame = AnalyzerFrame.AnalyzerFrame(settings)
			frame.run()

	print("Store settings")
	with open('settings.ini', 'w') as settingsfile:
		settings.write(settingsfile)
	print("Finsihed")

