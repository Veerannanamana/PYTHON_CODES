class KIET:
    def __init__(self,collage_name,location):
        self.collage_name=collage_name
        self.location=location
class KIET2:
    def __init__(self,strenth,branches):
        self.strenth=strenth
        self.branches=branches
class union(KIET,KIET2):
    def __init__(self,collage_name,location,strenth,branches,rank):
        KIET.__init__(self,collage_name,location)
        KIET2.__init__(self,strenth,branches)
        self.rank=rank
    def ok(self):
        print(self.collage_name,self.location,self.strenth,self.branches,self.rank)
u=union("PVU","KAKAINADA","100000","10","ANC:A++++")
u.ok()
