from turtle import *
speed(30)
width(4)
# კვადრატი
color("brown")

forward (200)
left(90)

forward(200)
left(90 )

forward (200)
left(90)

forward(200)
left(90)



# კარები

forward (70)
color ("gray")
left(90)
forward(120) #კარების სიმაღლე
right(90)
forward(60)
right(90)
forward(120)

penup() #კალმის აღება
goto (200, 200)
pendown () #კალმის ჩამოღება

#სახურავი
color("saddle brown")
begin_fill () #შიგნით გაფერადება
right (150)
forward (200)
left(120)
forward (200)
end_fill () #გაფერადება დასრულებულია

penup()
goto(10, 130)
pendown()

#ფანჯარა1
color ("cyan")
begin_fill()
right(150)
forward(50)
right (90)
forward(50)
right(90)
forward(50)
right (90)
forward(50)
right(90)
end_fill()

penup()
goto(190, 130)
pendown()

#ფანჯარა2
color("cyan")
begin_fill()
left(90)
forward(50)
right (90)
forward(50)
right(90)
forward(50)
right (90)
forward(50)
right(90)
end_fill()


exitonclick()