import turtle


def draw_head():
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.circle(30)


def draw_body():
    turtle.penup()
    turtle.goto(0, 40)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(100)


def draw_arms():
    turtle.penup()
    turtle.goto(-30, -20)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(60)
    turtle.penup()
    turtle.goto(30, -20)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(60)


def draw_legs():
    turtle.penup()
    turtle.goto(0, -60)
    turtle.pendown()
    turtle.setheading(225)
    turtle.forward(80)
    turtle.penup()
    turtle.goto(0, -60)
    turtle.pendown()
    turtle.setheading(315)
    turtle.forward(80)


def main():
    turtle.speed(2)
    draw_head()
    draw_body()
    draw_arms()
    draw_legs()
    turtle.done()


if __name__ == "__main__":
    main()