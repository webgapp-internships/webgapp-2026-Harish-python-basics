class dog:
    def sound(self):
        print("Dog barks")
class cat:
    def sound(self):
        print("cat meow") 
class cow:
    def sound(self):
        print("cow moos")
animal=[dog(),cat(),cow()]
for i in animal:
    i.sound()