#Decoding number from right to left (number 5 stop)

number = int(input("Enter a code of numbers: "))

sum = 0
actual_number = number

while actual_number > 0:
  last_number = actual_number % 10
  if last_number == 5:
    break
  actual_number = (actual_number - last_number) / 10
  sum = sum + last_number
  if actual_number < 0:
    break
  
print('sum is', sum)

