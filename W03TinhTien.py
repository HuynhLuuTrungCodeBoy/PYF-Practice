'''Viết chương trình hỏi người dùng đã chi bao nhiêu tiền tại cửa hàng.
Nếu họ chi ít hơn 75$, họ sẽ không được giảm giá.
Nếu họ chi 75$ trở lên, họ sẽ được giảm giá 15$.
Nếu người dùng chi từ 100$ trở lên, họ sẽ được giảm giá 25$.
Nếu người dùng chi từ 150$ trở lên, họ sẽ được giảm giá 50$.
Sau đó in ra tổng số tiền mà người dùng phải thanh toán.'''

tien=int(input("Số tiền đã chi: "))
thanh_toan=tien
if tien<75:
  ...
elif tien<100:
  thanh_toan-=15
elif tien<150:
  thanh_toan-=25
elif tien>=150:
  thanh_toan-=50
print("Số tiền cần thanh toán là:",thanh_toan)