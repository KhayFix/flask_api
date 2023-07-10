from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

courses = {
    1: {'info': 'some info', 'num': 56},
    2: {'info': 'some info', 'num': 5666}
}

parser = reqparse.RequestParser()
parser.add_argument('info', type=str)
parser.add_argument('num', type=int)


class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses.get(course_id)

    def delete(self, course_id):
        del courses[course_id]
        return courses

    def post(self, course_id):
        courses[course_id] = parser.parse_args()
        return courses

    def put(self, course_id):
        courses[course_id] = parser.parse_args()
        return courses


api.add_resource(Main, '/api/v2/main/<int:course_id>')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
