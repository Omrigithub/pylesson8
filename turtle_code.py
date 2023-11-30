import turtle
import lesson




# Turtle -- Start
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
player = turtle.Turtle()


# Points
p1 = lesson.point(100,-200)
p2 = lesson.point(-100,200)

# Line
l1 = lesson.line2(p1,p2)
l1.paint_line(player)

# Circle
c0 = lesson.circle(10, 100)
c0.paint_circle(player)

print(c0.get_area())


turtle.done()
