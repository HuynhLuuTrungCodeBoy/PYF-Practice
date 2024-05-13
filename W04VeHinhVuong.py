import turtle
a = int(input("Nhập độ dài các cạnh của hình vuông: "))
t = turtle.Turtle()
t.hideturtle()
t.pencolor("red")
edge = 0
while edge < 4:
    # Vẽ 1 cạnh của hình vuông
    t.forward(a)
    t.right(90)
    # Câu lệnh này đặt trong vòng lặp while
    # số lần lặp là 4, nên được hình vuông yêu cầu
    edge += 1
turtle.done()