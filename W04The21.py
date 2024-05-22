import random
################################### INPUT
print("ĐÂY LÀ TRÒ CHƠI CỘNG DỒN. AI GÂY RA SỐ >=21 TRƯỚC THÌ THUA")
loi=True
while loi:
  loi=False
  s=input("Bạn chọn chẵn (0) hay lẻ (1):")
  if len(s)!=1:
    loi=True
    print("\nNhập 0 để chọn chẵn, nhập 1 để chọn lẻ.")
  else:
    if not(ord(s)==48 or ord(s)==49):
      loi=True
      print("\nNhập 0 để chọn chẵn, nhập 1 để chọn lẻ.")
    else:
      so=int(s)
if so==0:
  print("Bạn đã chọn 0, vậy Máy là 1.")
else:
  print("Bạn đã chọn 1, vậy Máy là 0.")
############################### PROCESSING and OUTPUT
tong=0
while True:
  hien=random.randint(0,1)
  print("\nSố ngẫu nhiên:",hien)  
  if hien==so:#Người chơi trước
    loi=True
    while loi:
      nguoi=int(input("Mời bạn chọn 1 số (1, 2 hoặc 3):"))
      if nguoi==1 or nguoi==2 or nguoi==3:
        loi=False
    tong+=nguoi
    print(f"Với bộ số (1, 2, 3), Bạn chọn {nguoi} nên Tổng = {tong}")
    if tong>=21:
      print(f"Tổng >= 21. Bạn thua, Máy thắng!")
      break
    else:
      may=random.randint(1,3)
      tong+=may
      print(f"Với bộ số (1, 2, 3), Máy chọn {may} nên Tổng = {tong}")
      if tong>=21:
        print(f"Tổng >= 21. Máy thua, Bạn thắng!")
        break

  else:#khác biến so nên máy chơi trước
    may=random.randint(1,3)
    tong+=may
    print(f"Với bộ số (1, 2, 3), Máy chọn {may} nên Tổng = {tong}")
    if tong>=21:
      print(f"Tổng >= 21. Máy thua, Bạn thắng!")
      break
    else:
      loi=True
      while loi:
        nguoi=int(input("Mời bạn chọn 1 số (1, 2 hoặc 3):"))
        if nguoi==1 or nguoi==2 or nguoi==3:
          loi=False
      tong+=nguoi
      print(f"Với bộ số (1, 2, 3), Bạn chọn {nguoi} nên Tổng = {tong}")
      if tong>=21:
        print(f"Tổng >= 21. Bạn thua, Máy thắng!")
        break
    