import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
enable = 12
m1_input_pin1 = 7
m1_input_pin2 = 11
m2_input_pin1 = 29
m2_input_pin2 = 31

gpio.setup(enable, gpio.OUT)
gpio.setup(m1_input_pin1, gpio.OUT)
gpio.setup(m1_input_pin2, gpio.OUT)
gpio.setup(m2_input_pin1, gpio.OUT)
gpio.setup(m2_input_pin2, gpio.OUT)

gpio.output(enable, gpio.HIGH)
m1_forward_pwm = gpio.PWM(m1_input_pin1, 50)
m1_forward_pwm.start(0)
m1_backward_pwm = gpio.PWM(m1_input_pin2, 51)
m1_backward_pwm.start(0)
m2_forward_pwm = gpio.PWM(m2_input_pin1, 52)
m2_forward_pwm.start(0)
m2_backward_pwm = gpio.PWM(m2_input_pin2, 53)
m2_backward_pwm.start(0)

power_toggle = True

def motor1_forward(speed):
    m1_forward_pwm.ChangeDutyCycle(speed)
    m1_backward_pwm.ChangeDutyCycle(0)
    time.sleep(0.015)

def motor1_backward(speed):
    m1_forward_pwm.ChangeDutyCycle(0)
    m1_backward_pwm.ChangeDutyCycle(speed)
    time.sleep(0.015)

def motor2_forward(speed):
    m2_forward_pwm.ChangeDutyCycle(speed)
    m2_backward_pwm.ChangeDutyCycle(0)
    time.sleep(0.015)

def motor2_backward(speed):
    m2_forward_pwm.ChangeDutyCycle(0)
    m2_backward_pwm.ChangeDutyCycle(speed)
    time.sleep(0.015)

# WHIP
def toggle_motor():
    power_toggle = not power_toggle
    gpio.output(enable, power_toggle)
    return str(power_toggle)

def quit():
    gpio.output(enable, gpio.LOW)
    gpio.cleanup()