class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
l=Linked()
l.insert_begin(10)
l.insert_begin(20)
l.insert_begin(30)
l.display()
