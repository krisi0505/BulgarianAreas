import turtle
import pandas

screen = turtle.Screen()
image = "bg-02-scaled.gif"
# image = "Bulgaria_Administrative_Provinces.gif"
screen.addshape(image)
turtle.shape(image)

# def print_point(x, y):
#     print(x, y)
#
# turtle.onscreenclick(print_point)
#
# turtle.mainloop()

guessed_areas = set()

while len(guessed_areas) < 28:
    answer = screen.textinput(title=f"{len(guessed_areas)}/28 правилни", prompt="Напиши име на област")

    data = pandas.read_csv("areas.csv")

    row = data[data.area == answer]

    if answer == "предавам се":
        for index, a in data.iterrows():
            if a.area not in guessed_areas:
                t = turtle.Turtle()
                t.penup()
                t.hideturtle()
                t.setposition(float(a.x), float(a.y))
                t.write(f"{a.area}", align="center", font=("Arial", 12, "normal"))
        break

    if len(row) > 0:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.setposition(float(row.x.iloc[0]), float(row.y.iloc[0]))
        t.write(f"{row.area.iat[0]}", align="center", font=("Arial", 12, "normal"))
        guessed_areas.add(row.area.iat[0])
    else:
        print(f"Няма област {answer}")


screen.exitonclick()