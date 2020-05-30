from flask import Flask
from flask import request
from flask import render_template

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup import student_database, subject, work, mark
import sqlalchemy

from forms import CreateUser, CreateSub, CreateWork, AddMark

app = Flask(__name__)
app.config['SECRET_KEY'] = 'project'


@app.route("/", methods=['GET'])
def hello():
    return (
        {
            "uri": "/",
            "sub_uri": {
                "student create": "/student",
                "create subject": "/subject",
                "create work": "/work",
                "create mark": "/mark",

            }
        }
    )


@app.route('/student', methods=["GET", "POST"])
def create_sudent():
    form = CreateUser()
    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

            engine = create_engine(oracle_connection_string.format(

                username="ADMIN",
                password="oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="WORKSHOP"),
                echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = student_database(result['student_name'], result['student_mail'],
                                    result['student_group'], result['login'],
                                    result['student_pass'])
            session.add(adddata)
            session.commit()
            return render_template('ConfirmOK.html', result=result)

        except:
            result = request.form
            return render_template('ConfirmNotOK.html', result=result)

    return render_template('createStudent.html', form=form)


@app.route('/subject', methods=["GET", "POST"])
def create_sub():
    form = CreateSub()
    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
            engine = create_engine(oracle_connection_string.format(

                username="ADMIN",
                password="oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="WORKSHOP"),
                echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = subject(result['user_id'], result['sub_name'])
            session.add(adddata)
            session.commit()
            return render_template('ConfirmOK.html', result=result)

        except:
            result = request.form
            return render_template('ConfirmNotOK.html', result=result)

    return render_template('createSubject.html', form=form)


@app.route('/work', methods=["GET", "POST"])
def create_work():
    form = CreateWork()
    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
            engine = create_engine(oracle_connection_string.format(

                username="ADMIN",
                password="oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="WORKSHOP"),
                echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = work(result['user_id'], result['sub_name'],
                           result['work_name'])
            session.add(adddata)
            session.commit()
            return render_template('ConfirmOK.html', result=result)

        except:
            result = request.form
            return render_template('ConfirmNotOK.html', result=result)

    return render_template('createWork.html', form=form)


@app.route('/mark', methods=["GET", "POST"])
def add_mark():
    form = AddMark()
    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
            engine = create_engine(oracle_connection_string.format(

                username="ADMIN",
                password="oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="WORKSHOP"),
                echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = work(result['user_id'], result['sub_name'],
                           result['work_name'],result['mark'])
            session.add(adddata)
            session.commit()
            return render_template('ConfirmOK.html', result=result)

        except:
            result = request.form
            return render_template('ConfirmNotOK.html', result=result)

    return render_template('addMark.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)