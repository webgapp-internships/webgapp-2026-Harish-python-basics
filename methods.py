class department:
    def __init__(self,student_name):
        self.student_name=student_name
    def show(self):
        return "student details"
    
class cse(department):
    def details(self):
        return f"{self.student_name}:CSE department"

class ece(department):
    def details(self):
        return f"{self.student_name}:ECE department"

class IT(department):
    def details(self):
        return f"{self.student_name}:IT department"
class project(cse):
    def __init__(self,student_name,project_name):
        super().__init__(student_name)
        self.project_name=project_name

    def pro(self):
        return f"{self.student_name}:is woring in {self.project_name}"  
s1=cse("harish")
s2=ece("abineswari")
s3=IT("madhu")
s4=project("harish","management")

print(s1.details())
print(s2.details())
print(s3.details())
print(s4.pro())