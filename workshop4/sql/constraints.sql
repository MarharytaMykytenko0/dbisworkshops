
alter table student_database
    add constraint student_check1 CHECK (LENGTH(login) >= 5);
alter table student_database
    add constraint student_check2 CHECK  (LENGTH(student_pass) >= 5);
alter table sudent_database
    add constraint sudent_unique UNIQUE  (sudent_mail, login);
alter table student_database
    add constraint student_check3 CHECK (status IN (0, 1));


alter table subjects
    add constraint subjects_fk foreign key (user_id) references student_database(id);
alter table subjects
    add constraint subjects_check CHECK (status IN (0, 1));


alter table work
    add constraint work_fk foreign key (user_id) references student_database(id);
alter table work
    add constraint work_check CHECK (status IN (0, 1));


alter table mark
    add constraint mark_check CHECK (status IN (0, 1));



