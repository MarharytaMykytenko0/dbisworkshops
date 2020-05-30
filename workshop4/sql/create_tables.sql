create table student_database(
    id INTEGER NOT NULL,
    student_name VARCHAR2(100) NOT NULL,
    student_mail VARCHAR2(100) NOT NULL,
    student_group VARCHAR2(5) NOT NULL,
    login VARCHAR2(100) NOT NULL,
    student_pass VARCHAR2(100) NOT NULL,
  constraint student_pk primary key (id)
);

create table subjects(
    student_id INTEGER NOT NULL,
    sub_name VARCHAR2(100) NOT NULL,
    CONSTRAINT sub_pk PRIMARY KEY (student_id, sub_name)
);

create table work(
    student_id INTEGER NOT NULL,
    sub_name VARCHAR2(100) NOT NULL,
    work_name VARCHAR2(100) NOT NULL,
    CONSTRAINT  work_pk PRIMARY KEY (student_id, work_name)
);

create table mark(
    student_id INTEGER NOT null,
    sub_name VARCHAR2(100) NOT NULL,
    work_name VARCHAR2(100) NOT NULL,
    mark INTEGER NOT NULL,
    date_creating DATE not null,
    CONSTRAINT student_pk PRIMARY KEY (student_id)
);