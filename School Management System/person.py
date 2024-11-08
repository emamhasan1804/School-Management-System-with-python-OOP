import random
from school import School
class Person:
    def __init__(self,name):
        self.name = name
    
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluateExam(self):
        return random.randint(1,100)

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom # object of Classroom
        self.__id = None
        self.marks = {} # {'eng':78,'ICT':90}
        self.subject_grade = {} #{'english':'A','math':'A+'}
        self.grade = None # final grade
    
    def finalGrade(self):
        sum = 0
        sub = 0
        for grade in self.subject_grade.values():
            point = School.gradeToValue(grade)
            sum += point
            sub += 1
        if sum>0:
            sum /= sub
        gpa = School.valueToGrade(sum)
        self.grade = gpa

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value



