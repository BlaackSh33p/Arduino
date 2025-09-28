from machine import Pin
import time

led = Pin(2, Pin.OUT)  # GPIO2 is usually onboard LED

while True:
    print("uname:", os.uname())
    led.value(not led.value())
    time.sleep(0.1)
