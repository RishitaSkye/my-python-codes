 #OOPS CONCEPT
class Student:
    college_name= "NSEC"
    def __init__(self,name,marks):
     self.name=name
     self.marks=marks
     
     print("adding new students in database...")
s1=Student("Radha", 96)
print(s1.name)
print(s1.marks)

s1=Student("Krishna",98)
print(s1.name)
print(s1.marks)

print(Student.college_name)




class Student:
    college_name= "NSEC"
    name="anonymous" #class.attr
    def __init__(self,name):
     self.name=name #obj.attr
     print("adding new students in database...")

s1=Student("Rishita")
print(s1.name)

print(Student.college_name)




class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi", self.name, "Your average score is:", sum/3)
s1=Student("Abhishek Ghosh", [98,57,69])
s1.get_avg()

s1.name="Debjani Das"
s1.get_avg()