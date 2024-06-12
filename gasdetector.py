from machine import Pin, ADC
from time import sleep

# Initialize pins
gaz = ADC(Pin(34))
gaz.atten(ADC.ATTN_11DB)

redled_pin = Pin(19, Pin.OUT)
buzzer_pin = Pin(18, Pin.OUT)

while True:
    gaz_value = gaz.read()  # Read analog value from MQ-4 sensor
    print('Gas Reading: %4.0f' %gaz_value)
    if gaz_value > 500:  # Check if gas concentration exceeds threshold
        # Deactivate LED and buzzer
        print("All OK! No Gas Detected")
        redled_pin.value(0)
        buzzer_pin.value(0)
    else:
        # Activate LED and buzzer
        print("Alert! Gas Detected")
        redled_pin.value(1)
        buzzer_pin.value(1)
    sleep(0.5)  # Delay before next reading