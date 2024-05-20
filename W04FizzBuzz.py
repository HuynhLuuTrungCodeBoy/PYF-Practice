### INPUT nhập liệu
loi=True #loi là biến kiểm tra lỗi, True là có lỗi, có lỗi thì bắt nhập lại
while loi:
  loi = False #Mong muốn không có lỗi
  hai_so=input("Nhập vào 2 số nguyên dương bất kì (cách nhau khoảng trắng), số sau lớn hơn số trước:")#nhận vào 1 chuỗi
  tach_so=hai_so.split()# tách chuỗi thành các từ
  if len(tach_so) != 2: # nếu không phải 2 từ
    loi=True # có lỗi
  else:                 # nếu đúng là 2 từ
    for tu in tach_so:  # kiểm tra từng từ
      for i in tu:
        if ord(i) <48 or ord(i) >57:# Kiểm tra từng ký tự của mỗi từ, nếu không phải số thì
          loi=True ###################################################################### có lỗi
          print("2 số bạn nhập vào chưa phải số nguyên\n")
          break
      if loi:
        break
    if not loi:# Kiểm tra không gặp lỗi, đây là 2 số nguyên
      start=int(tach_so[0]) #lấy số nguyên đầu tiên
      end=int(tach_so[1]) #lấy số nguyên thứ hai
      if start>=end:# kiểm tra xem số trước có lớn hơn số sau không, nếu có thì
        loi=True ####################################################### có lỗi
        print("Số sau phải lớn hơn số trước.\n")

#########################################################################################
########################## PROCESSING AND OUTPUT Xử lý & XUẤT ###########################
#########################################################################################
for i in range(start,end+1):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)