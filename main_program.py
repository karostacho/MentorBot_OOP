from display import Displayer
from file_data import CsvFile
from db_data import SqlData

class MainProgram():
    def __init__(self):
        self.displayer = Displayer()
        self.csv_file = CsvFile()
        self.sql_data = SqlData()

    def run(self):
        user_input = self.displayer.show_menu()
        if not user_input.isdigit():
            self.displayer.inform_the_selection_is_invalid()
            return self.run()
        user_input = int(user_input)
        if user_input not in range(10):
            self.displayer.inform_the_selection_is_invalid()
            return self.run() 
        if user_input == 0:
            quit()
        if user_input == 1:
            student_id = self.displayer.ask_for_student_id()
            self.sql_data.get_student_by_unique_id(student_id)
            return self.run()  
        if user_input == 2:
            self.csv_file.get_all_students_from_given_class()
            return self.run() 
        if user_input == 3:
            self.csv_file.get_youngest_student_from_all_classes()
            return self.run() 
        if user_input == 4:
            self.csv_file.get_oldest_student_from_all_classes()
            return self.run() 
        if user_input == 5:   
            self.csv_file.calculate_average_grade_of_all_students()
            return self.run() 
        if user_input == 6:   
            self.csv_file.return_rounded_average_presence_of_all_students()
            return self.run()
        if user_input == 7:   
            self.csv_file.get_sorted_student_list_by_average_grade()
            return self.run() 
        if user_input == 8:   
            self.csv_file.get_number_of_students_in_each_class()
            return self.run() 
        if user_input == 9:   
            self.csv_file.get_sorted_student_list_by_year_of_birth_and_then_by_surname()
            return self.run() 
        else:
            self.displayer.inform_the_selection_is_invalid()
            return self.run() 
        
mentor_bot = MainProgram()
mentor_bot.run()
