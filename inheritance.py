print("single inheritance")
class animal:
    def sound(self):
        print("animals make sound")
class dog(animal):
    def bark(self):
        print("dog barks")
d=dog()
d.sound()
d.bark()
print("_________________________________")
print("multiple inheritance")
class father:
    def father_skill(self):
        print("driving")
class mother:
    def mother_skill(self):
        print("cooking")
class son(father,mother):
    pass
s=son()
s.father_skill()
s.mother_skill()
print("___________________________________")
print("multilevel inheritance")
class grandfather:
    def grand_property(self):
        print("grandfather property")
class father(grandfather):
    def father_property(self):
        print("father property")
class son(father):
    pass
s1=son()
s1.grand_property()
s1.father_property()
print("__________________________________________")
print("heirarchical inheritance")
class vehical:
    def vehical(self):
        print("vehical started")
class car(vehical):
    def car(self):
        print("car started")
class bike(vehical):
    pass
v=car()
v1=bike()
v.vehical()
v.car()
v1.vehical()
print("________________________________________")
print("hybrid inheritance")
class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
class C(A):
    def displayC(self):
        print("class C")
class D(B,C):
    def displayD(self):
        print("class D")
obj=D()
obj.displayA()
obj.displayB()
obj.displayC()
obj.displayD()
