import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
"""
SPEED	            SPI.MAX_SPEED_HZ VALUE
125.0 MHz	        125000000
62.5 MHz	        62500000
31.2 MHz	        31200000
15.6 MHz	        15600000
7.8 MHz	                7800000
3.9 MHz	                3900000
1953 kHz	        1953000
976 kHz	                976000
488 kHz	                488000
244 kHz	                244000
122 kHz	                122000
61 kHz	                61000
30.5 kHz	        30500
15.2 kHz	        15200
7629 Hz	                7629
"""
spi.max_speed_hz = 61000 #3900000
spi.mode = 0b00 # [CPOL|CPHA]
spi.bits_per_word=8

# Split an integer input into a two byte array to send via SPI
def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])
"""
# Repeatedly switch a MCP4151 digital pot off then on
    while True:
    write_pot(0x1FF)
    time.sleep(0.5)
    write_pot(0x00)
    time.sleep(0.5)''''
"""
resp = spi.xfer2([10,11,12,13,14])
print (resp)
