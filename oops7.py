class Person:
    name="anonymous"

    def changName(self,name):
        self.__class__.name="Rihaan"
        #self.name=name
p1=Person()
p1.changName("Rihaan")
print(p1.name)
print(Person.name)