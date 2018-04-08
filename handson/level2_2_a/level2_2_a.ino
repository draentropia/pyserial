// LEDS
const int GREENLEDPIN = 9;
const int BLUELEDPIN = 10;
const int REDLEDPIN = 11;
int greenLedVal;
int blueLedVal;
int redLedVal;
// Potenciometros
const int GREENPOTPIN = A3;
const int BLUEPOTPIN = A0;
const int REDPOTPIN = A2;
int greenPotVal = 0;
int bluePotVal = 0;
int redPotVal = 0;

void setup() {
  Serial.begin(9600);
  pinMode(GREENLEDPIN, OUTPUT);
  pinMode(BLUELEDPIN, OUTPUT);
  pinMode(REDLEDPIN, OUTPUT);
}

void loop() {
  greenPotVal = analogRead(GREENPOTPIN);
  Serial.print("green potval: ");
  Serial.print(greenPotVal);
  // Pot [0,1023], mapping to [0.255]
  greenLedVal = map(greenPotVal, 0, 1023, 0, 255);
  Serial.print(" green ledval: ");
  Serial.print(greenLedVal);

  bluePotVal = analogRead(BLUEPOTPIN);
  Serial.print(" | blue potval: ");
  Serial.print(bluePotVal);
  // Pot [0,1023], mapping to [0.255]
  blueLedVal = map(bluePotVal, 0, 1023, 0, 255);
  Serial.print(" blue ledval: ");
  Serial.print(blueLedVal);
  
  redPotVal = analogRead(REDPOTPIN);
  Serial.print(" | red potval: ");
  Serial.print(redPotVal);
  // Pot [0,1023], mapping to [0.255]
  redLedVal = map(redPotVal, 0, 1023, 0, 255);
  Serial.print(" red ledval: ");
  Serial.println(redLedVal);

  analogWrite(GREENLEDPIN, greenLedVal);
  analogWrite(BLUELEDPIN, blueLedVal);
  analogWrite(REDLEDPIN, redLedVal);
  delay(1000);
  }

