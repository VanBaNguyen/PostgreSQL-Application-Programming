# PostgreSQL-Application-Programming-COMP3005A-Assignment3

## Student Info

Name: Van Nguyen

StudentID: 101331941

## Demo Link

```bash
https://drive.google.com/file/d/1CPESoOFj_oyhiVk5tanRK-_1Nhhr_9z_/view?usp=sharing

In the video, I accidentally misread Jim Beam's name and said Josh, sorry about that!
```

## Install

```bash
#clone repo
git clone https://github.com/VanBaNguyen/PostgreSQL-Application-Programming.git

# make venv
python3 -m venv venv

# might be different on windows, works on MacOS
source venv/bin/activate

#install dependency
pip install psycopg2

#connect to pgadmin and alter credentials in main guard
#(add server button and copy over the credentials/ports or make new ones)

#run main.py
python3 main.py

#python code should alter the tables (shown in video)
```

## Functions

- `make_schema(connection, sql_path)` - Sets up database tables from SQL file
- `getAllStudents(connection)` - Fetches and displays all student records
- `addStudent(connection, first_name, last_name, email, enrollment_date)` - Adds a new student
- `updateStudentEmail(connection, student_id, new_email)` - Updates a student's email
- `deleteStudent(connection, student_id)` - Removes a student by ID

## Database Schema

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    enrollment_date DATE
);
```
