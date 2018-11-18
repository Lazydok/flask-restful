from flask_restful import reqparse, abort, Api, Resource
from app import APP, db
from app.models import ApplyAffiliation

api = Api(APP)


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('phone')
parser.add_argument('email')
parser.add_argument('content')


# Todo
# shows a single todo item and lets you delete a todo item
class Apply(Resource):

    def put(self):
        args = parser.parse_args()
        print(args)
        application = ApplyAffiliation(name=args.name, phone=args.phone, email=args.email, content=args.content)
        db.session.add(application)
        db.session.commit()
        return args, 201

    def get(self):
        return ApplyAffiliation.query.first()

##
## Actually setup the Api resource routing here
##
api.add_resource(Apply, '/apply')