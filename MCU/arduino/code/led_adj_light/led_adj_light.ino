int pushButton = 2;
int ledPin = 9;
int ledlight = 10;


void setup() {

  // put your setup code here, to run once:
  pinMode(pushButton, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  // put your main code here, to run repeatedly:


  bool kg2 = digitalRead(pushButton);

  if (!kg2) {

    if (ledlight < 255) {
      ledlight = ledlight + 1;
    } else {

      if (ledlight > 0) {
        ledlight = ledlight - 1;
      } else {
        ledlight = 0;
      }
    }

  } else {
    if (ledlight == 254) {
      ledlight = 0;
    }
  }

  delay(10);

  analogWrite(ledPin, ledlight);

  Serial.println("light");
  Serial.println(ledlight);
  
  delay(10);
}
