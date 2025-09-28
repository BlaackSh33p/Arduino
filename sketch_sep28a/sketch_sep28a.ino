// Blink LED on ESP32 pin 2

#define LED_PIN 2   // GPIO 2

void setup() {
  pinMode(LED_PIN, OUTPUT); // Set pin 2 as output
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // Turn LED on
  delay(1000);                 // Wait 1 second
  digitalWrite(LED_PIN, LOW);  // Turn LED off
  delay(1000);                 // Wait 1 second
}
