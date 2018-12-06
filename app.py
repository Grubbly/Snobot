import sumNums
import snobot_drive
from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return render_template('index.html', name='Snobot :D')

@app.route('/forward/<int:speed>')
def drive_forward(speed):
    snobot_drive.motor1_forward(speed)
    snobot_drive.motor2_forward(speed)
    return 'Driving forward at %d' % speed

@app.route('/backward/<int:speed>')
def drive_backward(speed):
    snobot_drive.motor1_backward(speed)
    snobot_drive.motor2_backward(speed)
    return 'Driving backward at %d' % speed

@app.route('/spinLeft/<int:speed>')
def spin_left(speed):
    snobot_drive.spin_left(speed)
    return 'Spinning left at %d' % speed

@app.route('/spinRight/<int:speed>')
def spin_right(speed):
    snobot_drive.spin_right(speed)
    return 'Spinning right at %d' % speed

@app.route('/quit')
def clean_quit():
    snobot_drive.quit()
    return 'GPIO Cleaned, robot off'

@app.route('/toggleMotor')
def toggle_motor():
    motor_state = snobot_drive.toggle_motor()
    return 'Motor %s' % motor_state 

@app.route('/turnTopServoCamera/<int:position')
def turn(position):
    snobot_drive.turnTopServoCamera(position)
    return 'Top Servo Camera moved to: %d' % position

if __name__ == '__main__':
    app.run(host='0.0.0.0')