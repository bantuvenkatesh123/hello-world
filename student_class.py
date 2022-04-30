class Student:
    def __int__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def getgrade(self):
        return self.grade
class course:
    def __int__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]
    def addstudent(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    def get_overallgrade(self):
        value=0
        for student in self.students:
            value+=student.getgrade()
        return value/len(self.students)
s1=Student('venkatesh',23,90)
course1=course('science',1)
course1.addstudent(s1)
course1.addstudent(s2)
course1.addstudent(s3)
print(course.get_overallgrade())

