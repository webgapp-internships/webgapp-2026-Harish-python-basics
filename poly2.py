class animal:
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("Dog barks")
class cat(animal):
    def sound(self):
        print("cat meow") 
a=animal()
b=dog()
c=cat()

a.sound()
b.sound()
c.sound()