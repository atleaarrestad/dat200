import turtle


def _koch_fractal_onethird(lenght, depth, t: turtle.Turtle):
    if depth > 0:
        for angle in [60, -120, 60, 0]:
            _koch_fractal_onethird(lenght, depth-1, t)
            t.left(angle)
    else:
        t.forward(lenght)

def koch_fractal(lenght, depth):
    t = turtle.Turtle()
    t.pensize = 2
    t.speed(0)
    for i in range(3):
        _koch_fractal_onethird(lenght, depth, t)
        t.right(120)
    

koch_fractal(10, 3)
turtle.done()