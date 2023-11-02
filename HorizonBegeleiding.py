from gpiozero import LED
import time

print("Hello World") # Klassieker
'''
Sources:
https://projects.raspberrypi.org/en/projects/leds-buzzers-scratch-games/1
https://projects.raspberrypi.org/en/projects/physical-computing/3
https://projects.raspberrypi.org/en/projects/leds-buzzers-scratch-games/3

'''



from gpiozero import LED
led = LED(17)
led.on()
led.off()


led1 = LED(17)
led2 = LED(27)
led3 = LED(22)


led1.on()
led1.off()
led2.on()
led2.off()
led3.on()
led3.off()

while True:
    led1.on()
    time.sleep(1)
    led1.off()
    led2.on()
    time.sleep(1)
    led2.off()
    led3.on()
    time.sleep(1)
    led3.off()