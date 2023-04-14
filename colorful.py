import turtle
colors=['orange','white','Green']
t=turtle.Pen()
turtle.bgcolor('blue')
for i in range(700):
    t.pencolor(colors[i%3])
    t.width(i/100+1)
    t.back(i)
    t.left(70)
    t.speed(45)
turtle.exitonclick()
