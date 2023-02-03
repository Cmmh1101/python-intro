# creating a new class (self represents the self function)
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


# creating a point and assigning the values of x and y
newPointFromCLass = Point(2, 8)

print(newPointFromCLass.x)
print(newPointFromCLass.y)
