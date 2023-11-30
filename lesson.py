import math
import turtle


class point:
    def __init__(self, x=0, y=0):
        self.x_cor = x
        self.y_cor = y

    def get_x(self):
        return self.x_cor

    def get_y(self):
        return self.y_cor

    def __str__(self):
        return "point position: {}".format(self.get_x() + self.get_y())


class line:
    def __init__(self, x1, x2, y1, y2):
        self.x1_cor = x1
        self.x2_cor = y1
        self.y1_cor = x2
        self.y2_cor = y2

    def paint_line(self, player):
        player.pu()
        player.goto(self.x1_cor, self.x2_cor)

    def get_length(self):
        return math.sqrt((self.x1_cor - self.x2_cor) ** 2 + (self.y2_cor - self.y2_cor) ** 2)


class line2:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def get_length(self):
        return math.sqrt((self.point1.x_cor - self.point2.x_cor) ** 2 + (self.point2.y_cor - self.point2.y_cor) ** 2)

    def paint_line(self, player):
        player.pu()
        player.goto(self.point1.x_cor, self.point1.y_cor)
        player.pd()
        player.goto(self.point2.x_cor, self.point2.y_cor)

class triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def get_perimiter(self):
        return line(self.p1, self.p2).get_length() + line(self.p1, self.p2).get_length() + line(self.p1,
                                                                                                self.p2).get_length()


class circle:
    def __init__(self, point, radius=100):
        self.p = point
        self.r = radius

    def get_area(self):
        return self.r ** 2 * math.pi

    def paint_circle(self, player):
        player.pd()
        player.circle(self.r)


