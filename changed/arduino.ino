#include <Servo.h>

#define SERVO_PORT 3

Servo myServo;
int val = 0;

void setup(){
  Serial.begin(9600);
  myServo.attach(SERVO_PORT);
  myServo.write(val);
}

void loop(){
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    val = input.toInt();
    if (val >= 0 && val <= 180) {
      myServo.write(val);
      Serial.print("Ok! Angle = ");
      Serial.println(input);
	} else
      Serial.println("Not correct input value!");
  }
}
