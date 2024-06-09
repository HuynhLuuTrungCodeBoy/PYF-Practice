import turtle
import time

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.screen = turtle.Screen()
        self.screen.setup(width=400, height=400)
        #self.screen.bgcolor("white")
        self.screen.bgcolor("#7AC7E8") #cyan color
        self.screen.title("Clock")
        self.screen.tracer(0)  # Tắt cập nhật tự động
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(3)

        # Vẽ mặt đồng hồ một lần
        self.draw_clock_face()

        # Tạo các con trỏ riêng biệt cho mỗi kim
        self.hour_hand = turtle.Turtle()
        self.minute_hand = turtle.Turtle()
        self.second_hand = turtle.Turtle()
        for hand in [self.hour_hand, self.minute_hand, self.second_hand]:
            hand.hideturtle()
            hand.speed(0)
            hand.pensize(3)

    def draw_clock_face(self):
        self.pen.penup()
        self.pen.goto(0, -160)
        self.pen.setheading(0)
        self.pen.color("black")
        self.pen.pendown()
        self.pen.circle(160)

        # Vẽ các vạch chia
        for i in range(60):
            angle=i*6
            self.pen.penup()
            self.pen.home()
            self.pen.setheading(angle)
            if i%5==0:
                self.pen.pensize(5)
                self.pen.forward(140)
                self.pen.pendown()
                self.pen.forward(18)
            else:
                self.pen.pensize(2)
                self.pen.forward(150)
                self.pen.pendown()
                self.pen.forward(8)

    def draw_clock_hands(self):
        # Vẽ kim giờ
        self.hour_hand.clear()
        self.hour_hand.penup()
        self.hour_hand.goto(0, 0)
        self.hour_hand.color("black")
        self.hour_hand.setheading(90)
        angle = (self.hour % 12) * 30 + (self.minute / 60) * 30
        self.hour_hand.right(angle)
        self.hour_hand.pendown()
        self.hour_hand.forward(80)

        # Vẽ kim phút
        self.minute_hand.clear()
        self.minute_hand.penup()
        self.minute_hand.goto(0, 0)
        self.minute_hand.color("black")
        self.minute_hand.setheading(90)
        angle = self.minute * 6 + (self.second / 60) * 6
        self.minute_hand.right(angle)
        self.minute_hand.pendown()
        self.minute_hand.forward(120)

        # Vẽ kim giây
        self.second_hand.clear()
        self.second_hand.penup()
        self.second_hand.goto(0, 0)
        self.second_hand.color("red")
        self.second_hand.setheading(90)
        angle = self.second * 6
        self.second_hand.right(angle)
        self.second_hand.pendown()
        self.second_hand.forward(140)

    def start_clock(self):
        while True:
            if self.second >= 60:
                self.second = 0
                self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
            if self.hour >= 24:
                self.hour = 0

            # Vẽ lại các kim
            self.draw_clock_hands()

            # Cập nhật lại màn hình để hiển thị các thay đổi mới nhất
            self.screen.update()

            # Delay để kiểm soát tốc độ chạy của đồng hồ
            time.sleep(1)

            # Tăng giây lên 1 đơn vị.
            self.second += 1

clock = Clock(23, 59, 0)
clock.start_clock()
