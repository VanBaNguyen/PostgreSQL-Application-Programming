import psycopg2

#connect/run schema from file
def make_schema(connection, sql_path="schema.sql"):
    try:
        # read schema.sql
        with open(sql_path, "r", encoding="utf-8") as f:
            sql_text = f.read()
    except Exception as e:
        print(f"Could not read '{sql_path}': {e}")
        return

    try:
        # run it the content
        with connection, connection.cursor() as cursor:
            cursor.execute(sql_text)
        print("Schema applied.")
    except Exception as e:
        print(f"Failed to apply schema: {e}")
        try:
            connection.rollback()
        except Exception:
            pass

#read all rows
def getAllStudents(connection):
    try:
        # Fetch all students from the database
        with connection, connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students;")
            students = cursor.fetchall()
            # print each student
            for student in students:
                print(student)
            return students
    except Exception as e:
        print(f"Failed to fetch students: {e}")
        try:
            connection.rollback()
        except Exception:
            pass
        return []

#insert one row
def addStudent(connection, first_name, last_name, email, enrollment_date):
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s);
            """, (first_name, last_name, email, enrollment_date))
        print("Student added successfully.\n")
    except Exception as e:
        print(f"[DB ERROR] Failed to add student: {e}")
        try:
            connection.rollback()
        except Exception:
            pass

#update email by id
def updateStudentEmail(connection, student_id, new_email):
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute("""
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
            """, (new_email, student_id))
        print("Student email updated successfully.\n")
    except Exception as e:
        print(f"[DB ERROR] Failed to update student email: {e}")
        try:
            connection.rollback()
        except Exception:
            pass

#delete by id
def deleteStudent(connection, student_id):
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM students
                WHERE student_id = %s;
            """, (student_id,))
        print("Student deleted successfully.\n")
    except Exception as e:
        print(f"[DB ERROR] Failed to delete student: {e}")
        # rollback on error
        try:
            connection.rollback()
        except Exception:
            pass

if __name__=="__main__":
    conn=None
    try:
        #open connection
        conn=psycopg2.connect(
            dbname="postgres",
            user="van",
            password="admin",
            host="localhost",
            port="5432"
        )
        print("Connected to PostgreSQL.")

        #drop table if exists
        try:
            with conn, conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS students;")
            print("Dropped existing 'students' table (if any).")
        except Exception as e:
            print(f"Failed to drop table: {e}")
            try:
                conn.rollback()
            except Exception:
                pass

        make_schema(conn)
        # getAllStudents(conn)

        students=getAllStudents(conn)
        addStudent(conn,'Sidiq','Akhmad','sidiq.akhmad@sudan.com','1967-03-01')
        # getAllStudents(conn)

        updateStudentEmail(conn,4,'sidiq.akhmad@newdomain.com')
        # getAllStudents(conn)

        deleteStudent(conn,3)
        getAllStudents(conn)

    except Exception as e:
        #fatal catchpip 
        print(f"{e}")
    finally:
        #close connection
        if conn is not None:
            try:
                conn.close()
                print("Connection closed.")
            except Exception as e:
                print(f"There was a close error: {e}")
