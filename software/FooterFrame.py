#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from tkinter import *
import serial.tools.list_ports
from PIL import Image, ImageTk


class FooterFrame(object):
	def __init__(self, parent, hwhandler):
		self.hwhandler = hwhandler
		self.frame = Frame(parent, bd=1)
		self.frame.pack(fill=X)

		# Icons need to be kept, else the garbage collector deletes them
		self.icons = []

		label = Label(self.frame, text='Device:')
		label.pack(side=LEFT, padx=2, pady=2)

		self.initDeviceSelection()

		label = Label(self.frame, text='COM-Port:')
		label.pack(side=LEFT, padx=2, pady=2)


		self.initComPortSelection()

		label = Label(self.frame, text='Baud:')
		label.pack(side=LEFT, padx=2, pady=2)

		self.initComPortBaudSelection();

		image = Image.open("icon/apply-24.png")
		icon = ImageTk.PhotoImage(image)
		self.icons.append(icon)

		button = Button(self.frame, image=icon, relief=FLAT, command=lambda p=self: FooterFrame.buttonApplyHardwareConfig(p))
		button.pack(side=LEFT, padx=2, pady=2)

		label = Label(self.frame, text='State:')
		label.pack(side=LEFT, padx=2, pady=2)

		self.deviceStateLabel = Label(self.frame, text='Not connected')
		self.deviceStateLabel.pack(side=LEFT, padx=2, pady=2)


	def buttonApplyHardwareConfig(self):
		self.hwhandler.selectImplementationByIndex(self.devSelectDevice.current())


	def initDeviceSelection(self):
		self.devSelectDeviceVar = StringVar()
		self.devSelectDevice = ttk.Combobox(self.frame, textvariable=self.devSelectDeviceVar, state='readonly', width=14)
		self.devSelectDevice['values'] = self.hwhandler.getHwImplementationNames()
		self.devSelectDevice.current(self.hwhandler.getSelectedHwImplementationIndex())
		self.devSelectDevice.pack(side=LEFT, padx=2, pady=2)


	def initComPortSelection(self):
		self.devSelectPortVar = StringVar()
		self.devSelectPort = ttk.Combobox(self.frame, textvariable=self.devSelectPortVar)
		ports = []
		for p in serial.tools.list_ports.comports():
			ports.append(p.device + ': ' + p.description)

		self.devSelectPort['values'] = ports

		self.devSelectPort.pack(side=LEFT, padx=2, pady=2)


	def initComPortBaudSelection(self):
		self.devSelectBaudVar = StringVar()
		self.devSelectBaud = ttk.Combobox(self.frame, textvariable=self.devSelectBaudVar, width=7)
		self.devSelectBaud['values'] = ('115200', '9600', '19200', '38400', '57600')
		self.devSelectBaud.current(0)
		self.devSelectBaud.pack(side=LEFT, padx=2, pady=2)


	def setDeviceState(self, text):
		self.deviceStateLabel.config(text=text)




