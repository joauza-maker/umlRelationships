class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self):
        self.current_student = None 

    def assign_student(self, student_object):
        self.current_student = student_object 

alex = Student("Alex")
professor = Teacher()
professor.assign_student(alex)

print(professor.current_student.name)

