class vehical:
    def __init__(self,brand,speed):
        self.brand=brand
        self.__speed=speed
    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return f"brand:{self.brand}"
    
class car(vehical):
    def __init__(self,brand,speed,fuel_type):
        super(). __init__(brand,speed)
        self.fuel_type=fuel_type

    def show(self):
        print(self.get_brand())
        print("speed:",self.get_speed())
        print("fuel type:",self.fuel_type)

        if self.get_speed()>=120:
            print("status: fast car")
        else: 
            print("status:Normal car")

s1=car("Rolls Royce",130,"petrol")
s2=car("BMW",80,"diesel")

s1.show()
s2.show()