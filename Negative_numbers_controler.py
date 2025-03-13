#Control negative number
number = int(input("Enter number: "))
list = []

while number >= 0:
  list.append(number)
  if number < 0:
    break  
  number = int(input("Enter number: "))
print("the list of numbers: ", list)