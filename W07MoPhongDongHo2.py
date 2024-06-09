import turtle
import time

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.screen = turtle.Screen()
        self.screen.setup(width=400, height=400)
        self.screen.bgcolor("#7AC7E8") # cyan color
        self.screen.title("Clock by Huỳnh Lưu Trung")        
        self.screen.tracer(0)  # Tắt cập nhật tự động để màn hình chạy mượt.
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(3)
        self.center = turtle.Turtle()
        self.center.color("red")
        self.center.shape("circle")
        self.center.penup()

        self.draw_clock_face()
        self.start_clock()

    def draw_clock_face(self):
        self.pen.penup()
        self.pen.goto(0, -160)
        self.pen.setheading(0)
        self.pen.color("black")
        self.pen.fillcolor("white")
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(160)
        self.center.goto(0, 0)
        self.pen.end_fill()

        # Vẽ các vạch chia
        for i in range(60):
            angle = i * 6
            self.pen.penup()
            self.pen.home()
            self.pen.setheading(angle)
            if i % 5 == 0:
                self.pen.pensize(5)
                self.pen.forward(140)
                self.pen.pendown()
                self.pen.forward(18)
            else:
                self.pen.pensize(2)
                self.pen.forward(150)
                self.pen.pendown()
                self.pen.forward(8)

    def draw_clock_hands(self, color1="white", color2="white", color3="white"):
        # Vẽ kim giờ
        self.pen.penup()
        self.pen.home()        
        self.pen.pensize(7)
        self.pen.setheading(90) # gốc thời gian, hướng 12h
        self.pen.color(color1)
        angle = (self.hour % 12) * 30 + (self.minute / 60) * 30
        self.pen.right(angle)
        self.pen.pendown()
        self.pen.forward(90)

        # Vẽ kim phút
        self.pen.penup()
        self.pen.home()        
        self.pen.pensize(5)
        self.pen.setheading(90)
        self.pen.color(color2)
        angle = self.minute * 6 
        self.pen.right(angle)
        self.pen.pendown()
        self.pen.forward(125)

        # Vẽ kim giây
        self.pen.penup()
        self.pen.home()        
        self.pen.pensize(1)
        self.pen.setheading(90)
        self.pen.color(color3)
        angle = self.second * 6
        self.pen.right(angle)
        self.pen.pendown()
        self.pen.forward(135)

    def start_clock(self):#update clock
        # Xóa các kim bằng cách vẽ chúng với màu nền
        self.draw_clock_hands()

        # Cập nhật thời gian
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1
        if self.hour >= 24:
            self.hour = 0

        # Vẽ các kim với màu mới
        self.draw_clock_hands("black", "green", "red")

        # Cập nhật lại màn hình để hiển thị các thay đổi mới nhất
        self.screen.update()

        # Lên lịch gọi lại hàm start_clock sau 1 giây để update lại màn hình vẽ
        self.screen.ontimer(self.start_clock, 1000)

clock = Clock(23, 59, 0)
turtle.mainloop()
