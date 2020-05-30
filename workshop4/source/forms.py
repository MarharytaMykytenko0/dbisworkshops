from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateTimeField


class CreateUser(FlaskForm):
    student_name = StringField("student_name: ")
    student_mail = StringField("student_mail: ")
    student_group = StringField("student_group: ")
    login = StringField("login: ")
    student_pass = PasswordField("password: ")
    submit = SubmitField("OK")


class CreateSub(FlaskForm):
    user_id = IntegerField("user_id: ")
    sub_name = StringField("sub_name: ")
    submit = SubmitField("OK")


class CreateWork(FlaskForm):
    user_id = IntegerField("user_id: ")
    sub_name = StringField("sub_name: ")
    work_name = StringField("work_name")
    submit = SubmitField("OK")


class AddMark(FlaskForm):
    sub_name = StringField("sub_name: ")
    work_name = StringField("work_name")
    mark = IntegerField("mark: ")
    date_creating = DateTimeField("date: ")
    submit = SubmitField("OK")


