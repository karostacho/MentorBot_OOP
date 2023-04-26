import psycopg2
import getpass

class Connector():
    def __init__(self):
        self.cursor = self.connect_to_database()
    
    def connect_to_database(self):
        try:
            password = getpass.getpass(prompt='Enter the database password: ')
            conn = psycopg2.connect(dbname="mentor_bot", user="postgres", password = password)
            cursor = conn.cursor()
            return cursor
        except psycopg2.OperationalError:
            print("Wrong password")
            return self.connect_to_database()

    
    def execute_sql_query(self, message):
        try:
            self.cursor.execute(message)
            return self.cursor.fetchall()
        except psycopg2.errors.UndefinedColumn as error:
            print(error)
            quit()
    