/**
 * Arduino Firmware for Testing OpenNetworkAnalyzer
 * 
 * This Firmware does not need any additional Hardware.
 * The Output Pin is D5, the input pin A0
 * 
 * License: GPLv3
 * Author: Brett Killion, Andreas Butti
 */

#include "SerialProtocol.h"

// http://forum.arduino.cc/index.php/topic,117425.0.html
#include "PWM/PWM.h"

// Hack... The Library is included directly...
#include "PWM/utility/ATimerDefs.cpp"
#include "PWM/utility/BTimerDefs.cpp"

/**
 * Command implementation
 */
class ONACommandImpl: public ONACommand {
public:
  /**
   * Get info string to return to the application
   */
  const char* getInfoString() {
    return "MINFREQ=1,MAXFREQ=60000";
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

    // Not really accurate, but working some sort of...
    if (!SetPinFrequency(5, freq)) {
      return false;
    }

   // setting the duty to 50% with the highest possible resolution that 
   // can be applied to the timer (up to 16 bit). 1/2 of 65536 is 32768.
   pwmWriteHR(5, 32768);

    return true;
  }

  /**
   * Read input value
   * 
   * @return Read value
   */
  uint32_t readInput() {
    uint32_t sum = 0;
    
    for (int n = 0; n < 16; n++) {
      sum += analogRead(A0);
    }
    sum = sum >> 2;

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

  // Initialize all timers except for 0, to save time keeping functions
  InitTimersSafe();
}

/**
 * Main Loop
 */
void loop() {
  com.executeCommand();
}

