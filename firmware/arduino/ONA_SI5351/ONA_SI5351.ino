/**
 * Arduino Firmware for Testing OpenNetworkAnalyzer
 * 
 * This Firmware does not need any additional Hardware.
 * The Output Pin is D5, the input pin A0
 * 
 * License: GPLv3
 * Author: Andreas Butti
 */

#include "SerialProtocol.h"

#include "si5351.h"
#include "Wire.h"

Si5351 si5351;

/**
 * Initialized flag
 */
bool g_hwInitialized = false;

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

    return "MINFREQ=4000,MAXFREQ=175000000";
  }

  /**
   * Set the frequency
   * 
   * @return true on success, false e.g. if out out of range
   */
  bool setFrequency(uint32_t freq) {
    if (freq < 4000) {
      // Less than 4kHz are not working with this IC / Lib
      return false;
    }

    if (!g_hwInitialized) {
      bool i2c_found = si5351.init(SI5351_CRYSTAL_LOAD_8PF, 0, 0);
      if (!i2c_found) {
        // Error LED
        digitalWrite(13, HIGH);

        Serial.print("E4: I2C Device not found!, ");
        return false;
      }
      g_hwInitialized = true;
    }
    
    // Set CLK0 to output 14 MHz
    si5351.set_freq(freq * 100ULL, SI5351_CLK0);
    
    // Query a status update and wait a bit to let the Si5351 populate the
    // status flags correctly.
    si5351.update_status();


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

  // State LEDs

  // Active LED
  pinMode(A1, OUTPUT);
  // Connected LED
  pinMode(A2, OUTPUT);
  // Error LED
  pinMode(13, OUTPUT);
}

/**
 * Main Loop
 */
void loop() {
  com.executeCommand();
}

