class StudentError(Exception):
    ...


class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} year's old\n"


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} year's old\n"


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()
        self.student_count = 0

    def add_student(self, student: Student):
        if self.student_count < 10:
            self.group.add(student)
            self.student_count += 1
        else:
            raise StudentError

    def delete_student(self, last_name: str):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student:
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__()
        return f'Number:{self.number}\n{all_students}'


gr = Group("1")

try:
    while True:
        student = Student("",1,"","","")
        gr.add_student(student)
except StudentError:
    print("Reached max student number")