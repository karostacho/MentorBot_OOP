## MentorBot ver.3.0

Your friend Justyna is a teacher and feel overwhelmed by all the duties in school. She asked you to write a short program that will help her cope with course management.

### Structure

MentorBot program structure should consists of at least four modules:

**file_data.py** - class that stores functions regarding data management when the data comes from file

**db_data.py** - class that stores functions regarding data management when the data comes from database

**display.py** - class that stores functions responsible for printing all the required data

**main_program.py** - Heart of MENTORBOT that contains the main class that is dependent on file_data.py or db_data.py (depending on data source) and display.py

You can introduce new classes if necessary to improve code quality.

For your implementation there is a "class_data.txt" CSV file.
Each line of the file represents student data in the following order:
`id,name,surname,year of birth,class,average grade,average presence`

The "file_data.py" module should read this file.
The "db_data.py" module should read local database table that will be created with the use of this file.

### Requirements

Justyna needs folowing functionality:

1. Get student by unique id
2. Get all students from given class
3. Get youngest student from all classes
4. Get oldest student from given class
5. Calculate average grade of all students
6. Returns rounded average presence of all students (2 decimal points)
7. Get sorted student list by average grade
8. Get number of students in each class
9. Get sorted student list by year of birth and then by surname

DEADLINE - 16.04.2023