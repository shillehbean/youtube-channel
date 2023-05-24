from machine import Pin, I2C
import time
import ustruct
 
# Constants
ADXL345_ADDRESS = 0x53 # address for accelerometer 
ADXL345_POWER_CTL = 0x2D # address for power control
ADXL345_DATA_FORMAT = 0x31 # configure data format
ADXL345_DATAX0 = 0x32 # where the x-axis data starts
 
# Initialize I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
 
# Initialize ADXL345
def init_adxl345():
    i2c.writeto_mem(ADXL345_ADDRESS, ADXL345_POWER_CTL, bytearray([0x08]))  # Set bit 3 to 1 to enable measurement mode
    i2c.writeto_mem(ADXL345_ADDRESS, ADXL345_DATA_FORMAT, bytearray([0x0B]))  # Set data format to full resolution, +/- 16g
 
# Read acceleration data
def read_accel_data():
    data = i2c.readfrom_mem(ADXL345_ADDRESS, ADXL345_DATAX0, 6)
    x, y, z = ustruct.unpack('<3h', data)
    return x, y, z
 
# Main loop
init_adxl345()
while True:
    x, y, z = read_accel_data()
    print('--------------------')
    print(x, y, z)
    print("X: {}, Y: {}, Z: {}".format(x*0.0039, y*0.0039, z*0.0039))
    time.sleep(0.5)
    
    
# if you do get OSError: [Errno 5] EIO, try unplug and plug
# if you do set different resolution 0.0039 may not be the constant (check data sheet)
