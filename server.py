from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

SEQ = 0

APPLICATIONS = {
    1: {
        'name': '',
        'phone': '',
        'email': '',
        'content': '',
    },
}


def abort_if_todo_doesnt_exist(app_id):
    if app_id not in APPLICATIONS:
        abort(404, message="APPLICATIONS {} doesn't exist".format(app_id))

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('phone')
parser.add_argument('email')
parser.add_argument('content')


# Todo
# shows a single todo item and lets you delete a todo item
class Apply(Resource):
    # def get(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     return TODOS[todo_id]
    #
    # def delete(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     del TODOS[todo_id]
    #     return '', 204

    def put(self):
        args = parser.parse_args()
        global SEQ
        SEQ += 1
        print(args)
        args = {key: arg for key, arg in args.items()}
        APPLICATIONS[SEQ] = args
        print(APPLICATIONS)
        return args, 201

##
## Actually setup the Api resource routing here
##
api.add_resource(Apply, '/apply')

if __name__ == '__main__':
    app.run(debug=True)