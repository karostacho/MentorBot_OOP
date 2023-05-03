from connector import Connector
from data_source import DataSource
from student import Student

class SqlData(DataSource):
    def __init__(self):
        self.connector = Connector()

    def map_to_student_list(self, db_data):
        student_list = Student.create_student_list(db_data)
        return student_list

    def get_student_by_unique_id(self, student_id):
        db_data = self.connector.execute_sql_query(f"SELECT * FROM class_data where id = '{student_id}'")
        student_list = self.map_to_student_list(db_data)
        return student_list

    def get_all_students_from_given_class(self, class_type):
        db_data = self.connector.execute_sql_query(f"SELECT * FROM class_data where class_type = '{class_type}'")
        student_list = self.map_to_student_list(db_data)
        return student_list

    def get_youngest_student_from_all_classes(self):
        db_data = self.connector.execute_sql_query(f"SELECT * FROM class_data order by year_of_birth desc limit 1")
        student_list = self.map_to_student_list(db_data)
        return student_list
    
    def get_oldest_student_from_all_classes(self):
        db_data = self.connector.execute_sql_query(f"SELECT * FROM class_data order by year_of_birth limit 1")
        student_list = self.map_to_student_list(db_data)
        return student_list
    
    def calculate_average_grade_of_all_students(self):
        db_data = self.connector.execute_sql_query(f"SELECT round(avg(average_grade),2) as average_grade FROM class_data")
        average_grade = db_data[0][0]
        return average_grade

    def return_rounded_average_presence_of_all_students(self):
        db_data = self.connector.execute_sql_query(f"SELECT round(avg(average_presence),2) as average_presence FROM class_data") 
        average_presence = db_data[0][0]
        return average_presence

    def get_sorted_student_list_by_average_grade(self):
        db_data = self.connector.execute_sql_query(f"SELECT * FROM class_data order by average_grade") 
        student_list = self.map_to_student_list(db_data)
        return student_list

    def get_number_of_students_in_each_class(self):
        db_data = self.connector.execute_sql_query(f"SELECT class_type ,count(id) FROM class_data group by class_type") 
        number_of_students_by_class = dict((class_type, number_of_students) for class_type, number_of_students in db_data)
        return number_of_students_by_class

    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        db_data = self.connector.execute_sql_query(f"SELECT * FROM class_data order by year_of_birth, surname") 
        student_list = self.map_to_student_list(db_data)
        return student_list
