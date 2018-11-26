import RPi.GPIO as gpio
import time

# gpio.setmode(gpio.BOARD)
gpio.setmode(gpio.BCM)

input_pin1 = 4
input_pin2 = 17
# pwm_path = "/sys/class/rpi-pwm/pwm0/"

gpio.setup(input_pin1, gpio.OUT)
gpio.setup(input_pin2, gpio.OUT)

forward_pwm = gpio.PWM(input_pin1, 100)
forward_pwm.start(5)
time.sleep(1)

# def set_pwm(property, value):
#     try:
#         f = open(pwm_path + property, 'w')
#         f.write(value)
#         f.close()
#     except:
#         print("Error writing to: " + pwm_path + property + " value: " + value)
#
# set_pwm("delayed", "0")
# set_pwm("mode", "pwm");
# set_pwm("frequency", "500")
# set_pwm("active", "1")
#
# def forward():
#     gpio.output(input_pin1, True)
#     gpio.output(input_pin2, False)
#
# def backward():
#     gpio.output(input_pin1, False)
#     gpio.output(input_pin2, True)
#
# forward()
#
while True:
    command = raw_input("Enter f/r (forward/backward) followed by a number 0-9 (speed) to drive. E.g. f5 :")
    direction = command[0]
    speed = int(command[1]) * 11

    if direction == "f":
        print(speed)
        forward_pwm.ChangeDutyCycle(speed)
        time.sleep(0.5)
    else:
        backward()

    if speed in range(0,10):
        set_pwm("duty", str(speed))