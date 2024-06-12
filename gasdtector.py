from machine import Pin, ADC
from time import sleep
# ESP32 Pin assignment

gaz = ADC(Pin(34)) # GPIO pin connected to the MQ-4 sensor
gaz.atten(ADC.ATTN_11DB)       

while True:
  gaz_value = gaz.read()
  print('Gas Reading: %4.0f' %gaz_value)

  if (gaz_value<500): 
    print("Alert! Gas Detected")
  else:
    print("All OK! No Gas Detected")
  sleep(1)