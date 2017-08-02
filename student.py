"""
A module for handling school students related information
"""


class Student(object):
    """Basic student class"""

    def __init__(self, name, ID, GPA):
        self.name = name
        self._GPA = GPA     # protected
        self.__ID = ID      # private

    def get_GPA(self):
        return self._GPA

    def set_GPA(self, GPA):
        self._GPA = GPA

    def __str__(self):
        return "Student Name " + self.name


class GradStudent(Student):
    def __init__(self, name, ID, GPA):
        super().__init__(name, ID, GPA, 'Grad')

    def is_pass(self):
        return self.get_GPA() >= 3

    def set_advisor(self, advisor):
        self.advisor = advisor

    def get_advisor(self):
        return self.advisor

class UndergradStudent(Student):
    def __init__(self, name, ID, GPA):
        super().__init__(name, ID, GPA, 'Undergrad')

    def is_pass(self):
        return self.get_GPA() >= 2.5
