import psycopg2
from tabulate import tabulate 

class Connector():
    def __init__(self):
        self.cursor = self.connect_to_database()


    def connect_to_database(self):
        conn = psycopg2.connect(dbname="mentor_bot", user="postgres", password="mandarynka!")
        cursor = conn.cursor()
        return cursor
    
    def execute_sql_query(self, message):
        self.cursor.execute(message)

    def print_students_table_from_db(self):
        rows = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        table = tabulate(rows, headers=headers)
        print(table)

