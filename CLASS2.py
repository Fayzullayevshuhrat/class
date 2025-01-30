# class Pupil:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age} -->> yoshda"
# 
# 
#     def __add__(self, other):
#         return Pupil(self.name, self.age + other)
# 
# 
# p1 = Pupil("Shuhrat", 17)
# print(p1)
# p1 += 1
# 
# 
# print(p1)
# 
# 




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)

        
        
