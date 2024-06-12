from machine import Pin
import time

led = Pin(2, Pin.OUT)
while True:
    print("hi")
    led.value(1)
    time.sleep_ms(500)
    led.value(0)
    time.sleep_ms(500)
