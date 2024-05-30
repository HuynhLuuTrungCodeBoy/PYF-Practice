expenses = [
    {'name': 'apple', 'price': 1.2, 'date': '2024-05-30'},
    {'name': 'banana', 'price': 0.5, 'date': '2024-05-29'},
    {'name': 'orange', 'price': 0.8, 'date': '2024-05-28'},
    {'name': 'milk', 'price': 2.5, 'date': '2024-05-27'},
    {'name': 'bread', 'price': 1.5, 'date': '2024-05-26'},
    {'name': 'eggs', 'price': 2.0, 'date': '2024-05-25'}
]

def add_item(myTempList, item):
  myTempList.append(item)

def find_index_item(myTempList, item_name):
  result=-1
  length=len(myTempList)
  for i in range(length):
    if myTempList[i]['name']==item_name:
      result=i
  return result

def remove_item(myTempList, item_name):
  if find_index_item(myTempList,item_name)>-1:
    del myTempList[find_index_item(myTempList,item_name)]
  else:
    print(item_name + "not in list")

print("what do you want to do? -\n"\
      "1. Add\n" \
      "2. Remove")
option = int(input("Select option 1 or 2: "))
name_input = input("Item name: ")
if option == 1:
    cost_input = int(input("Item cost: "))
    date_input = input("Date: ")
    item = {'name': name_input, 'cost':cost_input, 'date':date_input}
    add_item(expenses, item)
    print("Your expenses: ")
    for i in expenses:
        print(i)
elif option == 2:
    remove_item(expenses, name_input)
    print("Your expenses: ")
    for i in expenses:
        print(i)
else:
    print("Invalid input")