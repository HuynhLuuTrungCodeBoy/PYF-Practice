#thêm thư viện vẽ
import turtle
import random

def mau_ngau_nhien(): #màu đen #000000 bị bỏ qua trong hàm này
  red=random.randint(1,255)
  green=random.randint(1,255)
  blue=random.randint(1,255)
  return f'#{red:02x}{green:02x}{blue:02x}'

def ve_hinh_elip(goc_quay,ban_truc_lon,ban_truc_nho):
  #khởi tạo t là 1 đối tượng hình vẽ
  t=turtle.Turtle()  
  t.speed(10)
  t.pensize(3)
  mau_sac=mau_ngau_nhien()
  t.color(mau_sac)
  t.hideturtle()
  t.right(goc_quay)
  t.showturtle()
  for i in range(2):
      t.circle(ban_truc_lon,90)
      t.circle(ban_truc_nho,90)


turtle.bgcolor("black")
for i in range(18):
  ve_hinh_elip(i*20,100,50)


#Hiển thị kết quả
turtle.done()
