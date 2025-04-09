class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'{self.name}{self.age}'

p1=person("Logic ",19)
p2=person("Arthur ",29)
p3=person("Thapelo ",13)
print(p1,p2,p3 )