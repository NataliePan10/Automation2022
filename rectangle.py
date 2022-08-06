class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

rec = Rectangle(length = 5, width=7)
rec.area()
