import turtle
import numpy
#######################
def draw_trapezoid(base1, base2, height, OutLineColor, FillColor, PenSize, x, y):#base1 là đáy lớn; x,y : toạ độ bên trái đáy lớn.
    t = turtle.Turtle()
    t.hideturtle()

    # Thiết lập các thuộc tính hình thức
    t.color(OutLineColor)
    t.fillcolor(FillColor)
    t.pensize(PenSize)

    # Di chuyển rùa đến vị trí bắt đầu vẽ
    t.penup()
    t.goto(x, y)
    t.pendown()    

    # Bắt đầu tô màu
    t.begin_fill()

    # Vẽ hình thang cân
    a=numpy.arctan(2*height/(base1-base2)) #tính góc
    a=abs(numpy.degrees(a))
    t.forward(base1)    
    t.left(180-a)
    huyen=( ((base1-base2)/2)**2 + height**2 )**(0.5)
    t.forward(huyen)
    t.left(a)
    t.forward(base2)
    t.left(a)
    t.forward(huyen)

    # Kết thúc tô màu
    t.end_fill()

    # Kết thúc chương trình
    #turtle.done()

####################################################################################

def draw_rectangle(OutLineColor, FillColor, PenSize, Height, Width, x, y):
    # Tạo một đối tượng rùa
    t = turtle.Turtle()
    t.hideturtle()
    # Thiết lập các thuộc tính hình thức
    t.color(OutLineColor)
    t.fillcolor(FillColor)
    t.pensize(PenSize)
    
    # Di chuyển rùa đến vị trí bắt đầu vẽ
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Bắt đầu tô màu
    t.begin_fill()
    
    # Vẽ hình chữ nhật
    for _ in range(2):
        t.forward(Width)
        t.right(90)
        t.forward(Height)
        t.right(90)
    
    # Kết thúc tô màu
    t.end_fill()
    
    # Kết thúc chương trình
    # turtle.done()

# Sử dụng hàm để vẽ tường và cửa
draw_rectangle("blue", "white", 3, 150, 250, -150, 0)
draw_rectangle("brown", "white", 3, 90, 50, -50, -50)

# Vẽ ống khói
draw_rectangle("blue", "white", 2, 50, 30, -30, 65)

#vẽ mái nhà
turtle.hideturtle()
turtle.penup()
#turtle.goto(-63,150)
turtle.goto(-150, 0)
turtle.pendown()
turtle.pensize(3)
turtle.fillcolor("white")
turtle.pencolor("blue")
turtle.begin_fill()
#turtle.circle(-100,steps=3)
turtle.left(45)
turtle.forward(115)
turtle.right(90)
turtle.forward(115)
turtle.end_fill()

#vẽ khói
draw_rectangle("gray", "gray", 1, 50, 1, -5, 130)
draw_rectangle("gray", "gray", 1, 30, 1, -20, 115)

# Vẽ cây thông lớn
draw_trapezoid(50, 30, 90, "#808080", "#808080", 3, 175, -250) #chân cây thông
draw_trapezoid(160, 0, 70, "#4E6028", "#4E6028", 3, 120, -160) # tán dưới
draw_trapezoid(120, 0, 50, "#76923C", "#76923C", 3, 140, -100) # tán giữa
draw_trapezoid(100, 0, 30, "#C2D59B", "#C2D59B", 3, 150, -53) # tán trên

# vẽ cây thông nhỏ
draw_trapezoid(30, 20, 65, "#808080", "#808080", 3, -210, -160) #chân cây thông
draw_trapezoid(80, 0, 35, "#4E6028", "#4E6028", 3, -235, -95) # tán dưới
draw_trapezoid(60, 0, 25, "#76923C", "#76923C", 3, -225, -65) # tán giữa
draw_trapezoid(40, 0, 15, "#C2D59B", "#C2D59B", 3, -215, -40) # tán trên
# Kết thúc chương trình
turtle.done()