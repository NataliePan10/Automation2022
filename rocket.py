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
