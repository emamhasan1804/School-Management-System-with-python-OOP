class Classroom:
    def __init__(self,name):
        self.name = name
        self.students = [] # list of Student object
        self.subjects = [] # list of Subject object
    def addStudent(self,student):
        roll_no = f"{self.name} - {len(self.students)+1}"
        student.id = roll_no
        self.students.append(student)

    def addSubject(self,subject):
        self.subjects.append(subject)

    def takeSemesterFinalExam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.finalGrade()