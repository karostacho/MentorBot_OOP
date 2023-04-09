from student_class import Student
import collections
from statistics import mean

students = Student.create_student_list_from_csv()

def get_student_by_unique_id( id):
    students = Student.create_student_list_from_csv()
    for student in students:
        #if student == student.find_by_id(id):
        print(student.find_by_id(id))

def get_youngest_student_from_all_classes():
    students = Student.create_student_list_from_csv()
    list_of_years = [student.year_of_birth for student in students]
    print(max(list_of_years))

def get_sorted_student_list_by_average_grade():
    students = Student.create_student_list_from_csv()
    students_sorted_by_grade = sorted(students, key=lambda student: student.average_grade)
    return students_sorted_by_grade
        
def get_number_of_students_in_each_class():
    list_of_classes = [student.class_type for student in students]
    number_of_students_in_classes = collections.Counter(list_of_classes)
    for class_type, number in number_of_students_in_classes.items():
        print(f"Number of people in class {class_type}: {number}")

def calculate_average_grade_of_all_students():
    list_of_grades = [student.average_grade for student in students]
    print(mean(list_of_grades))


get_student_by_unique_id("P9!x")