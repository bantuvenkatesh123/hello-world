class myclass:
    id=0
    name=""
    def display(self,id,name):
        self.id=id
        self.name=name
        print(self.id,self.name)
info=myclass()
info.display(140687,'venkatesh')
