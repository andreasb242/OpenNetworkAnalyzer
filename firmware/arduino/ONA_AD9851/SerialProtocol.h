/**
 * Arduino Firmware OpenNetworkAnalyzer
 *
 * Communication implementation
 * Requests and Responds are always a single line, ending with '\n'
 * Responds starts with 'E' for error, with 'O' for OK
 *
 * ** THIS FILE IS SHARED WITH ALL ARDUINO PROJECT,
 *    NEEDS TO BE COPIED TO ALL FOLDER ON CHANGE!
 *    (if there is a simpler solution: please tell me) **
 * License: GPLv3
 * Author: Andreas Butti
*/

#include <Arduino.h>
#include "version.h"

/**
   Lenght of the command buffer
*/
#define CMD_BUFFER_SIZE 64


/**
 * Needs to be implemented by the firmware
 */
class ONACommand {
public:
  /**
   * Get info string to return to the application
   */
  virtual const char* getInfoString() = 0;

  /**
   * Set the frequency
   * 
   * @return true on success, false e.g. if out out of range
   */
  virtual bool setFrequency(uint32_t freq) = 0;

  /**
   * Read input value
   * 
   * @return Read value
   */
  virtual uint32_t readInput() = 0;
};


class ONACom {
public:

  /**
   * Constructor
   */
  ONACom(ONACommand& cmd) :
    command(cmd),
    bufferPos(0)
  {
  }

  /**
   * Setup serical communication
   */
  void setup() {
    // 500000 is working, if the UART-USB Chip supports it
    // But there is no feelable speed improvements
    Serial.begin(115200);
  }

  /**
   * Read a single command, execute it
   */
  void executeCommand() {
    boolean completed = false;

    while (Serial.available()) {
      char ch = (char)Serial.read();
      if (ch == '\n') {
        completed = true;
        break;
      }

      buffer[bufferPos] = ch;
      bufferPos++;
      if (bufferPos == CMD_BUFFER_SIZE) {
        // Command to long
        Serial.println("E1: Command to long!");
        bufferPos = 0;
        return;
      }
    }

    if (!completed || bufferPos == 0) {
      // No complete command received
      return;
    }

    buffer[bufferPos] = 0;

    processCommand();

    bufferPos = 0;
    return;
  }

private:
  /**
   * Process the received command
   */
  void processCommand() {
    // Get information about this board
    if (buffer[0] == 'i') {
      Serial.print("O:");
      Serial.println(command.getInfoString());

    
    // Get Version information
    } else if (buffer[0] == 'v') {
      Serial.print("O:");
      Serial.println("BOARD=" BOARD_TYPE ",FW=" SOFTWARE_VERSION ",BUILD=" __DATE__ "-" __TIME__);

    
    // Set Frequency
    } else if (buffer[0] == 'f') {
      uint32_t freq = atol(buffer + 1);
      if (command.setFrequency(freq)) {
        Serial.print("O: set freq to ");
        Serial.print(freq);
        Serial.println("Hz");
      } else {
        Serial.println("E3: Set failed");
      }

    // Read value
    } else if (buffer[0] == 'r') {
      uint32_t value = command.readInput();
      Serial.print("O:");
      Serial.println(value);


    // Invalid Command
    } else {
      Serial.print("E2: Invalid command: ");
      Serial.println(buffer);
    }
  }

  // Attributes
private:
  /**
   * Command implementation
   */
  ONACommand& command;

  /**
   * Read buffer
   */
  char buffer[CMD_BUFFER_SIZE];

  /**
   * Buffer position
   */
  uint8_t bufferPos;
};

