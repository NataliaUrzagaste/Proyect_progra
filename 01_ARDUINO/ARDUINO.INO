#include <ArduinoJson.h>
#include <SoftwareSerial.h>

#define finalcarA 2
#define finalcarB 4
#define poten1 A0
#define poten2 A1
#define led1 7
#define led2 5
#define led3 9

int presenciaA;
int presenciaB;
int lumin1;
int lumin2;

void setup() {
  pinMode(finalcarA, INPUT_PULLUP);
  pinMode(finalcarB, INPUT_PULLUP);
  pinMode(poten1, INPUT);
  pinMode(poten2, INPUT);
  
  pinMode(led1, OUTPUT);
  digitalWrite(led1, LOW);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  
  Serial.begin(9600);
}