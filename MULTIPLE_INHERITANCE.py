class student:
    def __init__(self,Id,Name):
        self.Id=Id
        self.Name=Name
class add:
    def __init__(self,vil):
        self.vil=vil
class education(student,add):
    def __init__(self,Id,Name,vil,Marks):
        student.__init__(self,Id,Name)
        add.__init__(self,vil)
        self.Marks=Marks
    def display(self):
        print("Student Roll Number is::",self.Id)
        print("Student Name is::",self.Name)
        print("Student add:",self.vil)
        print("Student Get Marks:",self.Marks)
Id=int(input())
Name=input()
vil="lutu"
Marks={'MPMC':55,'POC':56,'UHV':70}
s=education(Id,Name,vil,Marks,)
