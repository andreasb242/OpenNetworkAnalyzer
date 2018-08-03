# OpenNetworkAnalyzer
Improved software for https://hackaday.io/project/10021-arduino-network-analyzer

## Hardware
There are different hardware implementations, some based on Arduino, for an easy Start.

### Arduino
*firmware/arduino/ONA_PWM* is a firmware, which does not need any additional hardware.
The Pin *D5* is used as output, without any filtering, the Pin *A0* is used as input.
This firmware can be used to easy check how it's working, wihtout bying / building hardware.

But the output is a rectangular signal, which isn't really working for testing, as a rectangular signal contains different frequenecies instead of one.
Therefore this is only for testing purpose.

*Maximum Frequency* is 62500Hz, really low.

*firmware/arduino/ONA_AD9851* is the Version based on the first software-hackday.io Version.
There is the Arduino Uno Shield, layout located at *layout/hackaday.io-V2.0*.

And there is an Arduino Nano Version, located at *layout/arduino-nano-AD9851*


*firmware/arduino/ONA_SI5351*
Not yet ready

### STM32 USB
Not yet ready.

## Screenshots
![Screenshot](/screenshot/main.png?raw=true "Application Window Screenshot")

## Installation / running
### Ubuntu
    git clone https://github.com/andreasb242/OpenNetworkAnalyzer.git
    sudo apt install python3-tk python3-numpy python3-serial python3-pil.imagetk
    cd software
    python3 main.py

### Mac OS
    TODO

### Windows
    TODO


