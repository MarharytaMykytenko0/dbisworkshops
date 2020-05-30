CREATE SEQUENCE dept_seq START WITH 1 INCREMENT BY 1;



CREATE OR REPLACE TRIGGER dept_id 
BEFORE INSERT or UPDATE ON student_database 
FOR EACH ROW
WHEN ( new.id IS NULL )
BEGIN
   :new.id := dept_seq.nextval;
END;



CREATE OR REPLACE TRIGGER student_trigg 
BEFORE INSERT or UPDATE ON student_database
FOR EACH ROW
BEGIN
    IF :new.student_name is NULL
    THEN
        raise_application_error(-20004,'student_name is NULL');
    END IF;

    IF :new.student_mail is NULL
    THEN
        raise_application_error(-20004,'student_mail is NULL');
    END IF;
    
    IF :new.student_mail NOT LIKE '%@%.%'
    THEN
        raise_application_error(-20001,'Student mail is not valid!');
    END IF;
    
    IF :new.student_grout is NULL
    THEN
        raise_application_error(-20004,'student_grout is NULL');
    END IF;
    
    IF :new.login is NULL
    THEN
        raise_application_error(-20004,'login is NULL');
    END IF;

    IF :new.student_pass is NULL
    THEN
        raise_application_error(-20004,'student_pass is NULL');
    END IF;
    
    IF LENGTH(:new.login) < 5
    THEN
        raise_application_error(-20004,'length of login < 5');
    END IF;
    
    IF LENGTH(:new.student_pass) < 5
    THEN
        raise_application_error(-20004,'length of passsword < 5');
    END IF;
END;



CREATE OR REPLACE TRIGGER sub_trigger 
BEFORE INSERT OR UPDATE ON subjects
FOR EACH ROW
DECLARE
BEGIN
    IF :new.sub_name is NULL
    THEN
        raise_application_error(-20004,'sub_name is NULL');
    END IF;
END;



CREATE OR REPLACE TRIGGER work_trigger 
BEFORE INSERT OR UPDATE ON work
FOR EACH ROW
DECLARE
BEGIN
    IF :new.sub_name is NULL
    THEN
        raise_application_error(-20004,'sub_name is NULL');
    END IF;

    IF :new.work_name is NULL
    THEN
        raise_application_error(-20004,'work_name is NULL');
    END IF;
END;



CREATE OR REPLACE TRIGGER time_trigger 
BEFORE INSERT OR UPDATE ON mark
FOR EACH ROW
DECLARE
BEGIN
    IF :new.sub_name is NULL
    THEN
        raise_application_error(-20004,'sub_name is NULL');
    END IF;

    IF :new.work_name is NULL
    THEN
        raise_application_error(-20004,'work_name is NULL');
    END IF;

    IF :new.mark is NULL
    THEN
        raise_application_error(-20004,'mark is NULL');
    END IF;
    
    if :NEW.date_creating < SYSDATE
    THEN
        raise_application_error(-20004,'error with date');
    END IF;
END;