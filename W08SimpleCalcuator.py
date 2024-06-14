# Bước 1: Import thư viện Tkinter
import tkinter as tk

# Bước 2: Khởi tạo biến expression, lưu trữ biểu thức toàn cục
expression = ""

# Bước 3: Hàm cập nhật biểu thức
def press(num):
    global expression # sử dụng expression như biến toàn cục
    expression = expression + str(num)
    equation.set(expression) # gán giá trị của expression cho biến equation

# Bước 4: Hàm tính toán kết quả cuối cùng
def equalpress():
    try:
        global expression
        total = str(eval(expression)) #hàm eval sẽ tự tính toán + - * / sin cos ..., str sẽ chuyễn kết quả thành string gán cho total
        equation.set(total) # equation là 1 StringVar nên phải dùng phương thức set() để gán giá trị cho nó. Không dùng "=" để gán.
        # expression = "" # expression là 1 biến string thông thường nên dùng "=" gán được. Sự tồn tại của lệnh này khiến chương trình ngu đi.
    except:
        equation.set("Error")
        expression = ""

# Bước 5: Hàm xoá biểu thức
def clear():
    global expression
    expression = ""
    equation.set("")

# Bước 6: Khởi tạo cửa sổ GUI
window = tk.Tk()

# Bước 7: Cài đặt cửa sổ GUI
window.configure(background="light grey") # màu nền cửa sổ là xám nhẹ
window.title("Simple Calculator") # tiêu đê cửa sổ là : Simple Calculator
# window.geometry("460x205") # kích thước cửa sổ ngang x cao.
window.resizable(width=False,height=False)

# Bước 8: Biến equation là StringVar để cập nhật giá trị ra GUI
equation = tk.StringVar() # equation là 1 biến StringVar và đang có giá trị rỗng

# Bước 9: Khai báo entry field để hiển thị biểu thức và kết quả
expression_field = tk.Entry(window, textvariable=equation,font=("",21,"")) # người dùng nhập info vào Entry expression_field sẽ được equation lấy ra ngoài
expression_field.grid(columnspan=4, ipadx=70) # columnspan=4 nghĩa là entry này đi ngang qua 4 cột.

# Bước 10: Khởi tạo nút các số từ 0 đến 9
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 0)
]

w=8
for (digit, row, column) in buttons:
    tk.Button(window, text=digit,font=("",16,"bold"), width=w, command=lambda num=digit: press(num)).grid(row=row, column=column)

# Bước 11: Khởi tạo nút các toán tử +, -, *, /
operators = [
    ('+', 1, 3), 
    ('-', 2, 3), 
    ('*', 3, 3), 
    ('/', 4, 3)
]

for (operator, row, column) in operators:
      tk.Button(window, text=operator,font=("",16,"bold"), width=w, command=lambda num=operator: press(num)).grid(row=row, column=column)

# Bước 12: Khởi tạo nút tính kết quả toán tử
tk.Button(window, text="=",font=("",16,"bold"), width=w, command=equalpress).grid(row=4, column=2)

# Bước 13: Khởi tạo nút Clear
tk.Button(window, text="Clear",font=("",16,"bold"), width=w, command=clear).grid(row=4, column=1)

# Bước 14: Khởi tạo nút nhập dấu chấm "."
tk.Button(window, text=".",font=("",16,"bold"), width=w, command=lambda : press('.')).grid(row=5, column=0)

# Bước 15: Main loop để cửa sổ GUI có thể hiển thị và xử lý sự kiện
window.mainloop()
