import sumNums
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, first, second):
        return {'data': sumNums.sumNums(first,second)}

api.add_resource(sumNumbers, '/sumNums/<first>/<second>')

if __name__ == '__main__':
    app.run()
