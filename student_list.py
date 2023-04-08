import csv
from student_class import Student

class StudentList:
    def __init__(self):
        self.students = []

    def create_student_list_from_csv(self):     
        with open ("class_data.csv") as file:
            class_data = csv.reader(file)
            for row in class_data:
                id = row[0]
                name = row[1]
                surname = row[2]
                year_of_birth = row[3]
                class_type = row[4]
                average_grade = row[5]
                average_presence = row[6]

                student = Student(id,name, surname, year_of_birth, class_type ,average_grade,average_presence)
                self.students.append(student)
            return self.students