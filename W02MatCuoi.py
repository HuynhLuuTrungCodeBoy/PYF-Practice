#Thêm thư viện Turtle
import turtle 

#Xác định kích thước bút vẽ
turtle.pensize(5)

#Xác định màu bút vẽ là Blue
turtle.pencolor("Blue")

#Vẽ mặt hình tròn lớn bên ngoài
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)

#Vẽ mắt bằng hai hình tròn và tô màu đỏ tương ứng cho mắt
    #Màu nền mắt là màu đỏ
turtle.fillcolor ("red")
    # khai bao bien eyesize lưu kích thước mắt
eye_size = 17.5
    #Vẽ mắt trái
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
    #Vẽ mắt phải
turtle.penup() 
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#Vẽ hình tam giác cho mũi
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-70, steps=3)

#Vẽ miệng cười bằng nửa hình tròn
turtle.penup()
turtle.goto(-100, -70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
#turtle.mainloop()

#Dừng màn hình chờ người dùng tắt
turtle.done()