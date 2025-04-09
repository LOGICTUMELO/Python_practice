#Lambda functions 
x=lambda a:a+2
print(x(3))

def myadder(n):
    return lambda a:a+n 
Myadder=myadder(2)
print(Myadder(11))