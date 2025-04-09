class Mynumbers:
    def __iter__(self):#you can do operations but always return  the iterator object itself
        self.a=1
        return self
    def __next__(self):#this method allows you to do operations
        x=self.a 
        self.a +=1
        return x
myclass =Mynumbers()
myiter=iter(myclass)
#__next__() method allows you to do operations,and must return the next item in the sequence
#__init__() method initializing when the object is being created