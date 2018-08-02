#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import ttk
from WinUtil import *


class SettingsDialog(object):
	def __init__(self, settings, parent):
		self.settings = settings;
		self.stored = False

		self.root = Tk()
		# Show the window after it is centered
		hideWindow(self.root)
		self.root.resizable(False, False)
		self.root.title('Settings')

		self.window = ttk.Frame(self.root, padding=5)
		self.window.grid()
		self.window.grid_columnconfigure(0, weight=1)

		bt = ttk.Button(self.window, text="Cancel", width=15, command=lambda p=self: SettingsDialog.windowClose(p))
		bt.grid(column=0, row=100, pady=15)
		bt = ttk.Button(self.window, text="Apply", width=15, command=lambda p=self: SettingsDialog.applyChanges(p))
		bt.grid(column=1, row=100, pady=15)

		label = Label(self.window, text='Select Device')
		label.grid(column=0, row=0, columnspan=2)

		self.selectedTypeVar = StringVar()
		self.selectedType = ttk.Combobox(self.window, textvariable=self.selectedTypeVar, state='readonly')
		self.selectedType['values'] = ('Dummy (no hardware)', 'Arduino')
		self.selectedType.current(0)
		self.selectedType.grid(column=0, row=1, columnspan=2)

		centerWindowOnParent(self.root, parent)


	def windowClose(self):
		self.root.destroy()


	def applyChanges(self):
		self.stored = True
		if self.selectedType.current() == 0:
			self.settings['hardware']['type'] = 'dummy';
		if self.selectedType.current() == 1:
			self.settings['hardware']['type'] = 'arduino';

		self.settings['settings']['version'] = '1';
		self.root.destroy()


	def run(self):
		self.root.wait_window(self.window)




