from datetime import datetime

from flask import Blueprint, redirect, url_for, request
from flask_restful import Api, Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound

from coreapp.db import db
from coreapp.restful_api.parser_oracle_db.parser_db import parser

blueprint = Blueprint('service', __name__, template_folder='templates', )
api = Api()

courses = {
    1: {'info': 'some info', 'num': 56},
    2: {'info': 'some info', 'num': 5666}
}


class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses.get(course_id)


api.add_resource(Main, '/api/v2/main/<int:course_id>')
api.init_app(blueprint)

# @blueprint.route('/')
# def service_apache():
#     """
#     service_running возвращает такие значение 0, 3, 4, False.
#
#     0 - сервис работает.
#     3 - сервис не работает
#     4 - сервис не найден в системе.
#     False - ошибка.
#     """
#     # title = "apache2"
#     # form = ServiceAppForm()
#     # checkbox = CheckboxState.query.filter_by(id=1).first()  # Получаем состояние чекбокса из базы данных.
#     # # В базе данных храниться последнее состояние чекбокса.
#     # output = service_app.running(command='status', name_app=title)
#
#     return render_template('service_app/management_apache.html', title=title,
#                            service_state=output, form=form, chk=checkbox)
