#include <Arduino.h>
#include <EasyUltrasonic.h>
#include <Wire.h>
#include <DHT.h>

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11

#define TRIG_PIN 5 // Pin for the ultrasonic sensor trigger
#define ECHO_PIN 6    // Pin for the ultrasonic sensor echo
#define ULTRASONIC_POWER_PIN 13 // Pin for powering one of the ultrasonic sensors, the other uses VCC

DHT dht(DHTPIN, DHTTYPE);
EasyUltrasonic ultrasonic;

void setup() {
  Serial.begin(9600);
  dht.begin();
  ultrasonic.attach(TRIG_PIN, ECHO_PIN);
  pinMode(ULTRASONIC_POWER_PIN, OUTPUT);
  digitalWrite(ULTRASONIC_POWER_PIN, HIGH); // Provide power to one of the ultrasonic sensors
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  float distanceCM = ultrasonic.getDistanceCM();

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C  Distance: "));
  Serial.print(distanceCM);
  Serial.println(" cm");

  delay(2000); 
}































































































































































































































