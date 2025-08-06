'''class Vechile:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print("Engin Started")
class Car(Vechile):
    def __init__(self,brand,cost):
        Vechile.__init__(self,brand)
        self.cost=cost
    def start(self):
        super().start()
        print("Car is started")
        print(f"Brand is {self.brand} and cost {self.cost}.")
c=Car("BMW",121212)
c.start()'''
'''
class kiet2:
    def __init__(self,total_students,branches):
        self.total_students=total_students
        self.branches=branches
class kietw:
    def __init__(self,total_teachers,workers):
        self.total_teachers=total_teachers
        self.workers=workers
class kiet:
    def __init__(self,total_students,branches,total_teachers,workers,rooms):
        kiet2.__init__(self,total_students,branches)
        kietw.__init__(self,total_teachers,workers)
        self.rooms=rooms
    def display(self):
        print(":::KIET GROUP OF INSTITUTION:::")
        print("Total_Students:",self.total_students)
        print("Total_Branchess:",self.branches)
        print("Total_Teachers",self.total_teachers)
        print("Total_workers",self.workers)
        print("Total_Rooms",self.rooms)
k=kiet(6000,5,300,500,500)
k.display()'''
'''class one:
    def __init__(self,a):
        self.a=a
class two(one):
    def __init__(self,a,b):
        one.__init__(self,a)
        self.b=b
class three(two):
    def __init__(self,a,b,c):
        two.__init__(self,a,b)
        self.c=c
    def add(self):
        print(self.a+self.b+self.c)
t=three(10,20,30)
t.add()'''
class one:
    def __init__(self,a):
        self.a=a
class two(one):
    def __init__(self,a,b):
        one.__init__(self,a)
        self.b=b
    def add(self):
        print(self.a+self.b)
class three(one):
    def __init__(self,a,b):
        one.__init__(self,a)
        self.b=b
    def sub(self):
        print(self.a+self.b)
class four(three):
    def __init__(self,a,b,c):
        three.__init__(self,a,b)
        self.c=c
    def mul(self):
        print(self.a*self.b*self.c)
t=two(10,100)
tt=three(10,20)
f=four(1,2,3)
