import csv
from tabulate import tabulate
from display import Displayer

class Student:
    def __init__(self, id, name, surname, year_of_birth, class_type ,average_grade,average_presence):
        self.id = id
        self.name = name
        self.surname = surname
        self.year_of_birth = int(year_of_birth)
        self.class_type = class_type
        self.average_grade = int(average_grade)
        self.average_presence = int(average_presence)
        self.displayer = Displayer()
  
    def create_student_list_from_csv():     
        with open ("class_data.csv") as file:
            class_data = csv.reader(file)
            students = []
            for row in class_data:
                id = row[0]
                name = row[1]
                surname = row[2]
                year_of_birth = row[3]
                class_type = row[4]
                average_grade = row[5]
                average_presence = row[6]

                student = Student(id,name, surname, year_of_birth, class_type ,average_grade,average_presence)
                students.append(student)
            return students