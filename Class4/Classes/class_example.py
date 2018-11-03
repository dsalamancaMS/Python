# init is a "constructor"
# default function of definitions of class
# __repr__ represent the object
# every class method has to have "self"
# Classes have to have first letter in upper case for everyword

# represent is 

class MyPoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Object x={self.x} y={self.y}'

    def distance(self, other_point=None):
        import math
        if other_point is None:
            return math.sqrt(self.x**2 + self.y**2)
        if isinstance(other_point,MyPoint):
            return math.sqrt((self.x - other_point.x)** 2 + 
                            (self.y - other_point.y)**2)
            
        
p1 = MyPoint(2,4)

p2 = MyPoint(2,-2)

print(p1)

print(p1.distance(p2))

######## *************** CHECK if X var is type Y


print('Is Instance:',isinstance(p1,MyPoint))



class MyLine(MyPoint):
    def __init__(self,par1,par2):
        self.p1 = MyPoint(*par1)
        self.p2 = MyPoint(*par2)


l1 = MyLine((2,3),(1,2))




