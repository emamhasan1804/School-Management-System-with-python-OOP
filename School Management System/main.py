from school import School
from person import Student,Teacher,Person
from subject import Subject
from classroom import Classroom

# school
SHU = School('Sheikh Hasina University','Netrokona')
# add classrooms
fy = Classroom('First Year')
sy = Classroom('Second Year')
ty = Classroom('Third Year')
SHU.addClassroom(fy)
SHU.addClassroom(sy)
SHU.addClassroom(ty)
# add students
emam = Student('Emam Hasan',fy)
soumik = Student('Samiul Islam',sy)
maruf = Student('Naimul Ilsam',ty)
nusur = Student('Abdul Ahad',ty)
SHU.studentAdmission(emam)
SHU.studentAdmission(soumik)
SHU.studentAdmission(maruf)
SHU.studentAdmission(nusur)
# add teachers
abir = Teacher('Abir Sir')
shiam = Teacher('Shiam Sir')
mala = Teacher('Mala Mam')
SHU.addTeacher(abir)
SHU.addTeacher(shiam)
SHU.addTeacher(mala)
# add subjects:
lab = Subject('Lab Class',abir)
discrete = Subject('Discrete Mathematics',mala)
dld = Subject('Degital Logic Design',shiam)
club = Subject('Computer Club',abir)
fy.addSubject(lab)
fy.addSubject(discrete)
fy.addSubject(club)
sy.addSubject(dld)
sy.addSubject(club)
ty.addSubject(lab)
ty.addSubject(club)
# take exam
fy.takeSemesterFinalExam()
sy.takeSemesterFinalExam()
ty.takeSemesterFinalExam()
# print School
print(SHU)