class student:
    name=''
    age=0
    city=''
    def __int__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(+self.name,+self.age,+self.city)
mahesh=student()
mahesh.display('mahesh',23,'akp')


