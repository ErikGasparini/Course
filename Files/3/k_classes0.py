class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y


p = Point(3, 5)
print(p.getx())
print(p.gety())
