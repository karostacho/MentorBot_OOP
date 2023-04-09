from connector_to_sql import connect_to_database
from tabulate import tabulate

cursor = connect_to_database()
cursor.execute("SELECT * FROM class_data where class_type = 'B'")
rows = cursor.fetchall()

from data_source import DataSource
from display import Displayer

class SqlData(DataSource):
    def __init__(self):
        self.cursor = connect_to_database()
        self.displayer = Displayer()
        
    def get_student_by_unique_id(self, id):
        cursor.execute(f"SELECT * FROM class_data where id = '{id}'")

    def get_all_students_from_given_class(self, class_type):
        cursor.execute(f"SELECT * FROM class_data where class_type = '{class_type}'")
        
    def get_youngest_student_from_all_classes(self):
        cursor.execute(f"SELECT * FROM class_data order by year_of_birth")
        cursor.fetchone()
    
    def get_oldest_student_from_all_classes(self):
        cursor.execute(f"SELECT * FROM class_data order by year_of_birth desc")
        cursor.fetchone()
    
    def calculate_average_grade_of_all_students(self):
        cursor.execute(f"select round(avg(average_grade),2)")
    
    def return_rounded_average_presence_of_all_students(self):
        cursor.execute(f"select round(avg(average_presence),2)") 
    
    def get_sorted_student_list_by_average_grade(self):
        cursor.execute(f"SELECT * FROM class_data order by average_grade") 

    def get_number_of_students_in_each_class(self):
        cursor.execute(f"select class_type ,count(id) from class_data group by class_type") 
        
    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        cursor.execute(f"SELECT * FROM class_data order by year_of_birth, surname") 


