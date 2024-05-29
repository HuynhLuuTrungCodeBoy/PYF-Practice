import turtle
import numpy
#######################
#khởi tạo con rùa t; ẩn con rùa t   ;Tốc độ vẽ nhanh tối đa
t = turtle.Turtle(); t.hideturtle() ;t.speed(0)

def draw_trapezoid(base1, base2, height, OutLineColor, FillColor, PenSize, x, y):#base1 là đáy lớn; x,y : toạ độ bên trái đáy lớn.
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
    t.left(180-a)## Để con trỏ luôn hướng phải sau khi vẽ xong.

    # Kết thúc tô màu
    t.end_fill()

    # Kết thúc chương trình
    #turtle.done()

####################################################################################

def draw_rectangle(OutLineColor, FillColor, PenSize, Height, Width, x, y):
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
    
#Hàm vẽ cây thông
def draw_pine(width_tree,height_tree,x,y):#x, y là toạ độ gốc dưới bên trái của cây thông (điểm xám thấp nhất, bên trái)
    height_top=height_tree//11
    height_middle=height_top*2
    height_bottom=height_top*3
    height_root=height_top*5
    width_root_top=height_top
    width_root_bottom=int(width_tree*0.4)
    width_bottom=width_tree
    width_middle=int(width_tree*0.8)
    width_top=int(width_tree*0.6)
    draw_trapezoid(width_root_bottom, width_root_top, height_root, "#808080", "#808080", 3, x, y) #chân cây thông
    draw_trapezoid(width_bottom, 0, height_bottom, "#4E6028", "#4E6028", 3, x+width_root_bottom//2-width_bottom//2, y+height_root) # tán dưới
    draw_trapezoid(width_middle, 0, height_middle, "#76923C", "#76923C", 3, x+width_root_bottom//2-width_middle//2, y+height_root+height_bottom) # tán giữa
    draw_trapezoid(width_top, 0, height_top, "#C2D59B", "#C2D59B", 3, x+width_root_bottom//2-width_top//2, y+height_root+height_bottom+height_middle) # tán trên
    

#Hàm vẽ nhà
def draw_house(line_house,fill_house,line_size,height,width, x, y,line_door,fill_door):
    # Sử dụng hàm để vẽ tường và cửa
    #draw_rectangle("blue", "white", 3, 150, 250, -150, 0)
    draw_rectangle(line_house, fill_house, line_size, height, width, x, y)
    #draw_rectangle("brown", "white", 3, 90, 50, -50, -50)
    height_door=int(height*0.6)
    width_door=int(width*0.2)
    x_door=x + (width-width_door)//2
    y_door=y - (height-height_door)*5//6
    draw_rectangle(line_door, fill_door, line_size, height_door, width_door, x_door, y_door)

    # Vẽ ống khói
    y_chimney=y+int(height*0.2)
    draw_rectangle(line_house, "grey", line_size, -1*height_door//2, width_door//2, x_door, y_chimney)

    #vẽ mái nhà
    ###Chuẩn bị
    # t.pensize(3)
    t.pencolor(line_house)
    # t.fillcolor(fill_house)
    t.fillcolor("brown")

    ###Đưa bút vào vị trí
    t.penup()
    t.goto(x, y)

    ###Bắt đầu vẽ mái nhà
    t.pendown()
    t.begin_fill()
    t.left(45)
    t.forward(int(width*0.46))
    t.right(90)
    t.forward(int(width*0.46))
    t.left(45)
    t.end_fill()

    #vẽ khói
    draw_rectangle("gray", "gray", 1, -1*height_door//2, 1, x_door+(width_door//2)*8//10,10+y_chimney+height_door//2)
    draw_rectangle("gray", "white", 1, -1*height_door//3, 1,x_door + width_door//10      ,10+y_chimney+height_door//2)

def dat_con_rua(rua,x,y):
    rua.hideturtle()
    rua.penup()
    rua.goto(x,y)
    rua.pendown()
#Vẽ mặt trời
def draw_sun(x,y):
    #dat_con_rua(t,215,135)
    dat_con_rua(t,x,y)
    t.color("red","yellow")
    t.pensize(5)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.color("black")
#################################################################################
#Bắt đầu main
#################################################################################
ngang=40;cao=60;toa_do_x=-300;toa_do_y=210
for row in range(6):
    ngang+=3*row
    cao+=6*row
    toa_do_x=-300+40*(row%2)
    for tree in range(7-row):
        draw_pine(ngang,cao,toa_do_x, toa_do_y)
        toa_do_x+=ngang+20
    toa_do_y-=cao
#Vẽ nhà
draw_house("blue", "#00A2E8", 3, 150, 250, -70, 0,"red", "#C3C3C3")
#draw_pine(ngang,cao,toa_do_x, toa_do_y+cao);
draw_pine(160,240,185,-250)
draw_sun(215,135)
#################################################################################
#Kết thúc main
#################################################################################
# Kết thúc chương trình
turtle.done()