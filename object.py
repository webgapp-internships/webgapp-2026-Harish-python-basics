class student:
    name="harish"
    college="karpagam"

student1=student()
print(student1.name)
print(student1.college)

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("harish",18)
print(s1.name)
print(s1.age)