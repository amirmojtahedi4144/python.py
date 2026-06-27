class School:
    kooler = ""
    th = 1
    nimk = 12
    def __init__(self,name,loc):
        self.name = name
        self.loc = loc
    def takhte_hooshmand(self):
        if self.th == "tizhooshan":
            print("madrese bakelas")
        elif self.th == "nemoone dolati":
            print("madrese mamooli")
    def koolerr(self):
        if self.kooler == "bikooler":
            print("madrese chert va pert")
        elif self.kooler == "kooler dar":
            print("madreseh pooldari")
    def nimkat(self):
        if self.nimk == "bedoone nimkat":
            print("mesle dabirestan")
        elif self.nimk == "daraye nimkat":
            print("mesle ebtedaii")
sch1 = School("roshd","ghaemshahr")
print(sch1.name)
print(sch1.loc)
print(sch1.koolerr())
while True:
    x = input()
    if x == "tizhooshan":
        sch1.takhte_hooshmand()
    elif x == "nemoone dolati":
        sch1.takhte_hooshmand()
    elif x == "bikooler":
        sch1.koolerr()
    elif x == "kooler dar":
        sch1.koolerr()
    else:
        sch1.nimkat()