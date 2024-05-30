list1=[-11, 2, 3,0, 4, 5, -6,0]
def get_min_numbers(numbers):
  result = numbers[0]
  for num in numbers:
        if result > num:
            result = num
  return result

min_number = get_min_numbers(list1)
print("Min number: ", min_number)