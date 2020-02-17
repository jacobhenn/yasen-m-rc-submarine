#include <Servo.h>

Servo ESC;

ESCPin = 9;

int potValue;

void setup() {
	ESC.attach(ESCPin, 1000, 2000);
}

void loop() {
	while (motorValue < 180) {
		motorValue = motorValue + 10;
		ESC.write(motorValue);
		delay(1000);
	}
	motorValue = 0;
}
