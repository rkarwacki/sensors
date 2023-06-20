import smbus2
import time
import Adafruit_DHT
from datetime import datetime

now = datetime.now()

# DHT readout
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
humidity, temperature_dht = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

# LPS331AP readout
bus = smbus2.SMBus(1)  # run smbus

bus.write_byte_data(0x5d, 0x20, 0b10000000)  # run sensor
bus.write_byte_data(0x5d, 0x21, 0b1)
Temp_LSB = bus.read_byte_data(0x5d, 0x2b)  # read temperature
Temp_MSB = bus.read_byte_data(0x5d, 0x2c)

count = (Temp_MSB << 8) + Temp_LSB  # write temp
if (count >= 0x8000): 		# oldest bit is the temp sign
    count1 = -((65535-count) + 1)
else:
    count1 = count

temperature_lps = 42.5 + (count1/480.0)  # recalculate temperature according to docs
ph = bus.read_byte_data(0x5d, 0x2a)  # read pressure
pl = bus.read_byte_data(0x5d, 0x29)
pxl = bus.read_byte_data(0x5d, 0x28)

# recalculate pressure according to docs
pressure = float((((ph << 8)+pl) << 8)+pxl)/4096
print(now.strftime("%d/%m/%Y %H:%M:%S")+"|{0:0.1f}|{1:0.1f}|{2:0.1f}|{3:0.1f}".format(temperature_dht, temperature_lps, humidity, pressure))
