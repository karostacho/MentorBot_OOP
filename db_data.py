from connector_to_sql import Connector
from data_source import DataSource
from display import Displayer

class SqlData(DataSource):
    def __init__(self):
        self.connector = Connector()
        self.displayer = Displayer()

    def get_student_by_unique_id(self):
        student_id = self.displayer.ask_for_student_id()
        self.connector.execute_sql_query(f"SELECT * FROM class_data where id = '{student_id}'")
        self.connector.print_students_table_from_db()

    def get_all_students_from_given_class(self):
        class_type = self.displayer.ask_for_class_type()
        if class_type not in ["A", "a", "B", "b"]:
            self.displayer.inform_about_invalid("class type")
            self.get_all_students_from_given_class()
        else:
            self.connector.execute_sql_query(f"SELECT * FROM class_data where class_type = '{class_type}'")
            self.connector.print_students_table_from_db()

    def get_youngest_student_from_all_classes(self):
        self.connector.execute_sql_query(f"SELECT * FROM class_data order by year_of_birth desc limit 1")
        self.connector.print_students_table_from_db()
    
    def get_oldest_student_from_all_classes(self):
        self.connector.execute_sql_query(f"SELECT * FROM class_data order by year_of_birth limit 1")
        self.connector.print_students_table_from_db()
    
    def calculate_average_grade_of_all_students(self):
        self.connector.execute_sql_query(f"SELECT round(avg(average_grade),2) as average_grade FROM class_data")
        self.connector.print_students_table_from_db()

    def return_rounded_average_presence_of_all_students(self):
        self.connector.execute_sql_query(f"SELECT round(avg(average_presence),2) as average_presence FROM class_data") 
        self.connector.print_students_table_from_db()

    def get_sorted_student_list_by_average_grade(self):
        self.connector.execute_sql_query(f"SELECT * FROM class_data order by average_grade") 
        self.connector.print_students_table_from_db()

    def get_number_of_students_in_each_class(self):
        self.connector.execute_sql_query(f"SELECT class_type ,count(id) FROM class_data group by class_type") 
        self.connector.print_students_table_from_db()

    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        self.connector.execute_sql_query(f"SELECT * FROM class_data order by year_of_birth, surname") 
        self.connector.print_students_table_from_db()

