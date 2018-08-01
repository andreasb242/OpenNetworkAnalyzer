EESchema Schematic File Version 4
LIBS:ArduinoSpecAn-cache
EELAYER 26 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 1 1
Title "Arduino Scalar Network Analyzer Shield"
Date "2015-12-23"
Rev "1.0"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L ArduinoSpecAn-rescue:AD8307 U1
U 1 1 567AEDE5
P 8750 3600
F 0 "U1" H 8950 3350 60  0000 C CNN
F 1 "AD8307" H 8750 3850 60  0000 C CNN
F 2 "SMD_Packages:SOIC-8-N" H 8750 3650 60  0001 C CNN
F 3 "" H 8750 3650 60  0000 C CNN
	1    8750 3600
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:AD9851 U2
U 1 1 567AF1E6
P 3300 1600
F 0 "U2" H 3650 850 60  0000 C CNN
F 1 "AD9851" H 3300 2350 60  0000 C CNN
F 2 "Housings_SSOP:SSOP-28_5.3x10.2mm_Pitch0.65mm" H 3300 1600 60  0001 C CNN
F 3 "" H 3300 1600 60  0000 C CNN
	1    3300 1600
	1    0    0    -1  
$EndComp
Text Label 2550 4400 2    60   ~ 0
A0
$Comp
L ArduinoSpecAn-rescue:C_Small C2
U 1 1 567B2606
P 8150 3200
F 0 "C2" H 8160 3270 50  0000 L CNN
F 1 "10uF" H 8160 3120 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8150 3200 60  0001 C CNN
F 3 "" H 8150 3200 60  0000 C CNN
	1    8150 3200
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C4
U 1 1 567B275A
P 9350 3200
F 0 "C4" H 9360 3270 50  0000 L CNN
F 1 "10uF" H 9360 3120 50  0000 L CNN
F 2 "footprints:Custom_0805" H 9350 3200 60  0001 C CNN
F 3 "" H 9350 3200 60  0000 C CNN
	1    9350 3200
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R2
U 1 1 567B27BA
P 8750 2900
F 0 "R2" V 8850 2850 50  0000 L CNN
F 1 "51" V 8650 2850 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8750 2900 60  0001 C CNN
F 3 "" H 8750 2900 60  0000 C CNN
	1    8750 2900
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR02
U 1 1 567B2AA5
P 7650 3150
F 0 "#PWR02" H 7650 2900 50  0001 C CNN
F 1 "GND" H 7650 3000 50  0000 C CNN
F 2 "" H 7650 3150 60  0000 C CNN
F 3 "" H 7650 3150 60  0000 C CNN
	1    7650 3150
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:SMA J1
U 1 1 567B2CEE
P 9950 2900
F 0 "J1" H 9750 2800 60  0000 C CNN
F 1 "SMA" H 9950 3100 60  0000 C CNN
F 2 "footprints:SMA_Edgemount" H 9950 2900 60  0001 C CNN
F 3 "" H 9950 2900 60  0000 C CNN
	1    9950 2900
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR03
U 1 1 567B2DB3
P 9950 3350
F 0 "#PWR03" H 9950 3100 50  0001 C CNN
F 1 "GND" H 9950 3200 50  0000 C CNN
F 2 "" H 9950 3350 60  0000 C CNN
F 3 "" H 9950 3350 60  0000 C CNN
	1    9950 3350
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R3
U 1 1 567B2F06
P 9700 3650
F 0 "R3" V 9800 3600 50  0000 L CNN
F 1 "4R7" V 9600 3600 50  0000 L CNN
F 2 "footprints:Custom_0805" H 9700 3650 60  0001 C CNN
F 3 "" H 9700 3650 60  0000 C CNN
	1    9700 3650
	0    -1   -1   0   
$EndComp
NoConn ~ 9200 3750
NoConn ~ 8300 3650
$Comp
L power:GND #PWR04
U 1 1 567B32D9
P 8200 4000
F 0 "#PWR04" H 8200 3750 50  0001 C CNN
F 1 "GND" H 8200 3850 50  0000 C CNN
F 2 "" H 8200 4000 60  0000 C CNN
F 3 "" H 8200 4000 60  0000 C CNN
	1    8200 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 4800 2300 4800
Wire Wire Line
	3100 4900 2300 4900
Wire Wire Line
	8150 3100 8150 2900
Wire Wire Line
	7650 2900 8150 2900
Wire Wire Line
	8850 2900 9350 2900
Wire Wire Line
	9350 2900 9350 3100
Wire Wire Line
	8150 3300 8150 3450
Wire Wire Line
	8150 3450 8300 3450
Wire Wire Line
	9200 3450 9350 3450
Wire Wire Line
	9350 3450 9350 3300
Wire Wire Line
	7650 3150 7650 2900
Connection ~ 8150 2900
Connection ~ 9350 2900
Text Label 9350 2900 0    60   ~ 0
Input
Wire Wire Line
	9800 3650 9950 3650
Text Label 9950 3650 0    60   ~ 0
5V
Text Label 7750 3750 0    60   ~ 0
Vmag
Text Label 7800 4450 0    60   ~ 0
Vmag
Text Label 8650 4200 2    60   ~ 0
5V
$Comp
L power:GND #PWR05
U 1 1 567B5123
P 8650 5000
F 0 "#PWR05" H 8650 4750 50  0001 C CNN
F 1 "GND" H 8650 4850 50  0000 C CNN
F 2 "" H 8650 5000 60  0000 C CNN
F 3 "" H 8650 5000 60  0000 C CNN
	1    8650 5000
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:LM7301 U3
U 1 1 567B52F9
P 8650 4600
F 0 "U3" H 8900 4350 60  0000 C CNN
F 1 "LM7301" H 8950 4800 60  0000 C CNN
F 2 "Housings_SOT-23_SOT-143_TSOT-6:SOT-23-5" H 8650 4550 60  0001 C CNN
F 3 "" H 8650 4550 60  0000 C CNN
	1    8650 4600
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:KC5032A X1
U 1 1 567B611F
P 1350 1700
F 0 "X1" H 1500 1550 60  0000 C CNN
F 1 "KC5032A" H 1350 1850 60  0000 C CNN
F 2 "footprints:KC5032A-CM_SMD_Crystal" H 1350 1700 60  0001 C CNN
F 3 "" H 1350 1700 60  0000 C CNN
	1    1350 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	950  1650 850  1650
Wire Wire Line
	850  1650 850  1450
Wire Wire Line
	600  1450 850  1450
Wire Wire Line
	1850 1300 1850 1450
Wire Wire Line
	1850 1650 1750 1650
Connection ~ 1850 1450
Text Label 1850 1300 0    60   ~ 0
5V
$Comp
L power:GND #PWR06
U 1 1 567B632A
P 900 2000
F 0 "#PWR06" H 900 1750 50  0001 C CNN
F 1 "GND" H 900 1850 50  0000 C CNN
F 2 "" H 900 2000 60  0000 C CNN
F 3 "" H 900 2000 60  0000 C CNN
	1    900  2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	900  1750 900  1950
Wire Wire Line
	900  1750 950  1750
$Comp
L ArduinoSpecAn-rescue:C_Small C1
U 1 1 567B63B5
P 600 1750
F 0 "C1" H 610 1820 50  0000 L CNN
F 1 ".01uF" H 610 1670 50  0000 L CNN
F 2 "footprints:Custom_0805" H 600 1750 60  0001 C CNN
F 3 "" H 600 1750 60  0000 C CNN
	1    600  1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	600  1650 600  1450
Connection ~ 850  1450
Wire Wire Line
	600  1850 600  1950
Wire Wire Line
	600  1950 900  1950
Connection ~ 900  1950
Wire Wire Line
	1750 1750 2700 1750
Wire Wire Line
	3900 1250 4100 1250
Text Label 4100 1250 2    60   ~ 0
SDA
Wire Wire Line
	2700 1550 2300 1550
Text Label 2300 1550 0    60   ~ 0
SCL
Wire Wire Line
	2700 1650 2300 1650
Text Label 2300 1650 0    60   ~ 0
SLD
NoConn ~ 2700 2150
NoConn ~ 2700 2250
NoConn ~ 3900 2050
$Comp
L power:GND #PWR07
U 1 1 567B700B
P 4400 2600
F 0 "#PWR07" H 4400 2350 50  0001 C CNN
F 1 "GND" H 4400 2450 50  0000 C CNN
F 2 "" H 4400 2600 60  0000 C CNN
F 3 "" H 4400 2600 60  0000 C CNN
	1    4400 2600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 950  4400 950 
Wire Wire Line
	4400 950  4400 1050
Wire Wire Line
	3900 2150 4400 2150
Connection ~ 4400 2150
Wire Wire Line
	3900 2250 4400 2250
Connection ~ 4400 2250
Wire Wire Line
	3900 1350 4400 1350
Connection ~ 4400 1350
Wire Wire Line
	3900 1150 4400 1150
Connection ~ 4400 1150
Wire Wire Line
	3900 1050 4400 1050
Connection ~ 4400 1050
Wire Wire Line
	3900 1550 4400 1550
Connection ~ 4400 1550
Wire Wire Line
	3900 1850 4400 1850
Connection ~ 4400 1850
$Comp
L ArduinoSpecAn-rescue:R_Small R9
U 1 1 567B73DA
P 4750 2150
F 0 "R9" H 4780 2170 50  0000 L CNN
F 1 "50" H 4780 2110 50  0000 L CNN
F 2 "footprints:Custom_0805" H 4750 2150 60  0001 C CNN
F 3 "" H 4750 2150 60  0000 C CNN
	1    4750 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 1750 4750 1750
Wire Wire Line
	4750 1750 4750 2050
Wire Wire Line
	4750 2250 4750 2500
Wire Wire Line
	4750 2500 4400 2500
Connection ~ 4400 2500
$Comp
L ArduinoSpecAn-rescue:C_Small C7
U 1 1 567B75BC
P 5600 1900
F 0 "C7" H 5610 1970 50  0000 L CNN
F 1 "10pF" H 5610 1820 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5600 1900 60  0001 C CNN
F 3 "" H 5600 1900 60  0000 C CNN
	1    5600 1900
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C8
U 1 1 567B7631
P 6000 1900
F 0 "C8" H 6010 1970 50  0000 L CNN
F 1 "39pF" H 6010 1820 50  0000 L CNN
F 2 "footprints:Custom_0805" H 6000 1900 60  0001 C CNN
F 3 "" H 6000 1900 60  0000 C CNN
	1    6000 1900
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C9
U 1 1 567B7691
P 6400 1900
F 0 "C9" H 6410 1970 50  0000 L CNN
F 1 "39pF" H 6410 1820 50  0000 L CNN
F 2 "footprints:Custom_0805" H 6400 1900 60  0001 C CNN
F 3 "" H 6400 1900 60  0000 C CNN
	1    6400 1900
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C10
U 1 1 567B76E7
P 6800 1900
F 0 "C10" H 6810 1970 50  0000 L CNN
F 1 "10pF" H 6810 1820 50  0000 L CNN
F 2 "footprints:Custom_0805" H 6800 1900 60  0001 C CNN
F 3 "" H 6800 1900 60  0000 C CNN
	1    6800 1900
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:L_Small L1
U 1 1 567B781E
P 5800 1650
F 0 "L1" H 5830 1690 50  0000 L CNN
F 1 "270nH" H 5830 1610 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5800 1650 60  0001 C CNN
F 3 "" H 5800 1650 60  0000 C CNN
	1    5800 1650
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:L_Small L2
U 1 1 567B7A95
P 6200 1650
F 0 "L2" H 6230 1690 50  0000 L CNN
F 1 "470nH" H 6230 1610 50  0000 L CNN
F 2 "footprints:Custom_0805" H 6200 1650 60  0001 C CNN
F 3 "" H 6200 1650 60  0000 C CNN
	1    6200 1650
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:L_Small L3
U 1 1 567B7C20
P 6600 1650
F 0 "L3" H 6630 1690 50  0000 L CNN
F 1 "270nH" H 6630 1610 50  0000 L CNN
F 2 "footprints:Custom_0805" H 6600 1650 60  0001 C CNN
F 3 "" H 6600 1650 60  0000 C CNN
	1    6600 1650
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R10
U 1 1 567B7F0E
P 5300 1900
F 0 "R10" H 5330 1920 50  0000 L CNN
F 1 "100" H 5330 1860 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5300 1900 60  0001 C CNN
F 3 "" H 5300 1900 60  0000 C CNN
	1    5300 1900
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R13
U 1 1 567B7F96
P 7100 1900
F 0 "R13" H 7130 1920 50  0000 L CNN
F 1 "100" H 7130 1860 50  0000 L CNN
F 2 "footprints:Custom_0805" H 7100 1900 60  0001 C CNN
F 3 "" H 7100 1900 60  0000 C CNN
	1    7100 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 1650 5300 1650
Wire Wire Line
	5300 1650 5300 1800
Connection ~ 5300 1650
Wire Wire Line
	5900 1650 6000 1650
Wire Wire Line
	6300 1650 6400 1650
Wire Wire Line
	6700 1650 6800 1650
Wire Wire Line
	6800 1650 6800 1800
Wire Wire Line
	6400 1800 6400 1650
Connection ~ 6400 1650
Wire Wire Line
	6000 1800 6000 1650
Connection ~ 6000 1650
Wire Wire Line
	5600 1800 5600 1650
Connection ~ 5600 1650
Wire Wire Line
	7100 1650 7100 1800
Connection ~ 6800 1650
Wire Wire Line
	7100 2200 7100 2000
Wire Wire Line
	5300 2200 5600 2200
Wire Wire Line
	5300 2200 5300 2000
Wire Wire Line
	5600 2000 5600 2200
Connection ~ 5600 2200
Wire Wire Line
	6000 2000 6000 2200
Connection ~ 6000 2200
Wire Wire Line
	6400 2000 6400 2200
Connection ~ 6400 2200
Wire Wire Line
	6800 2000 6800 2200
Connection ~ 6800 2200
$Comp
L power:GND #PWR08
U 1 1 567B904B
P 6200 2300
F 0 "#PWR08" H 6200 2050 50  0001 C CNN
F 1 "GND" H 6200 2150 50  0000 C CNN
F 2 "" H 6200 2300 60  0000 C CNN
F 3 "" H 6200 2300 60  0000 C CNN
	1    6200 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 2300 6200 2200
Connection ~ 6200 2200
Connection ~ 7100 1650
Text Label 7300 1650 2    60   ~ 0
RF
$Comp
L ArduinoSpecAn-rescue:R_Small R1
U 1 1 567B9D46
P 1900 2500
F 0 "R1" H 1930 2520 50  0000 L CNN
F 1 "3k92" H 1930 2460 50  0000 L CNN
F 2 "footprints:Custom_0805" H 1900 2500 60  0001 C CNN
F 3 "" H 1900 2500 60  0000 C CNN
	1    1900 2500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 567B9E90
P 1900 2700
F 0 "#PWR09" H 1900 2450 50  0001 C CNN
F 1 "GND" H 1900 2550 50  0000 C CNN
F 2 "" H 1900 2700 60  0000 C CNN
F 3 "" H 1900 2700 60  0000 C CNN
	1    1900 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 2600 1900 2700
Wire Wire Line
	1900 2400 1900 2050
Wire Wire Line
	1900 2050 2700 2050
$Comp
L power:GND #PWR010
U 1 1 567BA433
P 2250 2700
F 0 "#PWR010" H 2250 2450 50  0001 C CNN
F 1 "GND" H 2250 2550 50  0000 C CNN
F 2 "" H 2250 2700 60  0000 C CNN
F 3 "" H 2250 2700 60  0000 C CNN
	1    2250 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 1850 2700 1850
Wire Wire Line
	2250 950  2250 1050
Wire Wire Line
	2700 1350 2250 1350
Connection ~ 2250 1850
Wire Wire Line
	2700 1050 2250 1050
Connection ~ 2250 1350
Wire Wire Line
	2700 950  2250 950 
Connection ~ 2250 1050
Wire Wire Line
	2600 1950 2700 1950
Wire Wire Line
	2600 600  2600 1150
Wire Wire Line
	2700 1450 2600 1450
Connection ~ 2600 1450
Wire Wire Line
	2700 1250 2600 1250
Connection ~ 2600 1250
Wire Wire Line
	2700 1150 2600 1150
Connection ~ 2600 1150
Text Label 2600 600  0    60   ~ 0
5V
Wire Wire Line
	3900 1450 4250 1450
Text Label 4250 1450 2    60   ~ 0
5V
Wire Wire Line
	3900 1950 4250 1950
Text Label 4250 1950 2    60   ~ 0
5V
Wire Wire Line
	9200 3650 9300 3650
Wire Wire Line
	9200 3550 9300 3550
Wire Wire Line
	9300 3550 9300 3650
Connection ~ 9300 3650
$Comp
L ArduinoSpecAn-rescue:C_Small C11
U 1 1 567C5D7E
P 7750 1850
F 0 "C11" H 7760 1920 50  0000 L CNN
F 1 ".1uF" H 7760 1770 50  0000 L CNN
F 2 "footprints:Custom_0805" H 7750 1850 60  0001 C CNN
F 3 "" H 7750 1850 60  0000 C CNN
	1    7750 1850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C12
U 1 1 567C6091
P 8000 1850
F 0 "C12" H 8010 1920 50  0000 L CNN
F 1 ".1uF" H 8010 1770 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8000 1850 60  0001 C CNN
F 3 "" H 8000 1850 60  0000 C CNN
	1    8000 1850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C13
U 1 1 567C6113
P 8250 1850
F 0 "C13" H 8260 1920 50  0000 L CNN
F 1 ".1uF" H 8260 1770 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8250 1850 60  0001 C CNN
F 3 "" H 8250 1850 60  0000 C CNN
	1    8250 1850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C14
U 1 1 567C619C
P 8500 1850
F 0 "C14" H 8510 1920 50  0000 L CNN
F 1 ".1uF" H 8510 1770 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8500 1850 60  0001 C CNN
F 3 "" H 8500 1850 60  0000 C CNN
	1    8500 1850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C15
U 1 1 567C6228
P 8750 1850
F 0 "C15" H 8760 1920 50  0000 L CNN
F 1 ".1uF" H 8760 1770 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8750 1850 60  0001 C CNN
F 3 "" H 8750 1850 60  0000 C CNN
	1    8750 1850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C5
U 1 1 567C63EB
P 9400 3950
F 0 "C5" H 9410 4020 50  0000 L CNN
F 1 ".1uF" H 9410 3870 50  0000 L CNN
F 2 "footprints:Custom_0805" H 9400 3950 60  0001 C CNN
F 3 "" H 9400 3950 60  0000 C CNN
	1    9400 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 1750 7750 1650
Wire Wire Line
	7750 1650 8000 1650
Wire Wire Line
	7750 1950 7750 2050
Wire Wire Line
	7750 2050 8000 2050
Wire Wire Line
	8000 1950 8000 2050
Connection ~ 8000 2050
Wire Wire Line
	8250 1950 8250 2050
Connection ~ 8250 2050
Wire Wire Line
	8500 1950 8500 2050
Connection ~ 8500 2050
Wire Wire Line
	8000 1750 8000 1650
Connection ~ 8000 1650
Wire Wire Line
	8250 1750 8250 1650
Connection ~ 8250 1650
Wire Wire Line
	8500 1650 8500 1750
Connection ~ 8500 1650
$Comp
L power:GND #PWR011
U 1 1 567C76A2
P 8500 2200
F 0 "#PWR011" H 8500 1950 50  0001 C CNN
F 1 "GND" H 8500 2050 50  0000 C CNN
F 2 "" H 8500 2200 60  0000 C CNN
F 3 "" H 8500 2200 60  0000 C CNN
	1    8500 2200
	1    0    0    -1  
$EndComp
Text Label 8750 1500 0    60   ~ 0
5V
Text Notes 9050 2050 0    60   ~ 0
Decoupling Caps:\n\n- LM7301 x 1\n- AD9851 x 4
Text Notes 5750 1300 0    60   ~ 0
72MHz Butterworth LPF\nMatched to 100 Ohms
Wire Wire Line
	9250 4600 9500 4600
Wire Wire Line
	9500 4600 9500 5350
Wire Wire Line
	8050 4750 8050 5350
Wire Wire Line
	8050 4750 8150 4750
Wire Wire Line
	7800 4450 8150 4450
Connection ~ 9500 4600
Text Label 9650 4600 2    60   ~ 0
A0
Wire Wire Line
	8300 3550 8200 3550
Wire Wire Line
	8200 3550 8200 4000
Wire Wire Line
	7750 3750 8300 3750
Wire Wire Line
	9800 3250 9800 3300
Wire Wire Line
	9800 3300 9900 3300
Wire Wire Line
	10100 3300 10100 3250
Wire Wire Line
	9900 3250 9900 3300
Connection ~ 9900 3300
Wire Wire Line
	10000 3250 10000 3300
Connection ~ 10000 3300
Wire Wire Line
	9950 3350 9950 3300
Connection ~ 9950 3300
$Comp
L ArduinoSpecAn-rescue:R_Small R15
U 1 1 567C1CD7
P 2850 4600
F 0 "R15" H 2880 4620 50  0000 L CNN
F 1 "2k" H 2880 4560 50  0000 L CNN
F 2 "footprints:Custom_0805" H 2850 4600 60  0001 C CNN
F 3 "" H 2850 4600 60  0000 C CNN
	1    2850 4600
	-1   0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R14
U 1 1 567C1D6D
P 3100 4600
F 0 "R14" H 3130 4620 50  0000 L CNN
F 1 "2k" H 3130 4560 50  0000 L CNN
F 2 "footprints:Custom_0805" H 3100 4600 60  0001 C CNN
F 3 "" H 3100 4600 60  0000 C CNN
	1    3100 4600
	-1   0    0    -1  
$EndComp
Text Label 2850 4250 0    60   ~ 0
5V
Wire Wire Line
	9400 3850 9400 3650
Connection ~ 9400 3650
$Comp
L power:GND #PWR012
U 1 1 567C5089
P 9400 4100
F 0 "#PWR012" H 9400 3850 50  0001 C CNN
F 1 "GND" H 9400 3950 50  0000 C CNN
F 2 "" H 9400 4100 60  0000 C CNN
F 3 "" H 9400 4100 60  0000 C CNN
	1    9400 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 4100 9400 4050
Wire Wire Line
	3100 4900 3100 4700
Wire Wire Line
	2850 4700 2850 4800
Wire Wire Line
	2850 4250 2850 4400
Wire Wire Line
	3100 4500 3100 4400
Wire Wire Line
	3100 4400 2850 4400
Connection ~ 2850 4400
Text Label 3050 4900 2    60   ~ 0
SCL
Text Label 2850 4800 2    60   ~ 0
SDA
$Comp
L ArduinoSpecAn-rescue:R_Small R12
U 1 1 569C48EE
P 8750 5350
F 0 "R12" V 8850 5300 50  0000 L CNN
F 1 "1k" V 8650 5300 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8750 5350 60  0001 C CNN
F 3 "" H 8750 5350 60  0000 C CNN
	1    8750 5350
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R11
U 1 1 569C497B
P 8050 5550
F 0 "R11" V 8150 5500 50  0000 L CNN
F 1 "1k" V 7950 5500 50  0000 L CNN
F 2 "footprints:Custom_0805" H 8050 5550 60  0001 C CNN
F 3 "" H 8050 5550 60  0000 C CNN
	1    8050 5550
	-1   0    0    1   
$EndComp
Wire Wire Line
	8650 5350 8050 5350
Connection ~ 8050 5350
Wire Wire Line
	9500 5350 8850 5350
$Comp
L power:GND #PWR013
U 1 1 569C4E3C
P 8050 5750
F 0 "#PWR013" H 8050 5500 50  0001 C CNN
F 1 "GND" H 8050 5600 50  0000 C CNN
F 2 "" H 8050 5750 60  0000 C CNN
F 3 "" H 8050 5750 60  0000 C CNN
	1    8050 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	8050 5650 8050 5750
Wire Wire Line
	8750 2050 8750 1950
Wire Wire Line
	8750 1500 8750 1650
Connection ~ 8750 1650
$Comp
L ArduinoSpecAn-rescue:MMBT3904 Q1
U 1 1 569C5979
P 3700 6300
F 0 "Q1" H 3900 6375 50  0000 L CNN
F 1 "MMBT3904" H 3900 6300 50  0000 L CNN
F 2 "footprints:SOT-23" H 3900 6225 50  0001 L CIN
F 3 "" H 3700 6300 50  0000 L CNN
	1    3700 6300
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:MMBT3904 Q2
U 1 1 569C5AE9
P 4400 6000
F 0 "Q2" H 4600 6075 50  0000 L CNN
F 1 "MMBT3904" H 4600 6000 50  0000 L CNN
F 2 "footprints:SOT-23" H 4600 5925 50  0001 L CIN
F 3 "" H 4400 6000 50  0000 L CNN
	1    4400 6000
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R5
U 1 1 569C5CEA
P 3800 5750
F 0 "R5" H 3830 5770 50  0000 L CNN
F 1 "220" H 3830 5710 50  0000 L CNN
F 2 "footprints:Custom_0805" H 3800 5750 60  0001 C CNN
F 3 "" H 3800 5750 60  0000 C CNN
	1    3800 5750
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R7
U 1 1 569C5E7A
P 4500 7200
F 0 "R7" H 4530 7220 50  0000 L CNN
F 1 "220" H 4530 7160 50  0000 L CNN
F 2 "footprints:Custom_0805" H 4500 7200 60  0001 C CNN
F 3 "" H 4500 7200 60  0000 C CNN
	1    4500 7200
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:POT Pot1
U 1 1 569C5F66
P 3000 6300
F 0 "Pot1" H 3000 6200 50  0000 C CNN
F 1 "1k" H 3000 6300 50  0000 C CNN
F 2 "footprints:ST4ETB_Trim_Pot" H 3000 6300 60  0001 C CNN
F 3 "" H 3000 6300 60  0000 C CNN
	1    3000 6300
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C3
U 1 1 569C622C
P 2600 6300
F 0 "C3" H 2610 6370 50  0000 L CNN
F 1 "10uF" H 2610 6220 50  0000 L CNN
F 2 "footprints:Custom_0805" H 2600 6300 60  0001 C CNN
F 3 "" H 2600 6300 60  0000 C CNN
	1    2600 6300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2700 6300 2750 6300
Wire Wire Line
	2500 6300 2350 6300
Text Label 2350 6300 2    60   ~ 0
RF
$Comp
L ArduinoSpecAn-rescue:R_Small R4
U 1 1 569C72B0
P 3450 7200
F 0 "R4" H 3480 7220 50  0000 L CNN
F 1 "100" H 3480 7160 50  0000 L CNN
F 2 "footprints:Custom_0805" H 3450 7200 60  0001 C CNN
F 3 "" H 3450 7200 60  0000 C CNN
	1    3450 7200
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R6
U 1 1 569C7362
P 4000 6850
F 0 "R6" H 4030 6870 50  0000 L CNN
F 1 "220" H 4030 6810 50  0000 L CNN
F 2 "footprints:Custom_0805" H 4000 6850 60  0001 C CNN
F 3 "" H 4000 6850 60  0000 C CNN
	1    4000 6850
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R8
U 1 1 569C7601
P 4700 6450
F 0 "R8" H 4730 6470 50  0000 L CNN
F 1 "47" H 4730 6410 50  0000 L CNN
F 2 "footprints:Custom_0805" H 4700 6450 60  0001 C CNN
F 3 "" H 4700 6450 60  0000 C CNN
	1    4700 6450
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C6
U 1 1 569C7704
P 5000 6450
F 0 "C6" H 5010 6520 50  0000 L CNN
F 1 "10uF" H 5010 6370 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5000 6450 60  0001 C CNN
F 3 "" H 5000 6450 60  0000 C CNN
	1    5000 6450
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3400 6300 3450 6300
Wire Wire Line
	3450 6300 3450 6850
Connection ~ 3450 6300
Wire Wire Line
	3450 6850 3900 6850
Connection ~ 3450 6850
Wire Wire Line
	4500 6200 4500 6450
Wire Wire Line
	3800 5850 3800 6000
Wire Wire Line
	3800 5650 3800 5550
Wire Wire Line
	3800 5550 4150 5550
Wire Wire Line
	4500 5550 4500 5800
Wire Wire Line
	4150 5550 4150 5400
Connection ~ 4150 5550
Text Label 4150 5400 0    60   ~ 0
5V
Wire Wire Line
	3800 6000 4200 6000
Connection ~ 3800 6000
Wire Wire Line
	4100 6850 4500 6850
Connection ~ 4500 6850
Wire Wire Line
	4600 6450 4500 6450
Connection ~ 4500 6450
Wire Wire Line
	4800 6450 4900 6450
$Comp
L power:GND #PWR014
U 1 1 569C8DF9
P 3800 6550
F 0 "#PWR014" H 3800 6300 50  0001 C CNN
F 1 "GND" H 3800 6400 50  0000 C CNN
F 2 "" H 3800 6550 60  0000 C CNN
F 3 "" H 3800 6550 60  0000 C CNN
	1    3800 6550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 6550 3800 6500
$Comp
L ArduinoSpecAn-rescue:SMA J2
U 1 1 569C9F74
P 5550 6450
F 0 "J2" H 5300 6350 60  0000 C CNN
F 1 "SMA" H 5550 6650 60  0000 C CNN
F 2 "footprints:SMA_Edgemount" H 5550 6450 60  0001 C CNN
F 3 "" H 5550 6450 60  0000 C CNN
	1    5550 6450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	5100 6450 5350 6450
$Comp
L power:GND #PWR015
U 1 1 569CA262
P 3450 7400
F 0 "#PWR015" H 3450 7150 50  0001 C CNN
F 1 "GND" H 3450 7250 50  0000 C CNN
F 2 "" H 3450 7400 60  0000 C CNN
F 3 "" H 3450 7400 60  0000 C CNN
	1    3450 7400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR016
U 1 1 569CA2F7
P 4500 7400
F 0 "#PWR016" H 4500 7150 50  0001 C CNN
F 1 "GND" H 4500 7250 50  0000 C CNN
F 2 "" H 4500 7400 60  0000 C CNN
F 3 "" H 4500 7400 60  0000 C CNN
	1    4500 7400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 7300 4500 7400
Wire Wire Line
	3450 7400 3450 7300
$Comp
L power:GND #PWR017
U 1 1 569CA61D
P 5550 7000
F 0 "#PWR017" H 5550 6750 50  0001 C CNN
F 1 "GND" H 5550 6850 50  0000 C CNN
F 2 "" H 5550 7000 60  0000 C CNN
F 3 "" H 5550 7000 60  0000 C CNN
	1    5550 7000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 6800 5400 6900
Wire Wire Line
	5400 6900 5500 6900
Wire Wire Line
	5700 6900 5700 6800
Wire Wire Line
	5500 6800 5500 6900
Connection ~ 5500 6900
Wire Wire Line
	5600 6800 5600 6900
Connection ~ 5600 6900
Wire Wire Line
	5550 7000 5550 6900
Connection ~ 5550 6900
Wire Wire Line
	3000 6150 3000 6100
Wire Wire Line
	3000 6100 3400 6100
Wire Wire Line
	3400 6100 3400 6300
NoConn ~ 3250 6300
Text Notes 5850 6450 0    60   ~ 0
50 Ohm output impedance.\nWill drive 0 dBm into 50 Ohm load.
Wire Wire Line
	8150 2900 8650 2900
Wire Wire Line
	9350 2900 9750 2900
Wire Wire Line
	1850 1450 1850 1650
Wire Wire Line
	850  1450 1850 1450
Wire Wire Line
	900  1950 900  2000
Wire Wire Line
	4400 2150 4400 2250
Wire Wire Line
	4400 2250 4400 2500
Wire Wire Line
	4400 1350 4400 1550
Wire Wire Line
	4400 1150 4400 1350
Wire Wire Line
	4400 1050 4400 1150
Wire Wire Line
	4400 1550 4400 1850
Wire Wire Line
	4400 1850 4400 2150
Wire Wire Line
	4400 2500 4400 2600
Wire Wire Line
	5300 1650 5600 1650
Wire Wire Line
	6400 1650 6500 1650
Wire Wire Line
	6000 1650 6100 1650
Wire Wire Line
	5600 1650 5700 1650
Wire Wire Line
	6800 1650 7100 1650
Wire Wire Line
	5600 2200 6000 2200
Wire Wire Line
	6000 2200 6200 2200
Wire Wire Line
	6400 2200 6800 2200
Wire Wire Line
	6800 2200 7100 2200
Wire Wire Line
	6200 2200 6400 2200
Wire Wire Line
	7100 1650 7300 1650
Wire Wire Line
	2250 1850 2250 2700
Wire Wire Line
	2250 1350 2250 1850
Wire Wire Line
	2250 1050 2250 1350
Wire Wire Line
	2600 1450 2600 1950
Wire Wire Line
	2600 1250 2600 1450
Wire Wire Line
	2600 1150 2600 1250
Wire Wire Line
	9300 3650 9400 3650
Wire Wire Line
	8000 2050 8250 2050
Wire Wire Line
	8250 2050 8500 2050
Wire Wire Line
	8500 2050 8500 2200
Wire Wire Line
	8500 2050 8750 2050
Wire Wire Line
	8000 1650 8250 1650
Wire Wire Line
	8250 1650 8500 1650
Wire Wire Line
	8500 1650 8750 1650
Wire Wire Line
	9500 4600 9650 4600
Wire Wire Line
	9900 3300 9950 3300
Wire Wire Line
	10000 3300 10100 3300
Wire Wire Line
	9950 3300 10000 3300
Wire Wire Line
	9400 3650 9600 3650
Wire Wire Line
	2850 4400 2850 4500
Wire Wire Line
	8050 5350 8050 5450
Wire Wire Line
	8750 1650 8750 1750
Wire Wire Line
	3450 6300 3500 6300
Wire Wire Line
	3450 6850 3450 7100
Wire Wire Line
	4150 5550 4500 5550
Wire Wire Line
	3800 6000 3800 6100
Wire Wire Line
	4500 6850 4500 7100
Wire Wire Line
	4500 6450 4500 6850
Wire Wire Line
	5500 6900 5550 6900
Wire Wire Line
	5600 6900 5700 6900
Wire Wire Line
	5550 6900 5600 6900
$Comp
L MCU_Module:Arduino_Nano_v3.x A1
U 1 1 5B688AEF
P 1800 4400
F 0 "A1" H 1800 3314 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 1800 3223 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 1950 3450 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 1800 3400 50  0001 C CNN
	1    1800 4400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5B688C9C
P 1850 5450
F 0 "#PWR0101" H 1850 5200 50  0001 C CNN
F 1 "GND" H 1855 5277 50  0000 C CNN
F 2 "" H 1850 5450 50  0001 C CNN
F 3 "" H 1850 5450 50  0001 C CNN
	1    1850 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 5400 1850 5400
Wire Wire Line
	1850 5450 1850 5400
Connection ~ 1850 5400
Wire Wire Line
	1850 5400 1800 5400
Wire Wire Line
	2000 3400 2000 3250
Text Label 2000 3250 0    60   ~ 0
5V
Wire Wire Line
	2550 4400 2300 4400
Text Label 2550 4700 2    60   ~ 0
SLD
Wire Wire Line
	2550 4700 2300 4700
$Comp
L Device:LED D1
U 1 1 5B63AF34
P 950 6400
F 0 "D1" V 895 6478 50  0000 L CNN
F 1 "LED" V 986 6478 50  0000 L CNN
F 2 "LED_SMD:LED_0805_2012Metric_Pad0.97x1.50mm_HandSolder" H 950 6400 50  0001 C CNN
F 3 "~" H 950 6400 50  0001 C CNN
	1    950  6400
	0    1    1    0   
$EndComp
$Comp
L Device:LED D2
U 1 1 5B63B191
P 1300 6400
F 0 "D2" V 1245 6478 50  0000 L CNN
F 1 "LED" V 1336 6478 50  0000 L CNN
F 2 "LED_SMD:LED_0805_2012Metric_Pad0.97x1.50mm_HandSolder" H 1300 6400 50  0001 C CNN
F 3 "~" H 1300 6400 50  0001 C CNN
	1    1300 6400
	0    1    1    0   
$EndComp
$EndSCHEMATC