import sumNums
import snobot_drive
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/forward/<speed>')
    def drive_forward():
        snobot_drive.forward(speed)
        return 'Driving forward at ' + speed + '%'

if __name__ == '__main__':
    app.run(host='0.0.0.0')