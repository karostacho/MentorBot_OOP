import collections
import csv
from statistics import mean
from student_class import Student
from data_source import DataSource

class CsvFile(DataSource):
    def __init__(self):
        self.students = self.get_data_from_csv()

    def get_data_from_csv(self):
        try:     
            with open ("class_data.csv") as file:
                class_data = csv.reader(file)
                student_list = Student.create_student_list(class_data)
                return student_list
        except Exception as exception:
            print (exception)
            quit()

    def get_student_by_unique_id(self, student_id):
        students_list = []
        for student in self.students:
            if student.id == student_id:
                students_list.append(student)
        return students_list

    def get_all_students_from_given_class(self, class_type):
        students_list = []
        for student in self.students:
            if student.class_type == class_type:
                students_list.append(student)
        return students_list
        
    def get_youngest_student_from_all_classes(self):
        list_of_years = [student.year_of_birth for student in self.students]
        year_of_younger_student = (max(list_of_years))
        students_list = []
        for student in self.students:
            if student.year_of_birth == year_of_younger_student:
                students_list.append(student)
        return students_list
    
    def get_oldest_student_from_all_classes(self):
        list_of_years = [student.year_of_birth for student in self.students]
        year_of_younger_student = (min(list_of_years))
        students_list = []
        for student in self.students:
            if student.year_of_birth == year_of_younger_student:
                students_list.append(student)
        return students_list
    
    def calculate_average_grade_of_all_students(self):
        list_of_grades = [student.average_grade for student in self.students]
        average_grade = mean(list_of_grades)
        return average_grade
        
    def return_rounded_average_presence_of_all_students(self):
        list_of_presence = [student.average_presence for student in self.students]
        average_presence = round(mean(list_of_presence),2)
        return average_presence
    
    def get_sorted_student_list_by_average_grade(self):
        students_sorted_by_grade = sorted(self.students, key=lambda student: student.average_grade)
        return students_sorted_by_grade

    def get_number_of_students_in_each_class(self):
        list_of_classes = [student.class_type for student in self.students]
        number_of_students_in_classes = collections.Counter(list_of_classes)
        return number_of_students_in_classes
            
    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        students_sorted_by_year = sorted(self.students, key=lambda student: student.year_of_birth)
        students_sorted_by_year_and_surname = sorted(students_sorted_by_year, key=lambda student: student.year_of_birth)
        return students_sorted_by_year_and_surname
