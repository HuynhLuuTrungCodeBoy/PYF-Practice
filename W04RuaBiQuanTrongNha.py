# Import thư viện đồ họa turtle
import turtle

# Import thư viện sinh số ngẫu nhiên
import random as r

####### Khởi tạo đối tượng và vẽ đường bao giới hạn###########
# Khởi tạo đối tượng turtle và đặt ví trí
# con trỏ ở điểm 0, -200. Mục đích để vẽ
# đường bao nhốt rùa cân chính giữa màn hình
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, -200)

# Vẽ đường bao nhốt rùa
# đường bao có màu đen
t.speed(10)
t.pensize(10)
t.pencolor("black")
t.pendown()
t.circle(200)

# Đặt con trỏ rùa về chính giữa đường bao
# Đổi màu rùa màu xanh
t.penup()
t.speed(10)
t.shape("turtle")
t.pencolor('green')
t.goto(0, 0)

# Tạo hướng ngẫu nhiên ban đầu cho rùa
# khi ở vị trí chính giữa đường bao
angle = r.randint(0, 360)
t.right(angle)
t.showturtle()

# Bắt đầu cho rùa chạy thoát khỏi đường bao
# Khi rùa di chuyển đến đường bao, bắt rùa
# về lại vị trí chính giữa của hộp
count = 0
while True:
    t.speed(1)
    # rùa chỉ di chuyển một khoảng cách
    # hơi bé hơn bán kính của hộp tròn là 200
    # tránh rùa di chuyển đè lên vạch
    t.forward(188)

    # Bắt rùa về vị trí ban đầu, chính giữa hộp tròn
    t.hideturtle()
    t.speed(10)
    t.goto(0, 0)
    
    angle = r.randint(0, 360)
    # Tạo hướng mới cho rùa chạy, thử vận may mới
    t.right(angle)
    t.showturtle()
    # Khi rùa thử đến số lần nào đó thì dừng lại
    # kết thúc chương trình bằng lệnh break
    count += 1
    if count == 10:
        break

turtle.done()