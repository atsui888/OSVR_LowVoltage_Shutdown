// Voltage_Listernernote
// listens to incoming voltage and sends data to Voltage_Actioner
// which sits on the Windows10 PC.
// Voltage_Listerner does not take any action, it just passes value to Voltage_Actioner

// if 50V voltage divider is used, then next line needs to be defined
#define VOLTAGE_DIVIDER_50V

float fVoltageSensor = 0;
float fVoltage = 0.0;

void setup()
{
  pinMode(A0, INPUT);
  Serial.begin(9600);
  delay(100);
}

void loop() {
  fVoltageSensor = analogRead(A0);

  #ifdef VOLTAGE_DIVIDER_50V
    fVoltage = (fVoltageSensor * 5)/1023 * 11;
  #else
    fVoltage = (fVoltageSensor * 5)/1023;
  #endif

  Serial.println(fVoltage);
  delay(2000);
}
