#Thêm thư viện
import turtle

#Nhập khoảng cách:
khoang_cach=float(input("Mời nhập khoảng cách: "))

#Khỏi tạo đối tượng rùa R
R=turtle.Turtle()

#Ẩn rùa, nhấc bút lên
R.hideturtle()
R.penup()

#Chuyển đến toạ độ 0,0
R.goto(0,0)

#Hiện rùa, đặt bút xuống
R.showturtle()
R.pendown()

#Chọn dạng RÙA cho rùa R
R.shape("turtle")

#Chọn màu xanh rêu cho rùa
R.color("#6B8E23")

#Chọn tốc độ nhanh nhất cho rùa R
R.speed(0)

#vẽ
# Đặt góc quay ban đầu
ban_kinh1 = 5
ban_kinh2 = 5

# Vẽ đường tròn xoắn ốc
dem=0
ban_kinh=10
while True:
    R.circle(ban_kinh,extent=1)
    dem+=1
    if dem%180==0:
        ban_kinh+=10
    if R.distance(0,0)>khoang_cach:
        break

#Chờ người dùng bấm kết thúc vẽ
turtle.done()