import psycopg2
import getpass
from tabulate import tabulate 

class Connector():
    def __init__(self):
        self.cursor = self.connect_to_database()
    
    def connect_to_database(self):
        password = getpass.getpass(prompt='Enter the database password: ')
        conn = psycopg2.connect(dbname="mentor_bot", user="postgres", password = password)
        cursor = conn.cursor()
        return cursor
    
    def execute_sql_query(self, message):
        self.cursor.execute(message)

    def get_rows_from_db(self):
        rows = self.cursor.fetchall()
        return rows
    
    def get_headers_from_db(self):
        headers = [desc[0] for desc in self.cursor.description]
        return headers

    def print_students_table_from_db(self):
        rows = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        table = tabulate(rows, headers=headers, tablefmt= "fancy_grid")
        print(table)

    def get_list_of_ids(self):
        self.cursor.execute(f"SELECT id FROM class_data")
        t_list = self.cursor.fetchall()
        list_of_ids = [item for tuple in t_list for item in tuple]
        return list_of_ids
