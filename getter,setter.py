class exam:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.__marks={}
    def add_marks(self,subject,score):
        self.__marks[subject]=score
    def display(self):
        print(self.__marks)
e=exam("veera","503")     
e.add_marks('Mean',60)
e.add_marks('Cn',80)
e.display()
