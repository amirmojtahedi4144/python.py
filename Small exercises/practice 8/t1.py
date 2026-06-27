class Person:
    dast = 2
    cheshm = 2
    pa = 2
    zaban = 1
    degree = ""
    age = 0
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

    def age_plus(self):
        self.age +=1
        if self.age == 10:
            self.degree = "sikl"
            print("sikl daryaft kardid")
        elif self.age == 18:
            self.degree = "diplom"
            print("diplom gereftid")
        elif self.age == 23:
            self.degree = ("lisans")
            print("lisans gereftid")
    def daramad(self):
        if self.degree == "":
            print(0)
        elif self.degree == "sikl":
            print(500)
        elif self.degree == "diplom":
            print(1000)
        elif self.degree == "lisans":
            print(1500)

p1 = Person("amir","mojtahedi")
print(p1.name)
print(p1.last_name)
print(p1.degree)
while True:
    x = int(input())
    if x == 1:
        p1.age_plus()
    else:
        p1.daramad()