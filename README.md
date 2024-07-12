# GSM Based Home Security System

## Introduction
This project demonstrates the implementation of a GSM-based home security system using an Arduino UNO. The system can detect obstacles using an IR sensor and send an SMS notification through a GSM module.

## Description
The security system uses a GSM module to send notifications to a mobile phone when an obstacle is detected by the IR sensor. An LED is also used to indicate detection visually. The GSM module uses AT commands to send SMS messages. When the IR sensor detects an obstacle, the LED turns on, and a message is sent to a predefined mobile number. The system can be monitored via the serial monitor in the Arduino IDE.

## Components Required
- Arduino UNO
- IR sensor
- LED
- 220 ohm resistor
- Jumper wires and a breadboard
- GSM SIM 900 module
- USB cable for uploading the code

## Circuit Diagram
### Connections
- **Arduino UNO to GSM SIM 900 Module**
  - 11 Pin → RX Pin
  - 10 Pin → TX Pin
  - GND → GND
- **Arduino UNO to IR Sensor**
  - 7 Pin → OUT Pin
  - 5 V → VCC
  - GND → GND
- **Arduino UNO to LED and 220 Ohm Resistor**
  - 4 Pin → Anode Terminal
  - GND → Cathode Terminal via 220 Ohm Resistor

## Code


#include <SoftwareSerial.h>

SoftwareSerial SIM900A(10, 11);

int val = 0;

void setup() {

    Serial.begin(9600);
    SIM900A.begin(9600);
    pinMode(4, HIGH);
    
}

void loop() {

    val = digitalRead(7);
    
    Serial.println(val);
    delay(1000);
    
    if (Serial.available() > 0) {
        switch (Serial.read());
    }
    
    if (SIM900A.available() > 0) {
        Serial.write(SIM900A.read());
    }
    
    if (val == 0) {
        Serial.println("Obstacle Detecting");
        digitalWrite(4, HIGH);
        Serial.println("Sending Message");
        SIM900A.println("AT+CMGF=1");
        delay(1000);
        Serial.println("Set SMS Number");
        SIM900A.println("AT+CMGS=\"xxxxxxxxxx\"\r");
        delay(1000);
        Serial.println("Set SMS Content");
        SIM900A.println("Someone is coming, be safe");
        delay(100);
        Serial.println("Finish");
        SIM900A.println((char)26);
        delay(1000);
        Serial.println("Message has been sent");
        digitalWrite(4, LOW);
    }
}

```
