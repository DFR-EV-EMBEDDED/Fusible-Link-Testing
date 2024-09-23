/*
  Read serial value from arduino
*/

void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);
}

void loop() {
  // read the input on analog pin 0
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the voltage value
  Serial.println(voltage);
  delayMicroseconds(5000); // delay for .005 seconds (for 200Hz sample)
}
