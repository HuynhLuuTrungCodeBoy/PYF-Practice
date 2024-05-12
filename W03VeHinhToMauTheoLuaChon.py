#import thư viện turtle
import turtle

#Khai báo biến shapeInput bằng giá trị người dùng nhập vào
#shapeInput = raw_input('Circle and square, what is your favorite shape?:') #raw_input không dùng trong python3
shapeInput = input('Circle and square, what is your favorite shape?:')
shapeInput = shapeInput.lower()

#Kiểm tra biến shapeInput có thuộc hình dáng mặc định đã cho hay không, nếu không thì in ra thông báo cho người dùng.
if shapeInput == 'circle' or shapeInput == 'square':
	...
else:
	print("Sorry, I don't have this shape :(")
	
#Nếu biến shapeInput thoã điều kiện, tiếp tục khai báo biến colorInput bằng giá trị người dùng nhập vào.
colorInput = input('What color will it be?, yellow, red or blue? :')
colorInput = colorInput.lower()

#Kiểm tra biến “colorInput” có thuộc hình dáng mặc định đã cho hay không, nếu không thì in ra thông báo cho người dùng.
if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue': 
	...
else:
	print("Sorry, I don't have this color :(")

# Thực hiện việc in hình vẽ dựa theo các biến mà người dùng vừa nhập vào.
# Trước tiên sẽ setup cửa sổ terminal
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Your shape")

#Setup hình dạng của khối theo giá trị “shapeInput” và “colorInput” và xuất ra kết quả
displayShape = turtle.Turtle()
displayShape.shape(shapeInput)
displayShape.color(colorInput)
turtle.done()