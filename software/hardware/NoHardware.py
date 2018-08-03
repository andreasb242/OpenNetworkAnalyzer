#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware
import random
from time import sleep


class NoHardware(BaseHardware.BaseHardware):
	def __init__(self, settings, model):
		super().__init__(settings, model)


	def start(self, listener):
		self.listener = listener
		self.listener.hwUpdateConnectionState('Select a device...')


