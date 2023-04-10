from tabulate import tabulate

class Displayer:
    def show_menu(self):
        user_input = input("\nMentorBot\nWhat infromation would you like to get?\n\n1. Get student by unique id\n2. Get all students from given class\n3. Get youngest student from all classes\n4. Get oldest student from given class\n5. Calculate average grade of all students\n6. Get rounded average presence of all students (2 decimal points)\n7. Get sorted student list by average grade\n8. Get number of students in each class\n9. Get sorted student list by year of birth and then by surname\n0. Exit program\n")
        return user_input
        
    def display(self,message):
        print(message)

    def inform_the_selection_is_invalid(self):
        self.display("\nInvalid selection. Please select a number 0-9\n")

    def ask_for_student_id(self):
        student_id = input("Student id, please\n")
        return student_id
    
    def ask_for_student_class_type(self):
        class_type = input("Class Type, please\n")
        return class_type

    def inform_id_does_not_exist(self):
        self.display("\nInvalid student ID\n")

    def inform_about_no_of_students(self,class_type, number):
        self.display(f"Number of students in class {class_type}: {number}")

    def print_table(self, rows, headers):
        table = tabulate(rows, headers)
        self.display(table)



    