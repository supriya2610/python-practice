import math
class Area:
    def __init__(self,length,breadth,side,radius,celsius):
        self.length=length
        self.breadth=breadth
        self.side=side
        self.radius=radius
        self.celsius=celsius
    def rectangle(self):
        return self.length*self.breadth
    def square(self):
        return (self.side)**2
    def circle(self):
        return math.pi*((self.radius)**2)
    def temp(self):
        Farhenheit=((self.celsius)*(9/5))+32
        return Farhenheit
a=Area(3, 5, 4, 2,78)
print(a.rectangle())
print(a.square())
print(a.circle())
print(a.temp())
