/**
 * Arduino Firmware for AD9851 OpenNetworkAnalyzer
 * 
 * License: GPLv3
 * Author: Brett Killion, Andreas Butti
 */

#include "SerialProtocol.h"

/**
 * AD9851 Pins
 */
const int WCLK = A4;
const int DATA = A5;
const int FQ_UD = 8;

/**
 * Set the frequency
 */
void setFreq(long frequency) {
  long FTW = (frequency * pow(2, 24)) / (179999563 / 256);
  long pointer = 1;
  int pointer2 = 0b10000000;
  int lastByte = 0b10000000;

  for (uint8_t i = 0; i < 32; i++) {
    if ((FTW & pointer) > 0) {
      digitalWrite(DATA, HIGH);
    } else {
      digitalWrite(DATA, LOW);
    }

    digitalWrite(WCLK, HIGH);
    digitalWrite(WCLK, LOW);
    pointer = pointer << 1;
  }

  for (uint8_t i = 0; i < 8; i++) {
    if ((lastByte & pointer2) > 0) {
      digitalWrite(DATA, HIGH);
    } else {
      digitalWrite(DATA, LOW);
    }

    digitalWrite(WCLK, HIGH);
    digitalWrite(WCLK, LOW);
    pointer2 = pointer2 >> 1;
  }

  digitalWrite(FQ_UD, HIGH);
  digitalWrite(FQ_UD, LOW);
}

/**
 * Command implementation
 */
class ONACommandImpl: public ONACommand {
public:
  /**
   * Get info string to return to the application
   */
  const char* getInfoString() {
    // Connected LED
    digitalWrite(A2, HIGH);

    return "MINFREQ=1,MAXFREQ=72000000";
  }

  /**
   * Set the frequency
   * 
   * @return true on success, false e.g. if out out of range
   */
  bool setFrequency(uint32_t freq) {
    if (freq < 1) {
      return false;
    }
    if (freq > 72000000) {
      return false;
    }


    return true;
  }

  /**
   * Read input value
   * 
   * @return Read value
   */
  uint32_t readInput() {
    // Active LED
    digitalWrite(A1, HIGH);

    uint32_t sum = 0;
    
    for (int n = 0; n < 16; n++) {
      sum += analogRead(A0);
    }
    sum = sum >> 2;

    // Active LED
    digitalWrite(A1, LOW);

    return sum;
  }
};

/**
 * Command implementation
 */
ONACommandImpl command;

/**
 * Communication interface
 */
ONACom com(command);


/**
 * Setup Hardware
 */
void setup() {
  // Setup communication
  com.setup();

  pinMode(WCLK, OUTPUT);
  pinMode(DATA, OUTPUT);
  pinMode(FQ_UD, OUTPUT);

  // State LEDs
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);

  // Enter serial mode
  digitalWrite(WCLK, HIGH);
  digitalWrite(WCLK, LOW);
  digitalWrite(FQ_UD, HIGH);
  digitalWrite(FQ_UD, LOW);

  setFreq(10000000);
}

/**
 * Main Loop
 */
void loop() {
  com.executeCommand();
}

