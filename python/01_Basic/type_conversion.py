age = 25
name = "omkar"
# if we have concate the above two variables it will give error because we are trying to concate int with str
# print("my name is " + name + " and my age is " + age)
str_age = str(age)  # converting int to str
print(name+str_age)
print(float(age))  # converting int to float
print(int(25.67))  # converting float to int
print(complex(age))  # converting int to complex
print(complex(25.67))  # converting float to complex
print(bool(age))  # converting int to bool
print(bool(0))  # converting int to bool