#define ingresoMoneda 12  //Aquí definimos los pines
#define moneda 2     // El boton va a simular el paso de una moneda     
#define potenciometro A0  //El valor de potenciometro va a simular que tan lleno está una botella

void setup() {
  pinMode(ingresoMoneda, INPUT_PULLUP); 
  pinMode(moneda, OUTPUT);             
}

void loop() {
  int medida = analogRead(potenciometro);         
  int ponderacion = map(medida, 8, 1015, 0, 10);  
  int tiempo = ponderacion * 1000;               

  // Lee el estado del botón de ingreso de moneda
  if (digitalRead(ingresoMoneda) == LOW) { 
    if (ponderacion <= 9) {                
      digitalWrite(moneda, HIGH);          
      delay(tiempo);                      
      digitalWrite(moneda, LOW);          
    } else {
      digitalWrite(moneda, LOW);           
    }
  } else {
    digitalWrite(moneda, LOW);             
  }
}