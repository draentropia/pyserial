const int GREENLEDPIN = 9;
const int BLUELEDPIN = 10;
const int REDLEDPIN = 11;


void setup() {
  pinMode(GREENLEDPIN, OUTPUT);
  pinMode(BLUELEDPIN, OUTPUT);
  pinMode(REDLEDPIN, OUTPUT);
}

void loop() {
  // 255 en cada uno y un delay
  analogWrite(REDLEDPIN, 255);
  analogWrite(BLUELEDPIN, 0);
  analogWrite(GREENLEDPIN, 0);
  delay(500);
  
  analogWrite(REDLEDPIN, 0);
  analogWrite(BLUELEDPIN, 255);
  analogWrite(GREENLEDPIN, 0);
  delay(500);

  analogWrite(REDLEDPIN, 0);
  analogWrite(BLUELEDPIN, 0);
  analogWrite(GREENLEDPIN, 255);
  delay(500);
  }
