import datetime
from sqlalchemy import create_engine, ForeignKey, Sequence, CheckConstraint
from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(
    oracle_connection_string.format(

        username="ADMIN",
        password="oracle",
        sid="XE",
        host="localhost",
        port="1521",
        database="WORKSHOP",

    )
    , echo=True
)

Base = declarative_base()


class student_database(Base):
    __tablename__ = 'student_database'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    student_name = Column(String(100), nullable=False)
    student_mail = Column(String(100), nullable=False, unique=True)
    student_group = Column(String(5), nullable=False)
    login = Column(String(100), CheckConstraint('LENGTH(login) >= 5'), nullable=False, unique=True)
    student_pass = Column(String(100), CheckConstraint('LENGTH(user_pass) >= 5'), nullable=False)
    status = Column(Boolean, nullable=False)

    def __init__(self, student_name, student_mail,
                 student_group, login, student_pass, status):
        """"""
        self.student_name = student_name
        self.student_mail = student_mail
        self.student_group = student_group
        self.login = login
        self.student_pass = student_pass
        self.status = status


class subject(Base):
    __tablename__ = 'subjects'

    user_id = Column(Integer, ForeignKey('student_database.id'), primary_key=True)
    sub_name = Column(String(50))
    status = Column(Boolean, nullable=False)

    def __init__(self, user_id, sub_name, status):
        """"""
        self.user_id = user_id
        self.sub_name = sub_name
        self.status = status

class work(Base):
    __tablename__ = 'work'

    user_id = Column(Integer, ForeignKey('student_database.id'), primary_key=True)
    sub_name = Column(String(50))
    work_name = Column(String(50))
    status = Column(Boolean, nullable=False)

    def __init__(self, user_id, sub_name, work_name, status):
        """"""
        self.user_id = user_id
        self.sub_name = sub_name
        self.work_name = work_name
        self.status = status

class mark(Base):
    __tablename__ = 'mark'

    user_id = Column(Integer, ForeignKey('student_database.id'), primary_key=True)
    sub_name = Column(String(50))
    work_name = Column(String(100))
    mark = Column(Integer, nullable=False)
    date_creating = Column(Date, nullable=False)
    status = Column(Boolean, nullable=False)

    def __init__(self, sub_name, work_name, mark, date_creating, status):
        """"""
        self.sub_name = sub_name
        self.work_name = work_name
        self.mark = mark
        self.date_creating = date_creating
        self.status = status


# create tables
Base.metadata.create_all(engine)