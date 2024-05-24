import turtle
t=turtle.Turtle()
t.hideturtle()

def ve_hcn(x,y,n,c,m,h=1):
  """ve_hcn là hàm vẽ hình chữ nhật.
  Hàm này nhận giá trị x,y là toạ độ điểm bắt đầu vẽ.
  h là hướng vẽ:
                1 là chiều kim đồng hồ,
                -1 chiều ngược hướng kim đồng hồ.
  n là chiều ngang, c là chiều cao, m là màu vẽ.
  x,y là số nguyên; n,c là số nguyên dương.
  m là số thập lục phân thể hiện màu theo quy ước hex hoặc tên màu tiếng anh.
  ví dụ về m: '#000000' là màu đen"""
  xx=int(x)
  yy=int(y)
  nn=int(n)
  cc=int(c)
  hh=int(h)

  global t # báo với python t là biến toàn cục
  t.penup()
  t.goto(xx,yy)
  t.pendown()
  t.color("blue")
  t.pensize(3)
  t.fillcolor(m)
  t.begin_fill()

  for i in range(2):
    t.forward(nn)
    if hh==1:
      t.right(90)
    else:
      t.left(90)
    t.forward(cc)
    if hh==1:
      t.right(90)
    else:
      t.left(90)
  
  t.end_fill()

# bắt đầu Vẽ nhà
ve_hcn(-200,50,90,150,"red",-1)
ve_hcn(-170,100,30,50,"green",-1)

ve_hcn(-200,50,90,150,"red",1)
ve_hcn(-170,-50,30,50,"green",-1)

ve_hcn(-110,50,90,150,"red",-1)
ve_hcn(-80,100,30,50,"green",-1)

ve_hcn(-110,50,90,150,"red",1)
ve_hcn(-80,-50,30,50,"green",-1)

ve_hcn(-20,50,150,150,"brown",1)
ve_hcn(30,-100,50,90,"yellow",-1)
#kết thúc vẽ nhà

turtle.done() #chờ đóng cửa sổ vẽ