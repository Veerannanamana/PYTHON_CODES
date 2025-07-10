class coll:
    def __init__(self,cname,add):
        self.cname=cname
        self.add=add
class kiet(coll):
    def __init__(self,cname,add,code):
        super().__init__(cname,add)
        self.code=code
    def show(self):
        print(f"My collage name is {self.cname} at {self.add} and EMCET code is {self.code}..")
k=kiet("kiet","korangi","B2")
k.show()
