class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = [] # list of teacher object
        self.classrooms = {} # {"class" : classroom object}
    def addClassroom(self,classroom):
        self.classrooms[classroom.name] = classroom
    def addTeacher (self,teacher):
        self.teachers.append(teacher)
    def studentAdmission(self,student):
        class_name = student.classroom.name
        self.classrooms[class_name].addStudent(student)

    @staticmethod
    def calculateGrade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70:
            return 'A'
        elif marks>=60:
            return 'A-'
        elif marks>=50:
            return 'B'
        elif marks>=40:
            return 'C'
        elif marks>=33:
            return 'D'
        else :
            return 'F'
    
    @staticmethod
    def gradeToValue(grade):
        grades = {'A+':5.00,'A':4.00,'A-':3.50,'B':3.00,'C':2.00,'D':1.00,'F':0.00}
        return grades[grade]
    
    @staticmethod
    def valueToGrade(value):
        if value == 5.00:
            return 'A+'
        elif value>=4.00:
            return 'A'
        elif value>=3.50:
            return 'A-'
        elif value>=3.00:
            return 'B'
        elif value>=2.00:
            return 'C'
        elif value>=1.00:
            return 'D'
        else :
            return 'F'
        
    def __repr__(self):
        for key in self.classrooms.keys():
            print(key)
        # all classrooms
        print("Students")
        result = ''
        for key,value in self.classrooms.items():
            result += f'---{key.upper()} classroom students\n'
            for student in value.students:
                result += f'{student.name}\n'
        print(result)

        # all students
        subject = ''
        for key,value in self.classrooms.items():
            subject += f'---{key.upper()} classroom subjects\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print(subject)

        # all subjects
        print("Teachers : ")
        for teacher in self.teachers:
            print(teacher.name)
        print("Students Ruselts")
        for key,value in self.classrooms.items():
            print(f'{key} results:')
            for student in value.students:
                for sub,mar in student.marks.items():
                    print(student.name,sub,mar,student.subject_grade[sub])
                print("Final Grade : ",student.grade)
                print()
        return ''
        # all students results