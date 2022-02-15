numbersList1 = input('Please Enter Some Numbers:')
numbersList = list(map(int, numbersList1))
operator = input('Please choose an operator:')
num2 = int(input('Please choose another number:'))
EvenOdd = input('Do you want to know if each answer is Even or Odd? (Y/N)')
brackets = []


for num in numbersList:
    if operator == '*':
        brackets.append(num * num2)
    if operator == '/':
        brackets.append(round(num / num2, 2)) if num2 != 0 else print('You cant divide', num,  'by zero')
    if operator == '+':
        brackets.append(num + num2)
    if operator == '-':
        brackets.append(num - num2)

for a, b in zip(brackets, numbersList):
    if EvenOdd == 'N':
      print(b, operator, num2, '=', a)
    elif EvenOdd == 'Y':
        if a % 2 == 0:
            print(b, operator, num2, '=', a, 'The answer is even')
        else:
            print(b, operator, num2, '=', a, 'The answer is odd')
