import collections
from statistics import mean
from student_class import Student
from data_source import DataSource
from display import Displayer

class CsvFile(DataSource):
    def __init__(self):
        self.students = Student.create_student_list_from_csv()
        self.displayer = Displayer()
        
    def get_student_by_unique_id(self, id):
        searched_id = None
        for student in self.students:
            if student.find_by_id(id):
                searched_id = student
                break
        if searched_id:
            self.displayer.display(student)
        else:
            self.displayer.inform_id_does_not_exist()

    def get_all_students_from_given_class(self):
        for student in self.students:
            self.displayer.display(student)
        
    def get_youngest_student_from_all_classes(self):
        list_of_years = [student.year_of_birth for student in self.students]
        year_of_younger_student = (max(list_of_years))
        for student in self.students:
            if student.year_of_birth == year_of_younger_student:
                self.displayer.display(student)
    
    def get_oldest_student_from_all_classes(self):
        list_of_years = [student.year_of_birth for student in self.students]
        year_of_younger_student = (min(list_of_years))
        for student in self.students:
            if student.year_of_birth == year_of_younger_student:
                self.displayer.display(student)
    
    def calculate_average_grade_of_all_students(self):
        list_of_grades = [student.average_grade for student in self.students]
        self.displayer.display(mean(list_of_grades))
    
    def return_rounded_average_presence_of_all_students(self):
        list_of_presence = [student.average_presence for student in self.students]
        self.displayer.display(round(mean(list_of_presence),2)) 
    
    def get_sorted_student_list_by_average_grade(self):
        students_sorted_by_grade = sorted(self.students, key=lambda student: student.average_grade)
        for student in students_sorted_by_grade:
            self.displayer.display(student)

    def get_number_of_students_in_each_class(self):
        list_of_classes = [student.class_type for student in self.students]
        number_of_students_in_classes = collections.Counter(list_of_classes)
        for class_type, number in number_of_students_in_classes.items():
            self.displayer.inform_about_no_of_students(class_type, number)
        
    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        students_sorted_by_year = sorted(self.students, key=lambda student: student.year_of_birth)
        students_sorted_by_year_and_surname = sorted(students_sorted_by_year, key=lambda student: student.year_of_birth)
        for student in students_sorted_by_year_and_surname:
            self.displayer.display(student)
