class company():
    def _init_(self):
        self.__companyName="Google"
    def companyName(self):
        print(self.__companyName)
c1=company()
c1.companyName()
print(c1.__companyName)
