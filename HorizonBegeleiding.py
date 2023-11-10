'''
Sources:
https://projects.raspberrypi.org/en/projects/leds-buzzers-scratch-games/1
https://projects.raspberrypi.org/en/projects/physical-computing/3
https://projects.raspberrypi.org/en/projects/leds-buzzers-scratch-games/3
https://gpiozero.readthedocs.io/en/latest/recipes.html#led
'''

from gpiozero import LED
import time

print("Hello World") # Klassieker


red = LED(17)
yellow = LED(27)
green = LED(22)


red.on()
red.off()
yellow.on()
yellow.off()
green.on()
green.off()

# while True:
for i in range(10):
    red.on()
    time.sleep(1)
    red.off()
    yellow.on()
    time.sleep(1)
    yellow.off()
    green.on()
    time.sleep(1)
    green.off()

from gpiozero import PWMLED
from time import sleep


red = PWMLED(17)
yellow = PWMLED(27)
green = PWMLED(22)

# while True:
for i in range(10):
    red.pulse()
    time.sleep(3)
    red.off()
    yellow.pulse()
    time.sleep(3)
    yellow.off()
    green.pulse()
    time.sleep(3)
    green.off()


from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(17, 27, 22)

lights.green.on()
sleep(3)
lights.green.off()
while True:
    lights.red.on()
    sleep(10)
    lights.red.off()
    lights.green.on()
    sleep(10)
    lights.green.off()
    lights.amber.on()
    sleep(3)
    lights.amber.off()