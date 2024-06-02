import os
def clrscr():
  if os.name=="nt":#windows
    os.system("cls")
  else:#Unix/Linux/Mac
    os.system("clear")

import random
length=random.randint(5, 10)
list1=[random.randint(0, length) for _ in range(length)]

def tim_2_so_max(list_in):  
  if list_in[1] > list_in[0]:
    max1=list_in[1];max2=list_in[0];
  else:
    max1=list_in[0]; max2=list_in[1];

  for i in range(2,length):
    if list_in[i] > max1:
      max2=max1;max1=list_in[i]
    elif list_in[i] > max2:
      max2=list_in[i]
  return (max1,max2)

big1,big2 = tim_2_so_max(list1)
clrscr()
print(list1)
print("2 số lớn nhất là:")
print(big1,' ',big2)