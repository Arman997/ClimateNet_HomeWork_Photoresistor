import RPi.GPIO as GPIO
import time
sclk = 11
miso = 9
mosi = 10
ce0 = 8

GPIO.setmode(GPIO.BCM)

GPIO.setup(miso, GPIO.IN)
GPIO.setup(mosi, GPIO.IN)

while True:
    time.sleep(0.1)
    print("miso: ",miso)
    print("mosi: ", mosi)
    print("sclk: ", sclk)
    print("ce0: ", ce0)
