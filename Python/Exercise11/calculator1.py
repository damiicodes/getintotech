def calculator(num1, num2, operator):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        print(num1 + num2)
    if operator == '*':
        print(num1 * num2)
    if operator == '-':
        print(num1 - num2)
    if operator == '/':
        answer = (num1 / num2) if num2 != 0 else 0
        print(answer)



calculator(5,0,'/')

# not sure wheter to use float instead of int and then round