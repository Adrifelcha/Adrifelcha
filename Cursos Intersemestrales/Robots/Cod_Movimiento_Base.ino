void setup() {
  // put your setup code here, to run once:
pinMode(2, OUTPUT);
pinMode(3, OUTPUT);

pinMode(4, OUTPUT);
pinMode(5, OUTPUT);
}


void Adelante(int time) {
  digitalWrite(2, HIGH);
  digitalWrite(3, LOW);

  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);

  delay(time);
}

void Atras(int time) {
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);

  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);

  delay(time);
}

void Derecha(int time) {
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);

  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);

  delay(time);
}


void Izquierda(int time) {
  digitalWrite(2, HIGH);
  digitalWrite(3, LOW);

  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);

  delay(time);
}

void Stop(int time){
 digitalWrite(2, LOW);
 digitalWrite(3, LOW);

 digitalWrite(4, LOW);
 digitalWrite(5, LOW);

 delay(time);
}

void loop()
{
  // put your main code here, to run repeatedly:
  Adelante(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Adelante(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Adelante(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Adelante(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Adelante(500);
  Stop(2000);
  Atras(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Atras(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Atras(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Atras(500);
  Stop(500);
  Izquierda(130);
  Stop(500);
  Atras(500); 
 }
