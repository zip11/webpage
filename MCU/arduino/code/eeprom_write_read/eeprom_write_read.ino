#include <EEPROM.h>

int address = 0;
byte value;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {

  value = 222;
  
  // put your main code here, to run repeatedly:
  // EEPROM.write(address,value);
  delay(100);

  // read a byte from the current address of the EEPROM
  value = EEPROM.read(address);

  Serial.print(address);
  Serial.print("\t");
  Serial.print(value, DEC);
  Serial.println();

  address = address + 1;
  if (address == EEPROM.length()) {
    address = 0;
  }

  delay(500);


}
