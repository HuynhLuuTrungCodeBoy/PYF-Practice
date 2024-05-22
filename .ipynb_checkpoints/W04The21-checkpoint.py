import random
###INPUT###
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

###PROCESSING###
print("\nNếu màn hình hiện số chẵn thì lượt chơi là của bạn.")
print("Nếu màn hình hiện số lẻ thì lượt chơi là của tôi.")
