from tabulate import tabulate

class Displayer:
    def show_menu(self):
        user_input = input("\nMentorBot\nWhat infromation would you like to get?\n\n1. Get student by unique id\n2. Get all students from given class\n3. Get youngest student from all classes\n4. Get oldest student from given class\n5. Calculate average grade of all students\n6. Get rounded average presence of all students (2 decimal points)\n7. Get sorted student list by average grade\n8. Get number of students in each class\n9. Get sorted student list by year of birth and then by surname\n0. Exit program\n")
        return user_input
        
    def display(self, message):
        print(message)

    def inform_the_selection_is_invalid(self):
        self.display("\nInvalid selection. Please select a number 0-9\n")

    def ask_for_class_type(self):
        class_type = input(f"Class type, please\n")
        return class_type.upper()
      
    def ask_for_student_id(self):
        student_id = input(f"Student id, please\n")
        return student_id

    def inform_about_invalid(self, selection):
        self.display(f"\nInvalid {selection}\n")

    def print_table(self, students_list):
        rows = []
        for student in students_list:
            rows.append([student.id, student.name, student.surname, student.year_of_birth, student.class_type, student.average_grade,student.average_presence])
        if not students_list:
            self.display("No results match your search criteria")
        else:
            headers = ["id", "name", "surname", "year_of_birth", "class_type" ,"average_grade","average_presence"] 
            self.display(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    def print_from_dictionary(self, number_of_students_by_class):
        for class_type, number in number_of_students_by_class.items():
            self.display(f"Number of students in class {class_type}: {number}")
    