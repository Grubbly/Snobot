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
backward_pwm = gpio.PWM(input_pin2, 100)
backward_pwm.start(0)

power_toggle = True

def forward(speed):
    print("Forward " + str(speed))
    forward_pwm.ChangeDutyCycle(speed)
    backward_pwm.ChangeDutyCycle(0)
    time.sleep(0.015)

def backward(speed):
    print("backward " + str(speed))
    forward_pwm.ChangeDutyCycle(0)
    backward_pwm.ChangeDutyCycle(speed)
    time.sleep(0.015)