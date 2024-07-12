#include <SoftwareSerial.h>

SoftwareSerial SIM900A(10, 11);  // SoftSerial( RX , TX );
// 10 pin connect to TX of GSM SIM 900 Module
// 11 pin connect to RX of GSM SIM 900 Module

int val = 0;

void setup() {
    Serial.begin(9600);   // sensor baud rate
    SIM900A.begin(9600);  // GSM baud rate
    pinMode(4, HIGH);     // LED connect D4
}

void loop() {
    val = digitalRead(7);  // IR sensor output pin connected to D7
    Serial.println(val);   // see the value in serial monitor in Arduino IDE
    delay(1000);

    if (Serial.available() > 0) {
        switch (Serial.read());
    }

    if (SIM900A.available() > 0) {
        Serial.write(SIM900A.read());
    }

    if (val == 0) {  // Check your sensor value 1 or 0
        // in my case IR sensor detects then value is 0 otherwise 1 you can change value
        Serial.println("Obstacle Detecting");
        digitalWrite(4, HIGH);  // LED ON
        Serial.println("Sending Message");
        SIM900A.println("AT+CMGF=1");    // Sets the GSM Module in Text Mode
        delay(1000);
        Serial.println("Set SMS Number");
        SIM900A.println("AT+CMGS=\"xxxxxxxxxx\"\r"); // Mobile phone number to send message, replace x with your number
        delay(1000);
        Serial.println("Set SMS Content");
        SIM900A.println("Someone is coming, be safe"); // Message content
        delay(100);
        Serial.println("Finish");
        SIM900A.println((char)26); // ASCII code of CTRL+Z
        delay(1000);
        Serial.println("Message has been sent");
        digitalWrite(4, LOW);   // LED OFF
    }
}
