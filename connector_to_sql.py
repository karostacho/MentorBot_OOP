import psycopg2
from tabulate import tabulate 

def connect_to_database():
    conn = psycopg2.connect(dbname="mentor_bot", user="postgres", password="mandarynka!")
    cursor = conn.cursor()
    return cursor

cursor = connect_to_database()


def get_student_by_unique_id(id):
    cursor.execute(f"SELECT * FROM class_data where id = '{id}'")
    

get_student_by_unique_id("P9!x")
rows = cursor.fetchall()
headers = [desc[0] for desc in cursor.description]
table = tabulate(rows, headers=headers)
print(table)