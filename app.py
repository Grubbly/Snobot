import sumNums
from drive import forward, backward
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, first, second):
        return {'data': sumNums.sumNums(first,second)}

class driveForward(Resource):
    def get(self, speed):
        return {'Motor Data': forward(speed)}

api.add_resource(sumNumbers, '/sumNums/<first>/<second>')
api.add_resource(driveForward, '/forward/<speed>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
