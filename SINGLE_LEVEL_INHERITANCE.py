class KIET:
    def __init__(self,collage_name,location):
        self.collage_name=collage_name
        self.location=location
class AID(KIET):
    def __init__(self,collage_name,location,department,num_students):
        super().__init__(collage_name,location)
        self.department=department
        self.num_students=num_students
    def aid_info(self):
        print("COLLAGE NAME:",self.collage_name)
        print("LOCATION:",self.location)
        print("DEPARTMENT:",self.department)
        print("TOTAL STUDENTS:",self.num_students)
class AIML(KIET):
    def __init__(self,collage_name,location,department,num_students):
        super().__init__(collage_name,location)
        self.department=department
        self.num_students=num_students
    def aiml_info(self):
        print("COLLAGE NAME:",self.collage_name)
        print("LOCATION:",self.location)
        print("DEPARTMENT:",self.department)
        print("TOTAL STUDENTS:",self.num_students)
a=AID("KIET","LORANGI","AID","210")
aa=AIML("KIET","LORANGI","AID","210")
a.aid_info()
aa.aiml_info()
