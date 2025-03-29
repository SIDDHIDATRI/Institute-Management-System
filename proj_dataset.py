import mysql.connector
mypro=mysql.connector.connect(host='localhost',user='root',password='admin',database='db1')
cur=mypro.cursor()
print(mypro)
print("Connection established.")

#CREATING STUDENT TABLE IN SQL

Stu_tab = "CREATE TABLE student(stu_id int,name varchar(40),mobile varchar(15),password varchar(50),course_name varchar(20))"
cur.execute(Stu_tab)
print("Student's table created")

#CREATING FACULTY TABLE IN SQL

Fac_tab= "CREATE TABLE faculty(fac_id int, name varchar(50),mobile varchar(15),password varchar(50))"
cur.execute(Fac_tab)
print("Faculty's table created")

# CREATING COURSE TABLE IN SQL

Cour_tab="CREATE TABLE course(course_id int,course_name varchar(15) UNIQUE,fac_id int)"
cur.execute(Cour_tab)
print("Course table is created")

#CREATING GRADE TABLE IN SQL

Grd_tab="CREATE TABLE grade(stu_id int,grade varchar(15))"
cur.execute(Grd_tab)
print("Grade table is created")

Stu_tab= "ALTER TABLE student ADD FOREIGN KEY(course_name) REFERENCES course(course_name)"
cur.execute(Stu_tab)
Stu_tab= "CREATE INDEX stu_id ON student(stu_id)"
cur.execute(Stu_tab)
Fac_tab="ALTER TABLE faculty ADD COLUMN course_name VARCHAR(50) UNIQUE"
cur.execute(Fac_tab)
Fac_tab="CREATE INDEX fac_id ON faculty(fac_id)"
cur.execute(Fac_tab)
Cour_tab=" ALTER TABLE course ADD FOREIGN KEY(fac_id) REFERENCES faculty(fac_id)"
cur.execute(Cour_tab)
Grd_tab="ALTER TABLE grade ADD FOREIGN KEY (stu_id) REFERENCES student(stu_id)"
cur.execute(Grd_tab)