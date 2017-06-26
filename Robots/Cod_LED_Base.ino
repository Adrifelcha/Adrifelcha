// Declaramos los pines que vamosa utilizar como Output
void setup() {
  // put your setup code here, to run once:
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
pinMode(9, OUTPUT);
}

//Definimos a qué pines están conectados los colores
int Red = 11;
int Blue = 10;
int Green = 12;

//Creamos una función para resetear (Apagar) los colores
void Reset(int time){
  digitalWrite(Blue,LOW);
  digitalWrite(Red,LOW);
  digitalWrite(Green,LOW);
  delay(time);
}

//FUNCION PRINCIPAL
void loop() {
  // put your main code here, to run repeatedly:

Reset(1000);

// Encender (TODO o NADA)
digitalWrite(Blue, HIGH);
delay(2000);
digitalWrite(Blue, LOW);
delay(2000);
digitalWrite(Red, HIGH);
delay(2000);
digitalWrite(Red, LOW);
delay(2000);
digitalWrite(Green, HIGH);
delay(2000);
digitalWrite(Green, LOW);
delay(2000);

// Tonalidades
// El verde está conectado a una entrada NOanalogica (sin virgulilla) 
// porque esta se usó para configurar la velocidad de las llantas.
// Las entradas digitales (NOanalogicas) slo reciben informacion de On-Off
//y no distinguen entre gradientes de PWM
analogWrite(Red,50);
delay(1000);
analogWrite(Red,100);
delay(1000);
analogWrite(Red,150);
delay(1000);
analogWrite(Red,200);
delay(1000);
analogWrite(Red,255);
delay(1000);
Reset(1000);

analogWrite(Blue,50);
delay(1000);
analogWrite(Blue,100);
delay(1000);
analogWrite(Blue,150);
delay(1000);
analogWrite(Blue,200);
delay(1000);
analogWrite(Blue,255);
delay(1000);
Reset(1000);


// Oscilaciones en color (Ascendente o descendente)
// Rojo
for (int i = 0; i < 51; i = i +10)
{ analogWrite(Red,i);
delay(1000);}
analogWrite(Red,0);
delay(1000);
//Azul
for (int i=0; i < 51; i = i +10)
{ analogWrite(Blue,i);
delay(1000);}
Reset(1000);


// Colores compuestos
// Purpura
analogWrite(Red,200);
analogWrite(Blue,120);
digitalWrite(Green, LOW);
delay(3000);
Reset(1000);
// Lila
analogWrite(Red,120);
analogWrite(Blue,200);
digitalWrite(Green, HIGH);
delay(3000);
Reset(1000);
// Naranja
analogWrite(Red,100);
analogWrite(Blue,0);
digitalWrite(Green, HIGH);
delay(3000);
Reset(1000);
}
