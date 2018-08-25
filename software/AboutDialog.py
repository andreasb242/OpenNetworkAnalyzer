#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
from tkinter import ttk
from WinUtil import *

class AboutDialog(object):
	def __init__(self, parent):
		self.root = Tk(className='OpenNetworkAnalyzer_INFO')
		# Show the window after it is centered
		hideWindow(self.root)
		self.root.resizable(False, False)
		self.root.title('About')

		self.window = ttk.Frame(self.root, padding=5)
		self.window.grid()
		self.window.grid_columnconfigure(0, weight=1)

		label = Label(self.window, text='License', font="Sans 12 bold")
		label.grid(column=0, row=0)

		label = Label(self.window, text='GNU GPL Version 3', font="Sans 10")
		label.grid(column=0, row=1)

		label = Label(self.window, text='Authors', font="Sans 12 bold")
		label.grid(column=0, row=20)

		label = Label(self.window, text='Brett Killion © 2016 - Now\nAndreas Butti © 2018 - Now', font="Sans 10")
		label.grid(column=0, row=21)


		label = Label(self.window, text='Website', font="Sans 12 bold")
		label.grid(column=0, row=100)

		label = Label(self.window, text='https://github.com/andreasb242/OpenNetworkAnalyzer', font="Sans 10")
		label.grid(column=0, row=101)

		centerWindowOnParent(self.root, parent)


	def run(self):
		self.root.wait_window(self.window)
