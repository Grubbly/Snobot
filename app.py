import sumNums
import snobot_drive
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/forward/<int:speed>')
def drive_forward(speed):
    snobot_drive.forward(speed)
    return 'Driving forward at %d' % speed

@app.route('/backward/<int:speed>')
def drive_backward(speed):
    snobot_drive.backward(speed)
    return 'Driving backward at %d' % speed

@app.route('/quit')
def clean_quit():
    snobot_drive.quit()
    return 'GPIO Cleaned, robot off'

@app.route('/toggleMotor')
def toggle_motor():
    motor_state = snobot_drive.toggle_motor()
    return 'Motor %s' % motor_state 

if __name__ == '__main__':
    app.run(host='0.0.0.0')