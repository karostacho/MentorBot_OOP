import collections
from statistics import mean
from student_class import Student
from data_source import DataSource
from display import Displayer

class CsvFile(DataSource):
    def __init__(self):
        self.students = Student.create_student_list_from_csv()
        self.displayer = Displayer()
        
    def get_student_by_unique_id(self):
        list_of_ids = [student.id for student in self.students]
        student_id = self.displayer.ask_for_student_id()
        if student_id not in list_of_ids:
            self.displayer.inform_about_invalid("student id")
            self.get_student_by_unique_id()
        else:
            students_list = []
            for student in self.students:
                if student.id == student_id:
                    students_list.append(student)
            self.displayer.print_table(students_list)

    def get_all_students_from_given_class(self):
        class_type = self.displayer.ask_for_class_type()
        if class_type not in ["A", "a", "B", "b"]:
            self.displayer.inform_about_invalid("class type")
            self.get_all_students_from_given_class()
        else:
            students_list = []
            for student in self.students:
                if student.class_type == class_type:
                    students_list.append(student)
            self.displayer.print_table(students_list)
        
    def get_youngest_student_from_all_classes(self):
        list_of_years = [student.year_of_birth for student in self.students]
        year_of_younger_student = (max(list_of_years))
        students_list = []
        for student in self.students:
            if student.year_of_birth == year_of_younger_student:
                students_list.append(student)
        self.displayer.print_table(students_list)
    
    def get_oldest_student_from_all_classes(self):
        list_of_years = [student.year_of_birth for student in self.students]
        year_of_younger_student = (min(list_of_years))
        students_list = []
        for student in self.students:
            if student.year_of_birth == year_of_younger_student:
                students_list.append(student)
        self.displayer.print_table(students_list)
    
    def calculate_average_grade_of_all_students(self):
        list_of_grades = [student.average_grade for student in self.students]
        average_grade = mean(list_of_grades)
        self.displayer.display(f"Average grade of all students: {average_grade}")
    
    def return_rounded_average_presence_of_all_students(self):
        list_of_presence = [student.average_presence for student in self.students]
        average_presence = round(mean(list_of_presence),2)
        self.displayer.display(f"Average presence of all students: {average_presence}") 
    
    def get_sorted_student_list_by_average_grade(self):
        students_sorted_by_grade = sorted(self.students, key=lambda student: student.average_grade)
        self.displayer.print_table(students_sorted_by_grade)

    def get_number_of_students_in_each_class(self):
        list_of_classes = [student.class_type for student in self.students]
        number_of_students_in_classes = collections.Counter(list_of_classes)
        for class_type, number in number_of_students_in_classes.items():
            self.displayer.inform_about_no_of_students(class_type, number)
        
    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        students_sorted_by_year = sorted(self.students, key=lambda student: student.year_of_birth)
        students_sorted_by_year_and_surname = sorted(students_sorted_by_year, key=lambda student: student.year_of_birth)
        self.displayer.print_table(students_sorted_by_year_and_surname)
