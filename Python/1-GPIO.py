#to excute we must use sudo pyhon3 ---.py
import Rpi.GPIO as GPIO
# use board numbering (1,2,3,--)
# mainly use it as other can diffe from one module to another
GPIO.setmode(GPIO.BOARD)
# use SoC numbering (GPIO1,GPIO2,GPIO3,--)
GPIO.setmode(GPIO.BCM)
# sets direction GPIO.setup(pin_number,direction)
# GPIO.OUT-->output ,GPIO.IN-->input
GPIO.setup(13,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
# assign output value GPIO.output(pin_number,value)
# True-->1"3.3v" ,False-->0"0v"
GPIO.output(13,True)
GPIO.output(13,False)
# read input pins GPIO.input(pin_number)
# returns True or False
value = GPIO.input(13)
