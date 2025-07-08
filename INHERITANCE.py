class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class faculty(person):
    def __init__(self,id,name,subject):
        person.__init__(self,id,name)
        self.subject=subject
    def show2(self):
        print(f"Mr.{self.name}, bearing the employee ID {self.name}, is a faculty member who teaches {self.subject}.")
class student(person):
    def __init__(self,id,name,branch):
        person.__init__(self,id,name)
        self.branch=branch
    def show3(self):
        print(f"I am {self.name}, bearing the roll number {self.id}..")
class projectmember:
    def __init__(self,pro_title):
        self.pro_title=pro_title
    def show4(self):
        print(f"Project title is {self.pro_title}..")
class intern(student,projectmember):
    def __init__(self,id,name,branch,pro_title,com_info):
        student.__init__(self,id,name,branch)
        projectmember.__init__(self,pro_title)
        self.com_info=com_info
    def show5(self):
        print(f"I am {self.name}, bearing the roll number {self.id}. I am currently pursuing B.Tech in the stream of Artificial Intelligence and Data Science ({self.branch}). I am working on a project titled {self.pro_title} at {self.com_info}.")
i=intern("23B25A4503","N.V.N.M.Lakshman","AID","INHERITANCE","KIET")
f=faculty("50001","Venkatesh","Web Development")
f.show2()
i.show3()
i.show4()
i.show5()
