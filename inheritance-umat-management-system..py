# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child class Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # Overriding display_info()
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

    def enroll_course(self, course):
        print(f"{self.name} has enrolled in {course}.")


# Child class Lecturer
class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def teach_course(self, course):
        print(f"{self.name} is teaching {course}.")


# Creating objects
student1 = Student("Rockson Baffour", 21, "FOE.41.006.mn")
lecturer1 = Lecturer("Dr. Cobbinah", 30, "LECTURER.oo1")


# Demonstration
print("Student Information")
student1.display_info()
student1.enroll_course("Object-Oriented Programming")

print("\nLecturer Information ")
lecturer1.display_info()
lecturer1.teach_course("Object-Oriented Programming")