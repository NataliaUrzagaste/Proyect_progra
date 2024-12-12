const int sensorMoneda = 4; 
const int buzzer = 5;       
const int finalCarrera = 6;  
const int relayBomba = 7;   

// Notas musicales en frecuencias (Hz)
const int NOTE_C4 = 262; 
const int NOTE_E4 = 330;
const int NOTE_G4 = 392;
const int NOTE_C5 = 523; 

// Contador de monedas
int contadorMonedas = 0;

// Función para enviar datos en formato JSON
void enviarDatosJSON(int sensorMonedaEstado, bool finalCarreraEstado, bool relayBombaEstado, const char* estado) {
  String json = "{";
  json += "\"sensorMoneda\":" + String(sensorMonedaEstado) + ","; // Estado del sensor de moneda
  json += "\"contadorMonedas\":" + String(contadorMonedas) + ",";  // Número de monedas detectadas
  json += "\"finalCarrera\":" + String(finalCarreraEstado ? 1 : 0) + ","; // Estado final de carrera
  json += "\"relayBomba\":" + String(relayBombaEstado ? 1 : 0) + ","; // Estado del relay de la bomba
  json += "\"estado\":\"" + String(estado) + "\""; 
  json += "}";

  Serial.println(json);  // Enviar el JSON por el puerto serial
}

void setup() {
  pinMode(sensorMoneda, INPUT_PULLUP); // Detector de monedas con pull-up
  pinMode(buzzer, OUTPUT);             // Buzzer como salida
  pinMode(finalCarrera, INPUT_PULLUP); // Final de carrera con pull-up
  pinMode(relayBomba, OUTPUT);         // Relay como salida
  
  digitalWrite(relayBomba, LOW);       
  Serial.begin(9600);                  
}

void loop() {
  int sensorState = digitalRead(sensorMoneda);      
  bool finalCarreraEstado = digitalRead(finalCarrera) == HIGH;
  bool relayBombaEstado = digitalRead(relayBomba) == HIGH;

  // Detectar moneda (estado alto)
  if (sensorState == HIGH) { 
    contadorMonedas++; // Incrementar el contador de monedas
    enviarDatosJSON(sensorState, finalCarreraEstado, relayBombaEstado, "Moneda detectada");
    tone(buzzer, 1000, 500);             
    delay(500);                           // Pequeño retraso para evitar rebotes

    // Esperar a que se active el final de carrera
    while (digitalRead(finalCarrera) == LOW) {
      delay(10);
    }

    // Final de carrera activado
    finalCarreraEstado = true;
    enviarDatosJSON(sensorState, finalCarreraEstado, relayBombaEstado, "Final de carrera activado");
    tone(buzzer, 1000, 1000);            
    delay(1000);

    // Activar bomba
    digitalWrite(relayBomba, HIGH);       
    relayBombaEstado = true;
    enviarDatosJSON(sensorState, finalCarreraEstado, relayBombaEstado, "Bomba activada");
    delay(10000);                          // Bomba funcionando durante 10 segundos

    // Apagar bomba
    digitalWrite(relayBomba, LOW);       
    relayBombaEstado = false;
    enviarDatosJSON(sensorState, finalCarreraEstado, relayBombaEstado, "Bomba apagada");

    playSuccessMelody();
  }

  delay(10);
}

void playSuccessMelody() {
  // Melodía de éxito 
  int melody[] = {NOTE_C4, NOTE_E4, NOTE_G4, NOTE_C5}; 
  int durations[] = {200, 200, 200, 400};              // Duración de cada nota

  for (int i = 0; i < 4; i++) {
    tone(buzzer, melody[i], durations[i]); // Tocar la nota
    delay(durations[i] + 50);              // Esperar el tiempo de la nota más un pequeño descanso
  }
}