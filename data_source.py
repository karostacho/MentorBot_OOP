from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def get_student_by_unique_id(self):
        pass

    @abstractmethod
    def get_all_students_from_given_class(self):
        pass

    @abstractmethod
    def get_youngest_student_from_all_classes(self):
        pass

    @abstractmethod
    def get_oldest_student_from_all_classes(self):
        pass

    @abstractmethod
    def calculate_average_grade_of_all_students(self):
        pass

    @abstractmethod
    def return_rounded_average_presence_of_all_students(self):
        pass

    @abstractmethod
    def get_sorted_student_list_by_average_grade(self):
        pass

    @abstractmethod
    def get_number_of_students_in_each_class(self):
        pass

    @abstractmethod
    def get_sorted_student_list_by_year_of_birth_and_then_by_surname(self):
        pass
    
