class Person:
    name="anonymous"

   # def changeName(self,name): #self basically a obj
    #    self.__class__.name="Rihaan"
        #self.name=name

    @classmethod
    def changeName(cls, name):
        cls.name=name
p1=Person()
p1.changeName("Rihaan")
print(p1.name)
print(Person.name)