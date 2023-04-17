class Student:
    def __init__(self, id, name, surname, year_of_birth, class_type ,average_grade,average_presence):
        self.id = id
        self.name = name
        self.surname = surname
        self.year_of_birth = int(year_of_birth)
        self.class_type = class_type
        self.average_grade = int(average_grade)
        self.average_presence = int(average_presence)
