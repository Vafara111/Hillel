class Human:
    ...


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def compare_student(self, student: "Student") -> bool:
        if self == student:
            return True
        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} year's old\n"