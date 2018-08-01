from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import numpy as np
from time import sleep
import serial
import math
import threading

# ================ Variable Definitions ===============================
graphWidth = 1000
graphHeight = 500

graphLeftBuffer = 50
graphTopBuffer = 50
graphBottomBuffer = 50
graphRightBuffer = 20

graphAreaWidth = graphWidth+graphLeftBuffer+graphRightBuffer
graphAreaHeight = graphHeight+graphTopBuffer+graphBottomBuffer

hDiv = 10
vDiv = 8

graphColor = 'Green'
labelColor = 'White'
traceColor = 'Red'
textLabelColor = 'Yellow'
titleColor = 'LightBlue'

traceWidth = 1

dBDivList = [1, 2, 3, 5, 10]
dBDivIndex = 4

refLevel = 10

numSamplesList = [51, 101, 501, 1001]
numSamplesIndex = 0

startFreq = 1000000
stopFreq = 72000000

SERIALPORT = "/dev/tty.usbmodem641" # For the Mac
#SERIALPORT = "COM5"
BAUD = 115200

traceID = 0
resetSweep = FALSE
refReady = FALSE

measMode = 0 #0 for absolute, 1 for relative, 2 for create reference

# ================ Function Definitions ===============================

def UpdateGraph():
	graphItems = graph.find_all()
	for n in graphItems:
		graph.delete(n)
	
	MakeGraph()
	AddTextInfo()
	MakeTrace()

def MakeGraph():
	# Draw horizontal grid lines
	i = 0
	xL = graphLeftBuffer
	xR = graphLeftBuffer + graphWidth
	
	dB = refLevel
	dBStep = dBDivList[dBDivIndex]
	
	if measMode == 0:
		units = "dBm"
	if measMode == 1:
		units = "dB"
	
	while (i <= vDiv):
		y = graphTopBuffer + i*graphHeight/vDiv
		Dline = [xL,y,xR,y]
		graph.create_line(Dline, fill=graphColor)
		txt = str(dB) + units
		graph.create_text(graphLeftBuffer/2, y - 4, text = txt, fill=labelColor)
		dB = dB - dBStep
		i = i + 1

	# Draw vertical grid lines
	i = 0
	yT = graphTopBuffer
	yB = graphTopBuffer + graphHeight
	
	freq = startFreq
	freqStep = (stopFreq-startFreq)/10
	
	while (i <= hDiv):
		x = graphLeftBuffer + i*graphWidth/hDiv
		Dline = [x,yT,x,yB]
		graph.create_line(Dline, fill = graphColor)
		txt = str(np.round(freq/1000000,3))+'M'
		graph.create_text(x, graphTopBuffer+10+graphHeight, text = txt, fill=labelColor)
		freq = freq+freqStep
		i = i + 1

def AddTextInfo():
	
	yInfo = graphTopBuffer + graphHeight + graphBottomBuffer - 15
	
	txt = str(np.round(startFreq/1000000,3)) + "MHz to " + str(np.round(stopFreq/1000000,3)) + "MHz"
	graph.create_text(80, yInfo, text = txt, fill=textLabelColor)
	
	if measMode == 0:
		units = "dBm"
	if measMode == 1:
		units = "dB"
	
	txt = "Ref Level: " + str(refLevel) + units
	graph.create_text(250, yInfo, text = txt, fill=textLabelColor)
	
	txt = str(dBDivList[dBDivIndex]) + "dB/div"
	graph.create_text(400, yInfo, text = txt, fill=textLabelColor)
	
	if measMode == 0:
		txt = "Mode: Absolute"
	if measMode == 1:
		txt = "Mode: Relative"
	graph.create_text(700, yInfo, text = txt, fill=textLabelColor)
	
	txt = "Center: " + str(((stopFreq-startFreq)/2 + startFreq)/1000000) + "MHz"
	graph.create_text(graphWidth/2 + graphLeftBuffer, yInfo, text = txt, fill=textLabelColor)
	
	txt = str(numSamplesList[numSamplesIndex]-1) + " samples/sweep"
	graph.create_text(850, yInfo, text = txt, fill=textLabelColor)
	
	txt = "Scalar Network Analyzer"
	graph.create_text(graphWidth/2 + graphLeftBuffer, graphTopBuffer/2, text = txt, font=tkFont.Font(size=18), fill=titleColor)
	
def MakeTrace():
	global traceID
	global traceColor
	global traceWidth
	global trace
	global readings
	global reference
	global measMode
		
	if measMode == 0:
		trace[1::2] = graphTopBuffer + (refLevel - readings[1::2]) * (graphHeight / (vDiv * dBDivList[dBDivIndex]))
		np.clip(trace[1::2], graphTopBuffer, graphTopBuffer+graphHeight, out=trace[1::2])
		
		trace[::2] = graphLeftBuffer + (readings[::2] - startFreq) * (graphWidth / (stopFreq-startFreq))
		np.clip(trace[::2], graphLeftBuffer, graphLeftBuffer+graphWidth, out=trace[::2])
		
		tracePlot = trace.astype(int).tolist()
	
	if measMode == 1:
		trace[1::2] = graphTopBuffer + (refLevel - readings[1::2] + reference[1::2]) * (graphHeight / (vDiv * dBDivList[dBDivIndex]))
		np.clip(trace[1::2], graphTopBuffer, graphTopBuffer+graphHeight, out=trace[1::2])
		
		trace[::2] = graphLeftBuffer + (readings[::2] - startFreq) * (graphWidth / (stopFreq-startFreq))
		np.clip(trace[::2], graphLeftBuffer, graphLeftBuffer+graphWidth, out=trace[::2])
		
		tracePlot = trace.astype(int).tolist()
	
	graph.delete(traceID)
	traceID = graph.create_line(tracePlot, fill=traceColor, width = traceWidth)

def SetupArrays():
	global resetSweep
	global readings
	global trace
	global stopFreq
	global startFreq
	global numSamplesList
	global numSamplesIndex	
	global measMode
	global reference
	
	fStep = (stopFreq-startFreq)/(numSamplesList[numSamplesIndex]-1)
	
	readings = np.zeros(2*numSamplesList[numSamplesIndex])
	readings[::2] = np.arange(numSamplesList[numSamplesIndex]) * (fStep) + startFreq
	
	trace = np.zeros(2*numSamplesList[numSamplesIndex])
	
	if measMode == 2:
		reference = np.zeros(2*numSamplesList[numSamplesIndex])
	
	resetSweep = TRUE
	
def BdBDivInc():
	global dBDivIndex
	
	if dBDivIndex >=4:
		dBDivIndex = 4
	else:
		dBDivIndex = dBDivIndex + 1
	
	UpdateGraph()

def BdBDivDec():
	global dBDivIndex
	
	if dBDivIndex <=0:
		dBDivIndex = 0
	else:
		dBDivIndex = dBDivIndex - 1
	
	UpdateGraph()
	
def BrefLevelIncTen():
	global refLevel
	
	refLevel = refLevel + 10

	if refLevel >= 20:
		refLevel = 20
	
	UpdateGraph()

def BrefLevelDecTen():
	global refLevel
	

	refLevel = refLevel - 10
	
	if refLevel <= -60:
		refLevel = -60
		
	UpdateGraph()
	
def BrefLevelIncOne():
	global refLevel
	
	refLevel = refLevel + 1
	
	if refLevel >= 20:
		refLevel = 20	
	
	UpdateGraph()

def BrefLevelDecOne():
	global refLevel
	
	refLevel = refLevel - 1
	
	if refLevel <= -60:
		refLevel = -60
		
	UpdateGraph()

def BSetFreqs():
	global startFreq
	global stopFreq
	global measMode
	
	prompt = "Set the sweep starting frequency (MHz):"
	retVal = simpledialog.askfloat("Set Start Frequency", prompt, parent = root, initialvalue = startFreq/1000000, minvalue = 0, maxvalue = 72)
	if retVal is not None:
		startFreq = retVal*1000000
		
	prompt = "Set the sweep stopping frequency (MHz):"
	retVal = simpledialog.askfloat("Set Stop Frequency", prompt, parent = root, initialvalue = stopFreq/1000000, minvalue = 0, maxvalue = 72)
	if retVal is not None:
		stopFreq = retVal*1000000
	
	measMode = 0
	
	SetupArrays()
	UpdateGraph()
		
def BIncSampSweep():
	global numSamplesIndex
	global measMode
	
	if numSamplesIndex >= 5:
		numSamplesIndex = 5
	else:
		numSamplesIndex = numSamplesIndex + 1
	
	measMode = 0
	
	SetupArrays()
	UpdateGraph()
		
def BDecSampSweep():
	global numSamplesIndex
	global measMode
	
	if numSamplesIndex <= 0:
		numSamplesIndex = 0
	else:
		numSamplesIndex = numSamplesIndex - 1
	
	measMode = 0
	
	SetupArrays()
	UpdateGraph()
	
def BClose():
	root.destroy()
	sys.exit()

def BCalibrate():
	global measMode
	global refReady
	global reference
	global readings
	
	measMode = 2
		
	SetupArrays()
	
	txt = "Creating reference!"
	graph.create_text(graphWidth/2 + graphLeftBuffer, graphTopBuffer + graphHeight/2, text = txt, font=tkFont.Font(size=32), fill='Red')
	root.update()
	while refReady == FALSE:
		sleep(.001)
	
	reference[::] = readings[::]
	
	refReady = FALSE
	measMode = 1
	
	UpdateGraph()
	
# ================ Call main routines ===============================
def Sweep():
	while (True):
		# UpdateGraph()
		MakeTrace()
		root.update_idletasks()
		root.update()

class SerialReader(object):
	
	def __init__(self):
		self.adcValue = 0
		global BAUD
		global SERIALPORT
		
		try:
			self.serialPort = serial.Serial(SERIALPORT, BAUD, timeout=1)
			thread = threading.Thread(target=self.run)
			thread.daemon = True
			thread.start()
		except:
			messagebox.showinfo("Oh no!","Serial comms aren't working.")

	def run(self):
		global resetSweep
		global readings
		global refReady
		global measMode
		
		self.n = 0
		
		while True:			
			if resetSweep == TRUE:
				resetSweep = FALSE
				self.n = 0
									
			FTW = readings[self.n*2].astype(int).astype(str)+'\n'
			self.serialPort.write(FTW.encode()) 						# Send frequency command
			
			self.serialPort.write('p\n'.encode())						
			self.adcValue = self.serialPort.readline().decode().strip()

			if len(self.adcValue) != 0:
				readings[self.n*2+1] = float(self.adcValue) * .5*0.0488 - 90.5 #0.0488 or 0.1953 - 83.998
				self.n = self.n + 1
			
			if self.n >= numSamplesList[numSamplesIndex]:
				self.n = 0
				if measMode == 2:
					refReady = TRUE
					print("REF READY!")
				
# ================ Make Screen ===============================
root = Tk()
root.resizable(False, False)
root.title('Scalar Network Analyzer')

window = ttk.Frame(root, padding=5)
window.grid()
window.grid_columnconfigure(0, weight=1)

graphArea = ttk.Frame(window)
graphArea.grid(column=0, row=0)

graph = Canvas(graphArea, width=graphAreaWidth, height=graphAreaHeight, background='black')
graph.grid()

controlArea = ttk.LabelFrame(window, text="Controls", borderwidth=10)
controlArea.grid(column=0, row=1, sticky=(N,E,S,W))


b = ttk.Button(window, text="Close", width=15, command=BClose)
b.grid(column = 0, row=2, pady=15)


b = ttk.Button(controlArea, text="dB/div +", width=10, command=BdBDivInc)
b.grid(column = 0, row = 0)

b = ttk.Button(controlArea, text="dB/div -", width=10, command=BdBDivDec)
b.grid(column = 0, row = 1)

b = ttk.Button(controlArea, text="Ref Lvl +10", width=10, command=BrefLevelIncTen)
b.grid(column = 1, row = 0)

b = ttk.Button(controlArea, text="Ref Lvl -10", width=10, command=BrefLevelDecTen)
b.grid(column = 1, row = 1)

b = ttk.Button(controlArea, text="Ref Lvl +1", width=10, command=BrefLevelIncOne)
b.grid(column = 2, row = 0)

b = ttk.Button(controlArea, text="Ref Lvl -1", width=10, command=BrefLevelDecOne)
b.grid(column = 2, row = 1)

b = ttk.Button(controlArea, text="+ Samples", width=10, command=BIncSampSweep)
b.grid(column = 3, row = 0)

b = ttk.Button(controlArea, text="- Samples", width=10, command=BDecSampSweep)
b.grid(column = 3, row = 1)

b = ttk.Button(controlArea, text="Set Freqs", width=10, command=BSetFreqs)
b.grid(column = 4, row = 0)

b = ttk.Button(controlArea, text="Calibrate", width=10, command=BCalibrate)
b.grid(column = 5, row = 0)

# ================ Call main routine ===============================
root.update()

SetupArrays()

UpdateGraph()

serialObject = SerialReader()

Sweep()