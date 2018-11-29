import RPi.GPIO as gpio
import time

try {
    gpio.cleanup()
    print("GPIO Cleaned")
} except {
    print("GPIO Started Clean")
}

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

try:
    while True:
        command = input("Enter f/r (forward/backward) followed by a number 0-9 (speed) to drive. E.g. f5 :")
        direction = command[0]
        if len(command) == 2 and direction != "q" and direction != " ":
            print("speed set")
            speed = int(command[1]) * 11
        else:
            print("Invalid command length for speed, speed not set")

        if direction == "f":
            forward(speed)
        elif direction == "q":
            gpio.output(enable, gpio.LOW)
            gpio.cleanup()
            print("BYE")
            break
        elif direction == " ":
            power_toggle = not power_toggle
            gpio.output(enable, power_toggle)
            if(power_toggle):
                print("Motor on")
            else:
                print("Motor off")
        else:
            backward(speed)
except:
    gpio.output(enable, gpio.LOW)
    gpio.cleanup()
    print("BYE")
