#include "dht.h"

const int sensorTempUmi = A1;
const int sensorGasAnalog = A0;
const int sensorGasDigi = 7;
int vetor[4];
dht DHT;

void setup() {
    Serial.begin(9600);
}

void loop() {
    gas();
    temp_umi();
    Serial.print(vetor[0]);
    Serial.print(",");
    Serial.print(vetor[1]);
    Serial.print(",");
    Serial.print(vetor[2]);
    Serial.print(",");
    Serial.println(vetor[3]);
    delay(2000);
}

void gas() {
    vetor[0] = analogRead(sensorGasAnalog)/8.3;
    vetor[1] = digitalRead(sensorGasDigi);
}

void temp_umi() {
    DHT.read11(sensorTempUmi);
    vetor[2] = DHT.humidity;
    vetor[3] = DHT.temperature;
}