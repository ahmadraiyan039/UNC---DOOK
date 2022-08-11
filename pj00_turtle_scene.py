"""It spells out your favorite college either Duke or UNC, depending on the user."""



from turtle import Turtle, done

import random

SPACE_BETWEEN_LETTERS: int = 3


def main() -> None:
    """Entrypoint of my program."""
    response: str = str(input("Are you Duke or UNC?"))
    x_pos: float = float(input("What is your x position?"))
    y_pos: float = float(input("What is your y position?"))
    size: float = float(input("What size?"))
    fill: str = str(input("What fill color do you want?"))
    if response == "Duke" or response == "duke":
        duke_t: Turtle = Turtle()
        draw_duke(duke_t, x_pos, y_pos, size, fill)     
    if response == "unc" or response == "UNC":
        UNC_t: Turtle = Turtle()
        draw_UNC(UNC_t, x_pos, y_pos, size, fill)
    done()
    

def draw_UNC(UNC: Turtle, x_pos: float, y_pos: float, size: float, fill: str) -> None:
    """Spells UNC, provided a turtle name, x and y position, size, and colors."""
    draw_U(UNC, x_pos, y_pos, size, fill)
    draw_N(UNC, x_pos, y_pos, size)
    draw_C(UNC, x_pos, y_pos, size, fill)
    

def draw_duke(D: Turtle, x_pos: float, y_pos: float, size: float, fill: str) -> None:
    """Spells Dook, provided a turtle name, x and y position, size, and colors."""
    draw_D(D, x_pos, y_pos, size, fill)
    draw_O(D, x_pos, y_pos, size, fill)
    draw_K(D, x_pos, y_pos, size)


def pick_color() -> str:
    """Picks a random pen color."""
    colors = ["blue", "green", "lightblue", "yellow", "brown"]
    return random.choice(colors)

    
def draw_D(D: Turtle, x_pos: float, y_pos: float, size: float, fill: str) -> None:
    """Writes the alphabet D."""
    D.penup()
    D.goto(x_pos, y_pos)
    D.pencolor(pick_color())
    D.fillcolor(fill)
    D.pendown()
    D.begin_fill()
    D.left(90)
    D.forward(size)
    D.right(90)
    D.circle(-size / 2, 180)
    D.hideturtle()
    

def draw_O(oo: Turtle, x_pos: float, y_pos: float, size: float, fill: str) -> None:
    """It draws the two Os."""
    oo.setheading(0)
    oo.penup()
    oo.goto((x_pos + size + 3), y_pos)
    oo.pencolor(pick_color())
    oo.fillcolor(fill)
    oo.pendown()
    oo.begin_fill()
    i: int = 0
    while i < 2:
        oo.setheading(0)
        oo.circle(size / 2)
        oo.goto((x_pos + size + size + 3), y_pos)
        i = i + 1
    oo.end_fill()
    oo.hideturtle()
    

def draw_K(K: Turtle, x_pos: float, y_pos: float, size: float) -> None:
    """Writes the alphbet K."""
    K.setheading(0)
    K.penup()
    K.goto((x_pos + 3 + (size * 2) + (size / 2) + 3), y_pos)
    K.pencolor(pick_color())
    K.pendown()
    K.left(90)
    K.forward(size)
    K.goto((x_pos + 3 + (size * 2) + (size / 2) + 3), y_pos + (size / 2))
    K.setheading(0)
    K.left(45)
    K.forward(size / 2)
    K.goto((x_pos + 3 + (size * 2) + (size / 2) + 3), y_pos + (size / 2))
    K.setheading(0)
    K.right(45)
    K.forward(size / 2)
    K.hideturtle()
    

def draw_U(U: Turtle, x_pos: float, y_pos: float, size: float, fill: str) -> None:
    """Writes the alphabet U."""
    U.penup()
    U.goto(x_pos, y_pos + size)
    U.setheading(270)
    U.pendown()
    U.pencolor(pick_color())
    U.fillcolor(fill)
    U.begin_fill()
    U.forward((3 * size) / 4)
    U.circle(size / 4, 180)
    U.setheading(90)
    U.forward((3 * size) / 4)
    U.end_fill()
    U.hideturtle()
    

def draw_N(N: Turtle, x_pos: float, y_pos: float, size: float) -> None:
    """Writes the alphabet N."""
    N.penup()
    N.pencolor(pick_color())
    N.goto(x_pos + (size / 2) + 3, y_pos)
    N.setheading(90)
    N.pendown()
    N.forward(size)
    N.right(135)
    N.forward((2 ** 0.5) * size)
    N.left(135)
    N.forward(size)
    N.hideturtle()
    

def draw_C(C: Turtle, x_pos: float, y_pos: float, size: float, fill: str) -> None:
    """Writes the alphabet C."""
    C.penup()
    C.goto(x_pos + 6 + (2 * size), y_pos)
    C.pencolor(pick_color())
    C.fillcolor(fill)
    C.pendown()
    C.setheading(180)
    C.begin_fill()
    C.circle(- size / 2, 200)
    C.end_fill()
    C.hideturtle()
    

if __name__ == "__main__":
    main()
