import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
enable = 12
input_pin1 = 7
input_pin2 = 11

gpio.setup(enable, gpio.OUT)
gpio.setup(input_pin1, gpio.OUT)
gpio.setup(input_pin2, gpio.OUT)

gpio.output(enable, gpio.HIGH)
forward_pwm = gpio.PWM(input_pin1, 50)
forward_pwm.start(0)
backward_pwm = gpio.PWM(input_pin2, 50)
backward_pwm.start(0)

power_toggle = True

def forward():
    print("Forward " + speed)
    forward_pwm.ChangeDutyCycle(speed)

def backward():
    print("backward " + speed)
    backward_pwm.ChangeDutyCycle(speed)

while True:
    command = input("Enter f/r (forward/backward) followed by a number 0-9 (speed) to drive. E.g. f5 :")
    direction = command[0]
    speed = int(command[1]) * 11

    if direction == "f":
        forward()    
    else if direction == "q":
        gpio.output(enable, gpio.LOW)
        gpio.cleanup()
    else if direction == " ":
        power_toggle = !power_toggle
        gpio.output(enable, power_toggle)
    else:
        backward()

    if speed in range(0,10):
        set_pwm("duty", str(speed))
