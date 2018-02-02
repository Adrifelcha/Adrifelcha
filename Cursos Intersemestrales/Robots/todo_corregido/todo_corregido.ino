// encender un led, mientras este encendido vamos a hacer una lectura y promediarla
//tomas lecturas, girar
//promediar lectura y va a esperar algo más grande
// todo analogwrite ay tiene la verdulilla
//analogwrtie se necsita pin de salida y valor

int s_i;
int s_d;
int acumulado_sd;
int acumulado_si;
int error;



void setup() 
{
  // put your setup code here, to run once:
  // Esta función DEPENDE DE  como conectaron el motor

//motor derecho
pinMode(2,OUTPUT);
pinMode(3,OUTPUT);

  //Motor izquierdo
pinMode(4,OUTPUT);
pinMode(5,OUTPUT);

Serial.begin(9600);
}

// delcaracion de función
void GirarDerecha (int time)
{ 
digitalWrite(2,LOW);
digitalWrite(3,HIGH);

digitalWrite(4,HIGH);
digitalWrite(5,LOW);

delay(time);

}

void GirarIzquierda (int time)

{
digitalWrite(2,HIGH);
digitalWrite(3,LOW);

digitalWrite(4,LOW);
digitalWrite(5,HIGH);

delay(time);
}

void AvanzarAdelante (int time)
{
  digitalWrite(2,HIGH);
digitalWrite(3,LOW);

digitalWrite(4,HIGH);
digitalWrite(5,LOW);

delay(time);
}

void AvanzarAtras (int time)

{
  digitalWrite(2,LOW);
digitalWrite(3,HIGH);

digitalWrite(4,LOW);
digitalWrite(5,HIGH);

delay(time);
}

void Stop (int time)
{
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);

  digitalWrite(4,LOW);
  digitalWrite(5,LOW);

  delay(time);
}

//acumulador

int calibracion_sd()
{
acumulado_sd = 0;
for(int i= 0; i< 51; i++)
{
  acumulado_sd = acumulado_sd + analogRead(A1);
  GirarDerecha(20);
  Stop(50);
}
acumulado_sd = acumulado_sd / 50;

analogWrite(10, 0);
return acumulado_sd;
}

int calibracion_si ()
{
acumulado_si = 0;
GirarIzquierda(20);
for(int i= 0; i< 51; i++)
{
  acumulado_si = acumulado_si + analogRead(A0);
  GirarIzquierda(20);
  Stop(50);
}
acumulado_si = acumulado_si / 50;

analogWrite(10, 0);
return acumulado_si;
}



void loop() {
  // put your main code here, to run repeatedly:
int currentCondition_sd = 0;
int currentCondition_si = 0;


analogWrite (11,200);
analogWrite (10,110);

analogWrite (9,100);
analogWrite (6,100);

currentCondition_sd = calibracion_sd ();
currentCondition_si = calibracion_si ();

Serial.print("Sensor 1: ");
Serial.print(currentCondition_sd);
Serial.print("--- Sensor 2: ");
Serial.println(currentCondition_si);
 GirarDerecha(50);
 


while(true)
  {
    s_i= analogRead (A0);
    s_d= analogRead (A1);

   Serial.print("Sensor 1: ");
Serial.print(s_d);
Serial.print("--- Sensor 2: ");
Serial.println(s_i);


    
if(s_i> (currentCondition_sd+30) || s_d > (currentCondition_si+30))
  {
    error= s_i - s_d;
    if(error>50)
    {
      GirarIzquierda (50);
    }
    else if(error < -50)
    {
      GirarDerecha(50);
    }
    else
    {
      AvanzarAdelante (50);
    }}
    else
    {
      Stop(100);
    }
    }
}

