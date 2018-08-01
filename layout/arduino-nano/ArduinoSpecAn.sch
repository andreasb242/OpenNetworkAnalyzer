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
P 4800 1650
F 0 "U1" H 5000 1400 60  0000 C CNN
F 1 "AD8307" H 4800 1900 60  0000 C CNN
F 2 "SMD_Packages:SOIC-8-N" H 4800 1700 60  0001 C CNN
F 3 "" H 4800 1700 60  0000 C CNN
	1    4800 1650
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:AD9851 U2
U 1 1 567AF1E6
P -8650 650
F 0 "U2" H -8300 -100 60  0000 C CNN
F 1 "AD9851" H -8650 1400 60  0000 C CNN
F 2 "Housings_SSOP:SSOP-28_5.3x10.2mm_Pitch0.65mm" H -8650 650 60  0001 C CNN
F 3 "" H -8650 650 60  0000 C CNN
	1    -8650 650 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:CONN_01X08 P3
U 1 1 567AF44C
P -1150 550
F 0 "P3" H -1150 1000 50  0000 C CNN
F 1 "CONN_01X08" V -1050 550 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x08" H -1150 550 60  0001 C CNN
F 3 "" H -1150 550 60  0000 C CNN
	1    -1150 550 
	-1   0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:CONN_01X08 P1
U 1 1 567AF565
P -1500 -550
F 0 "P1" H -1500 -100 50  0000 C CNN
F 1 "CONN_01X08" V -1400 -550 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x08" H -1500 -550 60  0001 C CNN
F 3 "" H -1500 -550 60  0000 C CNN
	1    -1500 -550
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:CONN_01X06 P2
U 1 1 567AF5D9
P -1500 650
F 0 "P2" H -1500 1000 50  0000 C CNN
F 1 "CONN_01X06" V -1400 650 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x06" H -1500 650 60  0001 C CNN
F 3 "" H -1500 650 60  0000 C CNN
	1    -1500 650 
	1    0    0    -1  
$EndComp
Text Label -1950 400  0    60   ~ 0
A0
Text Label -1950 500  0    60   ~ 0
A1
Text Label -1950 600  0    60   ~ 0
A2
Text Label -1950 800  0    60   ~ 0
A4
Text Label -1950 900  0    60   ~ 0
A5
NoConn ~ -1700 -900
$Comp
L power:GND #PWR01
U 1 1 567B1CC7
P -1850 -350
F 0 "#PWR01" H -1850 -600 50  0001 C CNN
F 1 "GND" V -1850 -550 50  0000 C CNN
F 2 "" H -1850 -350 60  0000 C CNN
F 3 "" H -1850 -350 60  0000 C CNN
	1    -1850 -350
	0    1    1    0   
$EndComp
Text Label -700 900  2    60   ~ 0
RX
Text Label -700 800  2    60   ~ 0
TX
Text Label -700 700  2    60   ~ 0
2
Text Label -700 600  2    60   ~ 0
3
Text Label -700 500  2    60   ~ 0
4
Text Label -700 400  2    60   ~ 0
5
Text Label -700 300  2    60   ~ 0
6
Text Label -700 200  2    60   ~ 0
7
Text Label -1950 -800 0    60   ~ 0
IOREF
Text Label -1950 -700 0    60   ~ 0
RESET
Text Label -1950 -600 0    60   ~ 0
3V3
Text Label -1950 -500 0    60   ~ 0
5V
Text Label -1950 -200 0    60   ~ 0
Vin
$Comp
L ArduinoSpecAn-rescue:C_Small C2
U 1 1 567B2606
P 4200 1250
F 0 "C2" H 4210 1320 50  0000 L CNN
F 1 "10µF" H 4210 1170 50  0000 L CNN
F 2 "footprints:Custom_0805" H 4200 1250 60  0001 C CNN
F 3 "" H 4200 1250 60  0000 C CNN
	1    4200 1250
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C4
U 1 1 567B275A
P 5400 1250
F 0 "C4" H 5410 1320 50  0000 L CNN
F 1 "10µF" H 5410 1170 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5400 1250 60  0001 C CNN
F 3 "" H 5400 1250 60  0000 C CNN
	1    5400 1250
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R2
U 1 1 567B27BA
P 4800 950
F 0 "R2" V 4900 900 50  0000 L CNN
F 1 "51" V 4700 900 50  0000 L CNN
F 2 "footprints:Custom_0805" H 4800 950 60  0001 C CNN
F 3 "" H 4800 950 60  0000 C CNN
	1    4800 950 
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR02
U 1 1 567B2AA5
P 3700 1200
F 0 "#PWR02" H 3700 950 50  0001 C CNN
F 1 "GND" H 3700 1050 50  0000 C CNN
F 2 "" H 3700 1200 60  0000 C CNN
F 3 "" H 3700 1200 60  0000 C CNN
	1    3700 1200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR03
U 1 1 567B2DB3
P 6000 1400
F 0 "#PWR03" H 6000 1150 50  0001 C CNN
F 1 "GND" H 6000 1250 50  0000 C CNN
F 2 "" H 6000 1400 60  0000 C CNN
F 3 "" H 6000 1400 60  0000 C CNN
	1    6000 1400
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R3
U 1 1 567B2F06
P 5750 1700
F 0 "R3" V 5850 1650 50  0000 L CNN
F 1 "4.7Ω" V 5650 1650 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5750 1700 60  0001 C CNN
F 3 "" H 5750 1700 60  0000 C CNN
	1    5750 1700
	0    -1   -1   0   
$EndComp
NoConn ~ 5250 1800
NoConn ~ 4350 1700
$Comp
L power:GND #PWR04
U 1 1 567B32D9
P 4250 2050
F 0 "#PWR04" H 4250 1800 50  0001 C CNN
F 1 "GND" H 4250 1900 50  0000 C CNN
F 2 "" H 4250 2050 60  0000 C CNN
F 3 "" H 4250 2050 60  0000 C CNN
	1    4250 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	-950 900  -700 900 
Wire Wire Line
	-950 800  -700 800 
Wire Wire Line
	-950 700  -700 700 
Wire Wire Line
	-950 600  -700 600 
Wire Wire Line
	-950 500  -700 500 
Wire Wire Line
	-950 400  -700 400 
Wire Wire Line
	-950 300  -700 300 
Wire Wire Line
	-950 200  -700 200 
Wire Wire Line
	-1700 -800 -1950 -800
Wire Wire Line
	-1700 -700 -1950 -700
Wire Wire Line
	-1700 -600 -1950 -600
Wire Wire Line
	-1700 -500 -1950 -500
Wire Wire Line
	-1700 -200 -1950 -200
Wire Wire Line
	-1700 400  -1950 400 
Wire Wire Line
	-1700 500  -1950 500 
Wire Wire Line
	-1700 600  -1950 600 
Wire Wire Line
	-1700 700  -1950 700 
Wire Wire Line
	-2250 800  -1700 800 
Wire Wire Line
	-2500 900  -1700 900 
Wire Wire Line
	-1700 -400 -1850 -400
Wire Wire Line
	-1850 -400 -1850 -350
Wire Wire Line
	-1850 -300 -1700 -300
Connection ~ -1850 -350
Wire Wire Line
	4200 1150 4200 950 
Wire Wire Line
	3700 950  4200 950 
Wire Wire Line
	4900 950  5400 950 
Wire Wire Line
	5400 950  5400 1150
Wire Wire Line
	4200 1350 4200 1500
Wire Wire Line
	4200 1500 4350 1500
Wire Wire Line
	5250 1500 5400 1500
Wire Wire Line
	5400 1500 5400 1350
Wire Wire Line
	3700 1200 3700 950 
Connection ~ 4200 950 
Connection ~ 5400 950 
Text Label 5400 950  0    60   ~ 0
Input
Wire Wire Line
	5850 1700 6000 1700
Text Label 6000 1700 0    60   ~ 0
5V
Text Label 3800 1800 0    60   ~ 0
Vmag
Text Label 6750 1100 0    60   ~ 0
Vmag
Text Label 7600 850  2    60   ~ 0
5V
$Comp
L power:GND #PWR05
U 1 1 567B5123
P 7600 1650
F 0 "#PWR05" H 7600 1400 50  0001 C CNN
F 1 "GND" H 7600 1500 50  0000 C CNN
F 2 "" H 7600 1650 60  0000 C CNN
F 3 "" H 7600 1650 60  0000 C CNN
	1    7600 1650
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:LM7301 U3
U 1 1 567B52F9
P 7600 1250
F 0 "U3" H 7850 1000 60  0000 C CNN
F 1 "LM7301" H 7900 1450 60  0000 C CNN
F 2 "Housings_SOT-23_SOT-143_TSOT-6:SOT-23-5" H 7600 1200 60  0001 C CNN
F 3 "" H 7600 1200 60  0000 C CNN
	1    7600 1250
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:KC5032A X1
U 1 1 567B611F
P -10600 750
F 0 "X1" H -10450 600 60  0000 C CNN
F 1 "KC5032A" H -10600 900 60  0000 C CNN
F 2 "footprints:KC5032A-CM_SMD_Crystal" H -10600 750 60  0001 C CNN
F 3 "" H -10600 750 60  0000 C CNN
	1    -10600 750 
	1    0    0    -1  
$EndComp
Wire Wire Line
	-11000 700  -11100 700 
Wire Wire Line
	-11100 700  -11100 500 
Wire Wire Line
	-11350 500  -11100 500 
Wire Wire Line
	-10100 350  -10100 500 
Wire Wire Line
	-10100 700  -10200 700 
Connection ~ -10100 500 
Text Label -10100 350  0    60   ~ 0
5V
$Comp
L power:GND #PWR06
U 1 1 567B632A
P -11050 1050
F 0 "#PWR06" H -11050 800 50  0001 C CNN
F 1 "GND" H -11050 900 50  0000 C CNN
F 2 "" H -11050 1050 60  0000 C CNN
F 3 "" H -11050 1050 60  0000 C CNN
	1    -11050 1050
	1    0    0    -1  
$EndComp
Wire Wire Line
	-11050 800  -11050 1000
Wire Wire Line
	-11050 800  -11000 800 
$Comp
L ArduinoSpecAn-rescue:C_Small C1
U 1 1 567B63B5
P -11350 800
F 0 "C1" H -11340 870 50  0000 L CNN
F 1 ".01uF" H -11340 720 50  0000 L CNN
F 2 "footprints:Custom_0805" H -11350 800 60  0001 C CNN
F 3 "" H -11350 800 60  0000 C CNN
	1    -11350 800 
	1    0    0    -1  
$EndComp
Wire Wire Line
	-11350 700  -11350 500 
Connection ~ -11100 500 
Wire Wire Line
	-11350 900  -11350 1000
Wire Wire Line
	-11350 1000 -11050 1000
Connection ~ -11050 1000
Wire Wire Line
	-10200 800  -9250 800 
Wire Wire Line
	-8050 300  -7850 300 
Text Label -7850 300  2    60   ~ 0
SDA
Wire Wire Line
	-9250 600  -9650 600 
Text Label -9650 600  0    60   ~ 0
SCL
Wire Wire Line
	-9250 700  -9650 700 
Text Label -9650 700  0    60   ~ 0
SLD
NoConn ~ -9250 1200
NoConn ~ -9250 1300
NoConn ~ -8050 1100
$Comp
L power:GND #PWR07
U 1 1 567B700B
P -7550 1650
F 0 "#PWR07" H -7550 1400 50  0001 C CNN
F 1 "GND" H -7550 1500 50  0000 C CNN
F 2 "" H -7550 1650 60  0000 C CNN
F 3 "" H -7550 1650 60  0000 C CNN
	1    -7550 1650
	1    0    0    -1  
$EndComp
Wire Wire Line
	-8050 0    -7550 0   
Wire Wire Line
	-7550 0    -7550 100 
Wire Wire Line
	-8050 1200 -7550 1200
Connection ~ -7550 1200
Wire Wire Line
	-8050 1300 -7550 1300
Connection ~ -7550 1300
Wire Wire Line
	-8050 400  -7550 400 
Connection ~ -7550 400 
Wire Wire Line
	-8050 200  -7550 200 
Connection ~ -7550 200 
Wire Wire Line
	-8050 100  -7550 100 
Connection ~ -7550 100 
Wire Wire Line
	-8050 600  -7550 600 
Connection ~ -7550 600 
Wire Wire Line
	-8050 900  -7550 900 
Connection ~ -7550 900 
$Comp
L ArduinoSpecAn-rescue:R_Small R9
U 1 1 567B73DA
P -7200 1200
F 0 "R9" H -7170 1220 50  0000 L CNN
F 1 "50" H -7170 1160 50  0000 L CNN
F 2 "footprints:Custom_0805" H -7200 1200 60  0001 C CNN
F 3 "" H -7200 1200 60  0000 C CNN
	1    -7200 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	-8050 800  -7200 800 
Wire Wire Line
	-7200 800  -7200 1100
Wire Wire Line
	-7200 1300 -7200 1550
Wire Wire Line
	-7200 1550 -7550 1550
Connection ~ -7550 1550
$Comp
L ArduinoSpecAn-rescue:C_Small C7
U 1 1 567B75BC
P -6350 950
F 0 "C7" H -6340 1020 50  0000 L CNN
F 1 "10pF" H -6340 870 50  0000 L CNN
F 2 "footprints:Custom_0805" H -6350 950 60  0001 C CNN
F 3 "" H -6350 950 60  0000 C CNN
	1    -6350 950 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C8
U 1 1 567B7631
P -5950 950
F 0 "C8" H -5940 1020 50  0000 L CNN
F 1 "39pF" H -5940 870 50  0000 L CNN
F 2 "footprints:Custom_0805" H -5950 950 60  0001 C CNN
F 3 "" H -5950 950 60  0000 C CNN
	1    -5950 950 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C9
U 1 1 567B7691
P -5550 950
F 0 "C9" H -5540 1020 50  0000 L CNN
F 1 "39pF" H -5540 870 50  0000 L CNN
F 2 "footprints:Custom_0805" H -5550 950 60  0001 C CNN
F 3 "" H -5550 950 60  0000 C CNN
	1    -5550 950 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C10
U 1 1 567B76E7
P -5150 950
F 0 "C10" H -5140 1020 50  0000 L CNN
F 1 "10pF" H -5140 870 50  0000 L CNN
F 2 "footprints:Custom_0805" H -5150 950 60  0001 C CNN
F 3 "" H -5150 950 60  0000 C CNN
	1    -5150 950 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:L_Small L1
U 1 1 567B781E
P -6150 700
F 0 "L1" H -6120 740 50  0000 L CNN
F 1 "270nH" H -6120 660 50  0000 L CNN
F 2 "footprints:Custom_0805" H -6150 700 60  0001 C CNN
F 3 "" H -6150 700 60  0000 C CNN
	1    -6150 700 
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:L_Small L2
U 1 1 567B7A95
P -5750 700
F 0 "L2" H -5720 740 50  0000 L CNN
F 1 "470nH" H -5720 660 50  0000 L CNN
F 2 "footprints:Custom_0805" H -5750 700 60  0001 C CNN
F 3 "" H -5750 700 60  0000 C CNN
	1    -5750 700 
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:L_Small L3
U 1 1 567B7C20
P -5350 700
F 0 "L3" H -5320 740 50  0000 L CNN
F 1 "270nH" H -5320 660 50  0000 L CNN
F 2 "footprints:Custom_0805" H -5350 700 60  0001 C CNN
F 3 "" H -5350 700 60  0000 C CNN
	1    -5350 700 
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R10
U 1 1 567B7F0E
P -6650 950
F 0 "R10" H -6620 970 50  0000 L CNN
F 1 "100" H -6620 910 50  0000 L CNN
F 2 "footprints:Custom_0805" H -6650 950 60  0001 C CNN
F 3 "" H -6650 950 60  0000 C CNN
	1    -6650 950 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R13
U 1 1 567B7F96
P -4850 950
F 0 "R13" H -4820 970 50  0000 L CNN
F 1 "100" H -4820 910 50  0000 L CNN
F 2 "footprints:Custom_0805" H -4850 950 60  0001 C CNN
F 3 "" H -4850 950 60  0000 C CNN
	1    -4850 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	-8050 700  -6650 700 
Wire Wire Line
	-6650 700  -6650 850 
Connection ~ -6650 700 
Wire Wire Line
	-6050 700  -5950 700 
Wire Wire Line
	-5650 700  -5550 700 
Wire Wire Line
	-5250 700  -5150 700 
Wire Wire Line
	-5150 700  -5150 850 
Wire Wire Line
	-5550 850  -5550 700 
Connection ~ -5550 700 
Wire Wire Line
	-5950 850  -5950 700 
Connection ~ -5950 700 
Wire Wire Line
	-6350 850  -6350 700 
Connection ~ -6350 700 
Wire Wire Line
	-4850 700  -4850 850 
Connection ~ -5150 700 
Wire Wire Line
	-4850 1250 -4850 1050
Wire Wire Line
	-6650 1250 -6350 1250
Wire Wire Line
	-6650 1250 -6650 1050
Wire Wire Line
	-6350 1050 -6350 1250
Connection ~ -6350 1250
Wire Wire Line
	-5950 1050 -5950 1250
Connection ~ -5950 1250
Wire Wire Line
	-5550 1050 -5550 1250
Connection ~ -5550 1250
Wire Wire Line
	-5150 1050 -5150 1250
Connection ~ -5150 1250
$Comp
L power:GND #PWR08
U 1 1 567B904B
P -5750 1350
F 0 "#PWR08" H -5750 1100 50  0001 C CNN
F 1 "GND" H -5750 1200 50  0000 C CNN
F 2 "" H -5750 1350 60  0000 C CNN
F 3 "" H -5750 1350 60  0000 C CNN
	1    -5750 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	-5750 1350 -5750 1250
Connection ~ -5750 1250
Connection ~ -4850 700 
Text Label -4650 700  2    60   ~ 0
RF
$Comp
L ArduinoSpecAn-rescue:R_Small R1
U 1 1 567B9D46
P -10050 1550
F 0 "R1" H -10020 1570 50  0000 L CNN
F 1 "3k92" H -10020 1510 50  0000 L CNN
F 2 "footprints:Custom_0805" H -10050 1550 60  0001 C CNN
F 3 "" H -10050 1550 60  0000 C CNN
	1    -10050 1550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 567B9E90
P -10050 1750
F 0 "#PWR09" H -10050 1500 50  0001 C CNN
F 1 "GND" H -10050 1600 50  0000 C CNN
F 2 "" H -10050 1750 60  0000 C CNN
F 3 "" H -10050 1750 60  0000 C CNN
	1    -10050 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	-10050 1650 -10050 1750
Wire Wire Line
	-10050 1450 -10050 1100
Wire Wire Line
	-10050 1100 -9250 1100
$Comp
L power:GND #PWR010
U 1 1 567BA433
P -9700 1750
F 0 "#PWR010" H -9700 1500 50  0001 C CNN
F 1 "GND" H -9700 1600 50  0000 C CNN
F 2 "" H -9700 1750 60  0000 C CNN
F 3 "" H -9700 1750 60  0000 C CNN
	1    -9700 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	-9700 900  -9250 900 
Wire Wire Line
	-9700 0    -9700 100 
Wire Wire Line
	-9250 400  -9700 400 
Connection ~ -9700 900 
Wire Wire Line
	-9250 100  -9700 100 
Connection ~ -9700 400 
Wire Wire Line
	-9250 0    -9700 0   
Connection ~ -9700 100 
Wire Wire Line
	-9350 1000 -9250 1000
Wire Wire Line
	-9350 -350 -9350 200 
Wire Wire Line
	-9250 500  -9350 500 
Connection ~ -9350 500 
Wire Wire Line
	-9250 300  -9350 300 
Connection ~ -9350 300 
Wire Wire Line
	-9250 200  -9350 200 
Connection ~ -9350 200 
Text Label -9350 -350 0    60   ~ 0
5V
Wire Wire Line
	-8050 500  -7700 500 
Text Label -7700 500  2    60   ~ 0
5V
Wire Wire Line
	-8050 1000 -7700 1000
Text Label -7700 1000 2    60   ~ 0
5V
Wire Wire Line
	5250 1700 5350 1700
Wire Wire Line
	5250 1600 5350 1600
Wire Wire Line
	5350 1600 5350 1700
Connection ~ 5350 1700
$Comp
L ArduinoSpecAn-rescue:C_Small C11
U 1 1 567C5D7E
P -9150 -850
F 0 "C11" H -9140 -780 50  0000 L CNN
F 1 ".1uF" H -9140 -930 50  0000 L CNN
F 2 "footprints:Custom_0805" H -9150 -850 60  0001 C CNN
F 3 "" H -9150 -850 60  0000 C CNN
	1    -9150 -850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C12
U 1 1 567C6091
P -8900 -850
F 0 "C12" H -8890 -780 50  0000 L CNN
F 1 ".1uF" H -8890 -930 50  0000 L CNN
F 2 "footprints:Custom_0805" H -8900 -850 60  0001 C CNN
F 3 "" H -8900 -850 60  0000 C CNN
	1    -8900 -850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C13
U 1 1 567C6113
P -8650 -850
F 0 "C13" H -8640 -780 50  0000 L CNN
F 1 ".1uF" H -8640 -930 50  0000 L CNN
F 2 "footprints:Custom_0805" H -8650 -850 60  0001 C CNN
F 3 "" H -8650 -850 60  0000 C CNN
	1    -8650 -850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C14
U 1 1 567C619C
P -8400 -850
F 0 "C14" H -8390 -780 50  0000 L CNN
F 1 ".1uF" H -8390 -930 50  0000 L CNN
F 2 "footprints:Custom_0805" H -8400 -850 60  0001 C CNN
F 3 "" H -8400 -850 60  0000 C CNN
	1    -8400 -850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C15
U 1 1 567C6228
P 9350 1250
F 0 "C15" H 9360 1320 50  0000 L CNN
F 1 ".1uF" H 9360 1170 50  0000 L CNN
F 2 "footprints:Custom_0805" H 9350 1250 60  0001 C CNN
F 3 "" H 9350 1250 60  0000 C CNN
	1    9350 1250
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C5
U 1 1 567C63EB
P 5450 2000
F 0 "C5" H 5460 2070 50  0000 L CNN
F 1 "100nF" H 5460 1920 50  0000 L CNN
F 2 "footprints:Custom_0805" H 5450 2000 60  0001 C CNN
F 3 "" H 5450 2000 60  0000 C CNN
	1    5450 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	-9150 -950 -9150 -1050
Wire Wire Line
	-9150 -1050 -8900 -1050
Wire Wire Line
	-9150 -750 -9150 -650
Wire Wire Line
	-9150 -650 -8900 -650
Wire Wire Line
	-8900 -750 -8900 -650
Connection ~ -8900 -650
Wire Wire Line
	-8650 -750 -8650 -650
Connection ~ -8650 -650
Wire Wire Line
	-8400 -750 -8400 -650
Wire Wire Line
	-8900 -950 -8900 -1050
Connection ~ -8900 -1050
Wire Wire Line
	-8650 -950 -8650 -1050
Connection ~ -8650 -1050
Wire Wire Line
	-8400 -1050 -8400 -950
$Comp
L power:GND #PWR011
U 1 1 567C76A2
P -8750 -500
F 0 "#PWR011" H -8750 -750 50  0001 C CNN
F 1 "GND" H -8750 -650 50  0000 C CNN
F 2 "" H -8750 -500 60  0000 C CNN
F 3 "" H -8750 -500 60  0000 C CNN
	1    -8750 -500
	1    0    0    -1  
$EndComp
Text Label 9350 900  0    60   ~ 0
5V
Text Notes -8100 -900 0    60   ~ 0
Decoupling Caps:\n- AD9851 x 4
Text Notes -6200 350  0    60   ~ 0
72MHz Butterworth LPF\nMatched to 100 Ohms
Wire Wire Line
	8200 1250 8450 1250
Wire Wire Line
	8450 1250 8450 2000
Wire Wire Line
	7000 1400 7000 2000
Wire Wire Line
	7000 1400 7100 1400
Wire Wire Line
	6750 1100 7100 1100
Connection ~ 8450 1250
Text Label 8600 1250 2    60   ~ 0
A0
Wire Wire Line
	4350 1600 4250 1600
Wire Wire Line
	4250 1600 4250 2050
Wire Wire Line
	3800 1800 4350 1800
Wire Wire Line
	5850 1300 5850 1350
Wire Wire Line
	5850 1350 5950 1350
Wire Wire Line
	6150 1350 6150 1300
Wire Wire Line
	5950 1300 5950 1350
Connection ~ 5950 1350
Wire Wire Line
	6050 1300 6050 1350
Connection ~ 6050 1350
Wire Wire Line
	6000 1400 6000 1350
Connection ~ 6000 1350
NoConn ~ -1700 -800
NoConn ~ -1700 -700
NoConn ~ -1700 -600
NoConn ~ -1700 -200
NoConn ~ -950 200 
NoConn ~ -950 300 
NoConn ~ -950 400 
NoConn ~ -950 500 
NoConn ~ -950 600 
NoConn ~ -950 700 
NoConn ~ -950 800 
NoConn ~ -950 900 
NoConn ~ -1700 900 
NoConn ~ -1700 800 
NoConn ~ -1700 700 
NoConn ~ -1700 600 
NoConn ~ -1700 500 
$Comp
L ArduinoSpecAn-rescue:R_Small R15
U 1 1 567C1CD7
P -2250 600
F 0 "R15" H -2220 620 50  0000 L CNN
F 1 "2k" H -2220 560 50  0000 L CNN
F 2 "footprints:Custom_0805" H -2250 600 60  0001 C CNN
F 3 "" H -2250 600 60  0000 C CNN
	1    -2250 600 
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R14
U 1 1 567C1D6D
P -2500 600
F 0 "R14" H -2470 620 50  0000 L CNN
F 1 "2k" H -2470 560 50  0000 L CNN
F 2 "footprints:Custom_0805" H -2500 600 60  0001 C CNN
F 3 "" H -2500 600 60  0000 C CNN
	1    -2500 600 
	1    0    0    -1  
$EndComp
Text Label -2250 250  2    60   ~ 0
5V
Wire Wire Line
	5450 1900 5450 1700
Connection ~ 5450 1700
$Comp
L power:GND #PWR012
U 1 1 567C5089
P 5450 2150
F 0 "#PWR012" H 5450 1900 50  0001 C CNN
F 1 "GND" H 5450 2000 50  0000 C CNN
F 2 "" H 5450 2150 60  0000 C CNN
F 3 "" H 5450 2150 60  0000 C CNN
	1    5450 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 2150 5450 2100
Wire Wire Line
	-2500 900  -2500 700 
Wire Wire Line
	-2250 700  -2250 800 
Wire Wire Line
	-2250 250  -2250 400 
Wire Wire Line
	-2500 500  -2500 400 
Wire Wire Line
	-2500 400  -2250 400 
Connection ~ -2250 400 
Text Label -2450 900  0    60   ~ 0
SCL
Text Label -2250 800  0    60   ~ 0
SDA
Text Label -1950 700  0    60   ~ 0
SLD
$Comp
L ArduinoSpecAn-rescue:R_Small R12
U 1 1 569C48EE
P 7700 2000
F 0 "R12" V 7800 1950 50  0000 L CNN
F 1 "1k" V 7600 1950 50  0000 L CNN
F 2 "footprints:Custom_0805" H 7700 2000 60  0001 C CNN
F 3 "" H 7700 2000 60  0000 C CNN
	1    7700 2000
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R11
U 1 1 569C497B
P 7000 2200
F 0 "R11" V 7100 2150 50  0000 L CNN
F 1 "1k" V 6900 2150 50  0000 L CNN
F 2 "footprints:Custom_0805" H 7000 2200 60  0001 C CNN
F 3 "" H 7000 2200 60  0000 C CNN
	1    7000 2200
	-1   0    0    1   
$EndComp
Wire Wire Line
	7600 2000 7000 2000
Connection ~ 7000 2000
Wire Wire Line
	8450 2000 7800 2000
$Comp
L power:GND #PWR013
U 1 1 569C4E3C
P 7000 2400
F 0 "#PWR013" H 7000 2150 50  0001 C CNN
F 1 "GND" H 7000 2250 50  0000 C CNN
F 2 "" H 7000 2400 60  0000 C CNN
F 3 "" H 7000 2400 60  0000 C CNN
	1    7000 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 2300 7000 2400
$Comp
L ArduinoSpecAn-rescue:MMBT3904 Q1
U 1 1 569C5979
P -4200 4950
F 0 "Q1" H -4000 5025 50  0000 L CNN
F 1 "MMBT3904" H -4000 4950 50  0000 L CNN
F 2 "footprints:SOT-23" H -4000 4875 50  0001 L CIN
F 3 "" H -4200 4950 50  0000 L CNN
	1    -4200 4950
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:MMBT3904 Q2
U 1 1 569C5AE9
P -3500 4650
F 0 "Q2" H -3300 4725 50  0000 L CNN
F 1 "MMBT3904" H -3300 4650 50  0000 L CNN
F 2 "footprints:SOT-23" H -3300 4575 50  0001 L CIN
F 3 "" H -3500 4650 50  0000 L CNN
	1    -3500 4650
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R5
U 1 1 569C5CEA
P -4100 4400
F 0 "R5" H -4070 4420 50  0000 L CNN
F 1 "220" H -4070 4360 50  0000 L CNN
F 2 "footprints:Custom_0805" H -4100 4400 60  0001 C CNN
F 3 "" H -4100 4400 60  0000 C CNN
	1    -4100 4400
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R7
U 1 1 569C5E7A
P -3400 5850
F 0 "R7" H -3370 5870 50  0000 L CNN
F 1 "220" H -3370 5810 50  0000 L CNN
F 2 "footprints:Custom_0805" H -3400 5850 60  0001 C CNN
F 3 "" H -3400 5850 60  0000 C CNN
	1    -3400 5850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:POT Pot1
U 1 1 569C5F66
P -4900 4950
F 0 "Pot1" H -4900 4850 50  0000 C CNN
F 1 "1k" H -4900 4950 50  0000 C CNN
F 2 "footprints:ST4ETB_Trim_Pot" H -4900 4950 60  0001 C CNN
F 3 "" H -4900 4950 60  0000 C CNN
	1    -4900 4950
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C3
U 1 1 569C622C
P -5300 4950
F 0 "C3" H -5290 5020 50  0000 L CNN
F 1 "10uF" H -5290 4870 50  0000 L CNN
F 2 "footprints:Custom_0805" H -5300 4950 60  0001 C CNN
F 3 "" H -5300 4950 60  0000 C CNN
	1    -5300 4950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	-5200 4950 -5150 4950
Wire Wire Line
	-5400 4950 -5550 4950
Text Label -5550 4950 2    60   ~ 0
RF
$Comp
L ArduinoSpecAn-rescue:R_Small R4
U 1 1 569C72B0
P -4450 5850
F 0 "R4" H -4420 5870 50  0000 L CNN
F 1 "100" H -4420 5810 50  0000 L CNN
F 2 "footprints:Custom_0805" H -4450 5850 60  0001 C CNN
F 3 "" H -4450 5850 60  0000 C CNN
	1    -4450 5850
	1    0    0    -1  
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R6
U 1 1 569C7362
P -3900 5500
F 0 "R6" H -3870 5520 50  0000 L CNN
F 1 "220" H -3870 5460 50  0000 L CNN
F 2 "footprints:Custom_0805" H -3900 5500 60  0001 C CNN
F 3 "" H -3900 5500 60  0000 C CNN
	1    -3900 5500
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:R_Small R8
U 1 1 569C7601
P -3200 5100
F 0 "R8" H -3170 5120 50  0000 L CNN
F 1 "47" H -3170 5060 50  0000 L CNN
F 2 "footprints:Custom_0805" H -3200 5100 60  0001 C CNN
F 3 "" H -3200 5100 60  0000 C CNN
	1    -3200 5100
	0    -1   -1   0   
$EndComp
$Comp
L ArduinoSpecAn-rescue:C_Small C6
U 1 1 569C7704
P -2900 5100
F 0 "C6" H -2890 5170 50  0000 L CNN
F 1 "10uF" H -2890 5020 50  0000 L CNN
F 2 "footprints:Custom_0805" H -2900 5100 60  0001 C CNN
F 3 "" H -2900 5100 60  0000 C CNN
	1    -2900 5100
	0    -1   -1   0   
$EndComp
Wire Wire Line
	-4500 4950 -4450 4950
Wire Wire Line
	-4450 4950 -4450 5500
Connection ~ -4450 4950
Wire Wire Line
	-4450 5500 -4000 5500
Connection ~ -4450 5500
Wire Wire Line
	-3400 4850 -3400 5100
Wire Wire Line
	-4100 4500 -4100 4650
Wire Wire Line
	-4100 4300 -4100 4200
Wire Wire Line
	-4100 4200 -3750 4200
Wire Wire Line
	-3400 4200 -3400 4450
Wire Wire Line
	-3750 4200 -3750 4050
Connection ~ -3750 4200
Text Label -3750 4050 0    60   ~ 0
5V
Wire Wire Line
	-4100 4650 -3700 4650
Connection ~ -4100 4650
Wire Wire Line
	-3800 5500 -3400 5500
Connection ~ -3400 5500
Wire Wire Line
	-3300 5100 -3400 5100
Connection ~ -3400 5100
Wire Wire Line
	-3100 5100 -3000 5100
$Comp
L power:GND #PWR014
U 1 1 569C8DF9
P -4100 5200
F 0 "#PWR014" H -4100 4950 50  0001 C CNN
F 1 "GND" H -4100 5050 50  0000 C CNN
F 2 "" H -4100 5200 60  0000 C CNN
F 3 "" H -4100 5200 60  0000 C CNN
	1    -4100 5200
	1    0    0    -1  
$EndComp
Wire Wire Line
	-4100 5200 -4100 5150
$Comp
L ArduinoSpecAn-rescue:SMA J2
U 1 1 569C9F74
P -2350 5100
F 0 "J2" H -2600 5000 60  0000 C CNN
F 1 "SMA" H -2350 5300 60  0000 C CNN
F 2 "footprints:SMA_Edgemount" H -2350 5100 60  0001 C CNN
F 3 "" H -2350 5100 60  0000 C CNN
	1    -2350 5100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	-2800 5100 -2550 5100
$Comp
L power:GND #PWR015
U 1 1 569CA262
P -4450 6050
F 0 "#PWR015" H -4450 5800 50  0001 C CNN
F 1 "GND" H -4450 5900 50  0000 C CNN
F 2 "" H -4450 6050 60  0000 C CNN
F 3 "" H -4450 6050 60  0000 C CNN
	1    -4450 6050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR016
U 1 1 569CA2F7
P -3400 6050
F 0 "#PWR016" H -3400 5800 50  0001 C CNN
F 1 "GND" H -3400 5900 50  0000 C CNN
F 2 "" H -3400 6050 60  0000 C CNN
F 3 "" H -3400 6050 60  0000 C CNN
	1    -3400 6050
	1    0    0    -1  
$EndComp
Wire Wire Line
	-3400 5950 -3400 6050
Wire Wire Line
	-4450 6050 -4450 5950
$Comp
L power:GND #PWR017
U 1 1 569CA61D
P -2350 5650
F 0 "#PWR017" H -2350 5400 50  0001 C CNN
F 1 "GND" H -2350 5500 50  0000 C CNN
F 2 "" H -2350 5650 60  0000 C CNN
F 3 "" H -2350 5650 60  0000 C CNN
	1    -2350 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	-2500 5450 -2500 5550
Wire Wire Line
	-2500 5550 -2400 5550
Wire Wire Line
	-2200 5550 -2200 5450
Wire Wire Line
	-2400 5450 -2400 5550
Connection ~ -2400 5550
Wire Wire Line
	-2300 5450 -2300 5550
Connection ~ -2300 5550
Wire Wire Line
	-2350 5650 -2350 5550
Connection ~ -2350 5550
Wire Wire Line
	-4900 4800 -4900 4750
Wire Wire Line
	-4900 4750 -4500 4750
Wire Wire Line
	-4500 4750 -4500 4950
NoConn ~ -4650 4950
Text Notes -2050 5100 0    60   ~ 0
50 Ohm output impedance.\nWill drive 0 dBm into 50 Ohm load.
Wire Wire Line
	-1850 -350 -1850 -300
Wire Wire Line
	4200 950  4700 950 
Wire Wire Line
	5400 950  5800 950 
Wire Wire Line
	-10100 500  -10100 700 
Wire Wire Line
	-11100 500  -10100 500 
Wire Wire Line
	-11050 1000 -11050 1050
Wire Wire Line
	-7550 1200 -7550 1300
Wire Wire Line
	-7550 1300 -7550 1550
Wire Wire Line
	-7550 400  -7550 600 
Wire Wire Line
	-7550 200  -7550 400 
Wire Wire Line
	-7550 100  -7550 200 
Wire Wire Line
	-7550 600  -7550 900 
Wire Wire Line
	-7550 900  -7550 1200
Wire Wire Line
	-7550 1550 -7550 1650
Wire Wire Line
	-6650 700  -6350 700 
Wire Wire Line
	-5550 700  -5450 700 
Wire Wire Line
	-5950 700  -5850 700 
Wire Wire Line
	-6350 700  -6250 700 
Wire Wire Line
	-5150 700  -4850 700 
Wire Wire Line
	-6350 1250 -5950 1250
Wire Wire Line
	-5950 1250 -5750 1250
Wire Wire Line
	-5550 1250 -5150 1250
Wire Wire Line
	-5150 1250 -4850 1250
Wire Wire Line
	-5750 1250 -5550 1250
Wire Wire Line
	-4850 700  -4650 700 
Wire Wire Line
	-9700 900  -9700 1750
Wire Wire Line
	-9700 400  -9700 900 
Wire Wire Line
	-9700 100  -9700 400 
Wire Wire Line
	-9350 500  -9350 1000
Wire Wire Line
	-9350 300  -9350 500 
Wire Wire Line
	-9350 200  -9350 300 
Wire Wire Line
	5350 1700 5450 1700
Wire Wire Line
	-8900 -650 -8750 -650
Wire Wire Line
	-8650 -650 -8400 -650
Wire Wire Line
	-8750 -650 -8750 -500
Wire Wire Line
	-8900 -1050 -8750 -1050
Wire Wire Line
	-8650 -1050 -8400 -1050
Wire Wire Line
	8450 1250 8600 1250
Wire Wire Line
	5950 1350 6000 1350
Wire Wire Line
	6050 1350 6150 1350
Wire Wire Line
	6000 1350 6050 1350
Wire Wire Line
	5450 1700 5650 1700
Wire Wire Line
	-2250 400  -2250 500 
Wire Wire Line
	7000 2000 7000 2100
Wire Wire Line
	-4450 4950 -4400 4950
Wire Wire Line
	-4450 5500 -4450 5750
Wire Wire Line
	-3750 4200 -3400 4200
Wire Wire Line
	-4100 4650 -4100 4750
Wire Wire Line
	-3400 5500 -3400 5750
Wire Wire Line
	-3400 5100 -3400 5500
Wire Wire Line
	-2400 5550 -2350 5550
Wire Wire Line
	-2300 5550 -2200 5550
Wire Wire Line
	-2350 5550 -2300 5550
$Comp
L MCU_Module:Arduino_Nano_v3.x A?
U 1 1 5B672321
P 2100 2250
F 0 "A?" H 2100 1164 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 2100 1073 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 2250 1300 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 2100 1250 50  0001 C CNN
	1    2100 2250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5B67284E
P 2150 3550
F 0 "#PWR?" H 2150 3300 50  0001 C CNN
F 1 "GND" H 2155 3377 50  0000 C CNN
F 2 "" H 2150 3550 50  0001 C CNN
F 3 "" H 2150 3550 50  0001 C CNN
	1    2150 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 3250 2150 3250
Wire Wire Line
	2150 3250 2150 3550
Connection ~ 2150 3250
Wire Wire Line
	2150 3250 2100 3250
Wire Wire Line
	2100 1250 2100 1100
Wire Wire Line
	2400 1250 2400 1100
$Comp
L power:+3V3 #PWR?
U 1 1 5B6A5A5B
P 2100 1100
F 0 "#PWR?" H 2100 950 50  0001 C CNN
F 1 "+3V3" H 2115 1273 50  0000 C CNN
F 2 "" H 2100 1100 50  0001 C CNN
F 3 "" H 2100 1100 50  0001 C CNN
	1    2100 1100
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5B6A5B31
P 2400 1100
F 0 "#PWR?" H 2400 950 50  0001 C CNN
F 1 "+5V" H 2415 1273 50  0000 C CNN
F 2 "" H 2400 1100 50  0001 C CNN
F 3 "" H 2400 1100 50  0001 C CNN
	1    2400 1100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 1250 2300 1250
Wire Wire Line
	2200 1250 2100 1250
Text Notes 3400 600  0    60   ~ 0
Input
Wire Notes Line
	3400 600  10350 600 
Wire Notes Line
	10350 600  10350 3550
Wire Notes Line
	10350 3550 3400 3550
Wire Notes Line
	3400 3550 3400 600 
$Comp
L ArduinoSpecAn-rescue:SMA J1
U 1 1 5B70300F
P 6000 950
F 0 "J1" H 5762 897 60  0000 R CNN
F 1 "SMA" H 5762 791 60  0000 R CNN
F 2 "" H 6000 950 60  0000 C CNN
F 3 "" H 6000 950 60  0000 C CNN
	1    6000 950 
	-1   0    0    -1  
$EndComp
Text Label 2850 2250 2    60   ~ 0
A0
Wire Wire Line
	2850 2250 2600 2250
Text Notes 9550 1350 0    60   ~ 0
Decoupling Caps:\n- LM7301 x 1
Wire Wire Line
	9350 900  9350 1150
Wire Wire Line
	-8750 -1050 -8750 -1250
Connection ~ -8750 -1050
Wire Wire Line
	-8750 -1050 -8650 -1050
Connection ~ -8750 -650
Wire Wire Line
	-8750 -650 -8650 -650
$Comp
L power:GND #PWR?
U 1 1 5B7475F9
P 9350 1500
F 0 "#PWR?" H 9350 1250 50  0001 C CNN
F 1 "GND" H 9350 1350 50  0000 C CNN
F 2 "" H 9350 1500 60  0000 C CNN
F 3 "" H 9350 1500 60  0000 C CNN
	1    9350 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 1350 9350 1500
Text Label -8750 -1250 0    60   ~ 0
5V
$EndSCHEMATC
