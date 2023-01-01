from machine import ADC, Pin
import utime
    
    
def get_capacitator_measurements():
    soil_adc = ADC(Pin(26)) # pin for analog values
    while True:
        print("ADC Value is -----> %d" % soil_adc.read_u16())
        utime.sleep(0.5)
        
get_capacitator_measurements()
