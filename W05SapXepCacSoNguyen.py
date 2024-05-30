def sort_numbers(num1, num2, num3):
  temp=0
  if num2<num1: # 2 3 1 num2<num1 sai
    temp=num1
    num1=num2
    num2=temp
  if num3<num1:
    temp=num2
    num2=num1
    num1=num3
    num3=temp
  elif num3<num2:
    temp=num2
    num2=num3
    num3=temp
  return (num1,num2,num3)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

a, b, c = sort_numbers(x, y, z)
print("Original numbers: ", x, y, z)
print("Sorted numbers: ", a, b, c)