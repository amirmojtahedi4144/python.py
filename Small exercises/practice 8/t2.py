class Students:
    sen = 0
    gen = 2
    clas = ""
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
    def sen_plus(self):
        self.sen += 1
        if self.sen == 10:
            print("ebtedaii")
        elif self.sen == 15:
            print("motevasete avalk")
        elif self.sen == 17:
            print("motevasete dovom")
    def gensiat(self):
        if self.gen == "pesar":
            print("pesarooneh")
        elif self.gen == "dokhtar":
            print("dokhtarooneh")
    def classs(self):
        if self.clas == "bahoosh":
            print("tizhooshan")
        elif self.clas == "kondzehn":
            print("nemooneh dolati")
s1 = Students("amir","mojtahedi")
print(s1.name)
print(s1.last_name)
while True:
    x = input()
    if x == 1:
        s1.sen_plus()
    elif x =="pesar":
        s1.gensiat()
    elif x == "dokhtar":
        s1.gensiat()
    else:
        s1.classs()