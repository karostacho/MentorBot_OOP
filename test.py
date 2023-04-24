import psycopg2
import getpass
from tabulate import tabulate
from student_class import Student
from db_data import SqlData

def connect_to_database():
        password = getpass.getpass(prompt='Enter the database password: ')
        conn = psycopg2.connect(dbname="mentor_bot", user="postgres", password = password)
        cursor = conn.cursor()
        return cursor
    
def execute_sql_query(message):
    cursor = connect_to_database()
    cursor.execute(message)
    return cursor.fetchall()


def print_table(students_list):
        rows = []
        for student in students_list:
            rows.append([student.id, student.name, student.surname, student.year_of_birth, student.class_type, student.average_grade,student.average_presence])
        headers = ["id", "name", "surname", "year_of_birth", "class_type" ,"average_grade","average_presence"] 
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def create_list(tuples):
    students = []
    for row in tuples:
        id = row[0]
        name = row[1]
        surname = row[2]
        year_of_birth = row[3]
        class_type = row[4]
        average_grade = row[5]
        average_presence = row[6]

        student = Student(id,name, surname, year_of_birth, class_type ,average_grade,average_presence)
        students.append(student)
    print(students)


tuples = execute_sql_query(f"SELECT class_type ,count(id) FROM class_data group by class_type")

resultDictionary = dict((x, y) for x, y in tuples)
     
print (resultDictionary)



