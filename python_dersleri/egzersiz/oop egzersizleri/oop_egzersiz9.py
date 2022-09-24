class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print("The name of student is:",self.name)
        print("The age of student is:",self.age)
        print("The section of student is:",self.section)

student = Student("Emre Güler", 20, "Computer Engineering")
student.displayStudent()
