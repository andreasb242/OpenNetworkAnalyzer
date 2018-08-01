#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


from hardware import BaseHardware

class Dummy(BaseHardware.BaseHardware):
	def __init__(self, settings):
		super().__init__(settings)

