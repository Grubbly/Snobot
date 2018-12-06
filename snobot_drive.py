import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
enable = 12
m1_input_pin1 = 7
m1_input_pin2 = 11
m2_input_pin1 = 29
m2_input_pin2 = 31
top_servo_pin = 15
bottom_servo_pin = 13

gpio.setup(enable, gpio.OUT)
gpio.setup(m1_input_pin1, gpio.OUT)
gpio.setup(m1_input_pin2, gpio.OUT)
gpio.setup(m2_input_pin1, gpio.OUT)
gpio.setup(m2_input_pin2, gpio.OUT)
gpio.setup(top_servo_pin, gpio.OUT)
gpio.setup(bottom_servo_pin, gpio.OUT)

gpio.output(enable, gpio.HIGH)
m1_forward_pwm = gpio.PWM(m1_input_pin1, 50)
m1_forward_pwm.start(0)
m1_backward_pwm = gpio.PWM(m1_input_pin2, 51)
m1_backward_pwm.start(0)
m2_forward_pwm = gpio.PWM(m2_input_pin1, 52)
m2_forward_pwm.start(0)
m2_backward_pwm = gpio.PWM(m2_input_pin2, 53)
m2_backward_pwm.start(0)
top_camera_servo = gpio.PWM(top_servo_pin, 54)
top_camera_servo.start(7.5)
bottom_camera_servo = gpio.PWM(bottom_servo_pin, 54)
bottom_camera_servo.start(7.5)

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

def spin_left(speed):
    motor2_forward(speed)
    motor1_backward(speed)

def spin_right(speed):
    motor2_backward(speed)
    motor1_forward(speed)

def turnTopServoCamera(position):
    top_camera_servo.ChangeDutyCycle(position)
    time.sleep(0.015)

def turnBottomServoCamera(position):
    bottom_camera_servo.ChangeDutyCycle(position)
    time.sleep(0.015)

# WHIP
def toggle_motor():
    power_toggle = not power_toggle
    gpio.output(enable, power_toggle)
    return str(power_toggle)

def quit():
    gpio.output(enable, gpio.LOW)
    gpio.cleanup()