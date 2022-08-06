

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

rec = Rectangle(length = 5, width=7)
rec.area()

class Rocket:
    def __init__(self):
        self.x=0
        self.y = 0

    def move_up(self):
        self.y += 1

    def move_right(self):
        self.x += 1

    def mode_down(self):
        self.y -= 1

    def move_left(self):

        self.x -= 1

    def current_position(self):
        print(self.x, self.y)

rocket = Rocket()
rocket.current_position()





#my_kid = Child(10, 'Mike')

#print(my_kid.age)
#print(my_kid.name)

# initializing another object of Child



