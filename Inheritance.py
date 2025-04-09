#Parent class is the class being inherited from
#Child class is the class that inherits from another class

class person:#parent class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):#Method 
        print(self.fname,self.lname)

x=person("Logic ","Tumelo")
x.printname()

class Student(person):#child class
    def __init__(self, fname, lname , graduation_year):
        super().__init__(fname, lname)
        self.graduation_year=graduation_year
def Greet(self):#method
    print('Welcome', self.fname,self.lname, "to the class of ",self.graduationyear)