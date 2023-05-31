#include "dht.h"

const int sensorTempUmi = A1;
const int sensorGasAnalog = A0;
const int sensorGasDigi = 7;

dht DHT;

void setup() {
  Serial.begin(9600);
}

void loop() {
  gas();
  temp_umi();
  Serial.println("----------------------");
  delay(2000);
}

void gas() {
  Serial.print("Valor Gas: ");
  Serial.println(analogRead(sensorGasAnalog));
  Serial.print("Valor Gas: ");
  Serial.println(digitalRead(sensorGasDigi));
}

void temp_umi() {
  DHT.read11(sensorTempUmi);
  Serial.print("Umidade: ");
  Serial.println(DHT.humidity);
  Serial.print("Temperatura: ");
  Serial.println(DHT.temperature, 0);
}