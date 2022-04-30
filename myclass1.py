class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def setage(self,age):
        self.age=age
d1=dog('proxy',23)
d2=dog('rocxy',25)
print(d1.getname())
print(d2.getage())
d1.setage(24)
print(d1.getage())

