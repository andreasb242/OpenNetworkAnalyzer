from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from time import sleep
import serial
import math
import threading



# ================ Call main routine ===============================
root.update()

SetupArrays()

UpdateGraph()

serialObject = SerialReader()

Sweep()
