
void setup() 
{
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(A0);
  float Voltage = sensorValue * (5.0 / 1023.0);
  
  if (Voltage > 1)
  {
    Serial.println(Voltage);
  }
  else
  {
    Serial.println('Z');
  }
}
