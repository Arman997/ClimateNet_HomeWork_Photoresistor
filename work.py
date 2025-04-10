from gpiozero import PWMLED, MCP3008
from time import sleep

pod = MCP3008(0)
led = PWMLED(17)

while True:
    if(pod.value < 0):
        led.value = 0

    else:
        led.value = pod.value 

    print(pod.value)
    sleep(0.1)
