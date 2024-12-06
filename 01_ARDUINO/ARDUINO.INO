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
void loop() {
  // Lectura de sensores de presencia
  presenciaA = digitalRead(finalcarA);
  presenciaB = digitalRead(finalcarB);

  if (presenciaA == LOW || presenciaB == LOW) {
    digitalWrite(led1, HIGH);
    delay(2000);
    digitalWrite(led1, LOW);
  } else {
    digitalWrite(led1, LOW);
  }
  // Lectura de potenciómetros y ajuste de luminosidad
  int medida1 = analogRead(poten1);
  int medida2 = analogRead(poten2);
  lumin1 = map(medida1, 8, 1015, 255, 0);
  lumin2 = map(medida2, 8, 1015, 255, 0);

  analogWrite(led2, lumin1);
  analogWrite(led3, lumin2);

  // Creación del objeto JSON
  StaticJsonDocument<200> jsonDoc;
  jsonDoc["datos1"] = presenciaA;
  jsonDoc["datos2"] = presenciaB;
  jsonDoc["datos3"] = lumin1;
  jsonDoc["datos4"] = lumin2;

// Convertir el JSON a string y enviarlo por Serial
  String output;
  serializeJson(jsonDoc, output);
  Serial.println(output);

  delay(500); // Espera para evitar lecturas excesivas
}