const int GREENLEDPIN = 9;
const int BLUELEDPIN = 10;
const int REDLEDPIN = 11;


void setup() {
  Serial.begin(9600);
  pinMode(GREENLEDPIN, OUTPUT);
  pinMode(BLUELEDPIN, OUTPUT);
  pinMode(REDLEDPIN, OUTPUT);
}

void loop() {
  // 255 en cada uno y un delay
  analogWrite(REDLEDPIN, 255);
  analogWrite(BLUELEDPIN, 0);
  analogWrite(GREENLEDPIN, 0);
  Serial.println("RED on");
  delay(1500);
  
  analogWrite(REDLEDPIN, 0);
  analogWrite(BLUELEDPIN, 255);
  analogWrite(GREENLEDPIN, 0);
  Serial.println("RED off, BLUE on");
  delay(1500);

  analogWrite(REDLEDPIN, 0);
  analogWrite(BLUELEDPIN, 0);
  analogWrite(GREENLEDPIN, 255);
  Serial.println("BLUE off, GREEN on");
  delay(1500);
  }
