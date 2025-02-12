'''
A school maintains records of its employees and students. Your task is to implement a Python program using inheritance to model this scenario.
Requirements:
1. Create a base class Person with the following attributes:
name (string): Name of the person.
age (integer): Age of the person.
The class should have:
An __init__ method to initialize these attributes.
A display_info() method to print the details of the person.

2. Create a derived class Teacher that inherits from Person with additional attributes:
subject (string): Subject the teacher teaches.
salary (integer): Monthly salary of the teacher.
The class should:
Override the display_info() method to include the subject and salary.

3. Create another derived class Student that inherits from Person with additional attributes:
grade (string): The grade/class of the student.
roll_number (integer): The student's roll number.
The class should:
Override the display_info() method to include the grade and roll number.

4. Write a Python script to demonstrate the functionality:
Create objects of Teacher and Student classes.
Call their display_info() methods to print the details.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(self.name)
        print(self.age)

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary
    def display_info(self):
        super().display_info()
        print(self.subject)
        print(self.salary)
class Student(Person):
    def __init__(self,name,age,grade,roll_number):
        super().__init__(name,age)
        self.grade=grade
        self.roll_number=roll_number
    def display_info(self):
        super().display_info()
        print(self.grade)
        print(self.roll_number)

t1=Teacher("Ram", 43, "Coding", 60000)
s1=Student("Sita", 20, "A", 47)

print("***TEACHER DETAILS***")
t1.display_info()
print("***STUDENT DETAILS***")
s1.display_info()