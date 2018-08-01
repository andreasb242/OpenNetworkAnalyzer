#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware
import random
from time import sleep


class Dummy(BaseHardware.BaseHardware):
	def __init__(self, settings, model):
		super().__init__(settings, model)

	# Read a single value, return True to continue, False to stop
	def readValue(self):
		sleep(.3)
		
		value = random.randint(-40, 10)
		self.model.readings[self.n * 2 + 1] = value


