class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def insert_pos(self,data,pos):
        new_node=Node(data)
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        temp = self.head
        for i in range(pos - 1):
            if temp is None:
                break
            temp = temp.next
        if temp is None:
            print("Out of range")
            return
        new_node.next=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("end")
l=Linked()
l.insert_begin(10)
l.insert_begin(20)
l.insert_end(30)
l.insert_end(40)
l.insert_pos(100,4)
l.display()
