class person:
    def __init__(self,name,age):
        self.name=name
        self.age=str(age)

p1=person("Logic",19)
print('my name is '+p1.name +' i am '+ p1.age + ' years old') 