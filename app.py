import sumNums
import snobot_drive
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# class sumNumbers(Resource):
#     def get(self, first, second):
#         return {'data': sumNums.sumNums(first,second)}

# class driveForward(Resource):
#    def get(self, speed):
#        snobot_drive.forward(speed)
#        return {'Motor Data': "5"}

# api.add_resource(sumNumbers, '/sumNums/<first>/<second>')
# api.add_resource(driveForward, '/forward/<speed>')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
