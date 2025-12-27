num1 = int(input("enter the first number "))
num2 =int(input("enter the second number "))

sel_operation = input("select operation +,-,*,/ ,%,**")

if sel_operation == '+':
    sum = num1 + num2
    print("the sum is ", sum)
elif sel_operation =='-':
    difference = num1 - num2
    print("the difference is ",difference)
elif sel_operation == '*':
    product = num1 * num2 
    print("the product is ",product)
elif sel_operation == '/':
    quotient = num1 / num2
    print("the quotient is ",quotient)
elif sel_operation == '%':
    remainder = num1 % num2
    print("the remainder is ",remainder)
elif sel_operation == '**':
    power = num1 ** num2
    print("the result is ",power)
else :
    print("invalid operation selected")