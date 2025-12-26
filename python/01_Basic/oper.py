'''in the python there are various operators used to perform operations on variables and values
arithmetic operators,assignment operators,comparison operators,logical operators,bitwise operators etc
operators are special symbols that perform specific operations on one or more operands  
eg +,-,*,/,%,//,**,=,==,!=,>,<,>=,<=,and,or,not,&,|,^,~,<<,>> etc'''
# examples of operators in python  
a = 10
b = 5
# arithmetic operators
print("Addition:",a+b)  # addition
print("Subtraction:",a-b)  # subtraction
print("Multiplication:",a*b)  # multiplication
print("Division:",a/b)  # division
print("Modulus:",a%b)  # modulus
print("Floor Division:",a//b)  # floor division
print("Exponentiation:",a**b)  # exponentiation
# assignment operators
c = 15
c += 5  # c = c + 5
print("Assignment Addition:",c)
c -= 5  # c = c - 5
print("Assignment Subtraction:",c)
c *= 2  # c = c * 2
print("Assignment Multiplication:",c)
c /= 5  # c = c / 5
print("Assignment Division:",c)
c %= 4  # c = c % 4
print("Assignment Modulus:",c)
# comparison operators
print("Equal to:",a==b)  # equal to
print("Not equal to:",a!=b)  # not equal to
print("Greater than:",a>b)  # greater than
print("Less than:",a<b)  # less than
print("Greater than or equal to:",a>=b)  # greater than or equal to
print("Less than or equal to:",a<=b)  # less than or equal to
# logical operators
print("Logical AND:",a>5 and b<10)  # logical and
print("Logical OR:",a>5 or b>10)  # logical or
print("Logical NOT:",not(a>5))  # logical not
# bitwise operators
print("Bitwise AND:",a&b)  # bitwise and
print("Bitwise OR:",a|b)  # bitwise or


print("Bitwise XOR:",a^b)  # bitwise xor
print("Bitwise NOT:",~a)  # bitwise not 
print("Left Shift:",a<<2)  # left shift
print("Right Shift:",a>>2)  # right shift