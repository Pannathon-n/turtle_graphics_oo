import turtle
import random

class Polygon:
    def __init__(self, num_side, size, orientation, location, color, border_size):
        self.num_sides = num_side
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

def get_new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

class PolygonArt:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def run(self):
        choice = int(input("Choose an art style (1-9): "))
        
        options = {
            1: (3, Polygon),
            2: (4, Polygon),
            3: (5, Polygon),
            4: (random.randint(3, 5), Polygon),
            5: (3, EmbeddedPolygon),
            6: (4, EmbeddedPolygon),
            7: (5, EmbeddedPolygon),
            8: (random.randint(3, 5), EmbeddedPolygon),
            9: (random.randint(3, 5), EmbeddedPolygon)
        }

        num_sides, polygon_class = options.get(choice, (3, Polygon))

        for _ in range(30):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)

            if polygon_class == EmbeddedPolygon:
                polygon = polygon_class(num_sides, size, orientation, location, color, border_size, num_levels=2, reduction_ratio=0.618)
            else:
                polygon = polygon_class(num_sides, size, orientation, location, color, border_size)

            polygon.draw()

            if choice == 9:
                new_color = get_new_color()
                Polygon(num_sides, size, orientation, location, new_color, border_size).draw()

        turtle.done()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        for _ in range(self.num_levels):
            super().draw()
            self.size *= self.reduction_ratio
            self.location[0] += self.size * (1 - self.reduction_ratio) / 2
            self.location[1] += self.size * (1 - self.reduction_ratio) / 2

art_generator = PolygonArt()
art_generator.run()
