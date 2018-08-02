#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License: GPL3


def getWindowCenter(win):
	win.update_idletasks()
	width = win.winfo_width()
	height = win.winfo_height()
	return win.winfo_x() + (width // 2), win.winfo_y() + (height // 2)

# Hide window before centering it
def hideWindow(win):
	#win.attributes('-alpha', 0.0)
	# Not working :-(
	pass

def centerWindowOnParent(win, parent):
	if parent is None:
		return

	win.update_idletasks()
	width = win.winfo_width()
	height = win.winfo_height()
	x , y = getWindowCenter(parent)

	win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
	win.deiconify()
	# Not working :-(
	#root.attributes('-alpha', 1.0)
	
