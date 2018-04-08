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
  int red = 0;
  int blue = 0;
  int green = 0;

  while (Serial.available()>0)
  {
    red = Serial.parseInt();
    green = Serial.parseInt();
    blue = Serial.parseInt();
  
    if (Serial.read() == '\n') {
      Serial.println("Data read ");
      red = constrain(red, 0, 255);
      green = constrain(green, 0 , 255);
      blue = constrain(blue, 0, 255);
      analogWrite(REDLEDPIN, red);
      analogWrite(GREENLEDPIN, green);
      analogWrite(BLUELEDPIN, blue);
    }
  }
} 
