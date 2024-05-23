print("BẢNG CỬU CHƯƠNG TỪ 1 ĐẾN 9:")
for i in range(1,11):
  for j in range(1,10):
    print("{:<2} * {:>2} = {:>2}".format(j,i,i*j),end="\t")
  print()