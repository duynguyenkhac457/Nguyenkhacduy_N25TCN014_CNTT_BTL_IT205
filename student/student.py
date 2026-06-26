from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def show_info(self):
        pass

class Student(Person):
    def __init__(self, student_id, name, class_name):
        self.id = student_id
        self.name = name
        self.class_name = class_name

    def show_info(self):
        return f"{self.id} | {self.name} | {self.class_name}"
