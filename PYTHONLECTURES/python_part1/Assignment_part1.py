''' This is assignment for python level1 for my aiml journey'''
# Q1 
# name = str(input("enter your name :"))
# age = int(input("enter your age :"))
# print("Hello ", name, "you are",age,"years old")

#Q2

# a=float(input("enter the 1st num :"))
# b=float(input("enter the 2nd num :"))

# print("sum :",a+b)
# print("differnce: ",a-b)
# print("product: ",a*b)
# print("quotient",a/b)

#Q3
# a=int(input("enter 1st int number : "))
# b=int(input("enter 2nd int number : "))
# c=float(input("enter 1st float number : "))

# print(float(a+b+c)/3)

#Q4
# a=str(input("enter str num :"))
# b=int(a)
# c=float(a)
# d=str(a)
# print(b,"type is ",type(b))
# print(c,"type is ",type(c))
# print(d,"type is ",type(d))

#Q5
# x = 10 + 3 * 2 ** 2
# print(x)

# Q6
# a=3
# b=4
# t=a
# a=b
# b=t
# print("a:",a,"b:",b)

# Q7
# temperature = str(input("enter temp in celsius : "))
# CelsiusTemp=float(temperature)
# FahrenheitTemp = (CelsiusTemp*(9/5)+32)
# print("FahrenheitTemp :",FahrenheitTemp)

#Q8
# r=float(input("enter radius :"))
# Area = 3.14 * (r**2)
# print("Area: ",Area)

#Q9
# P=float(input("enter principal : "))
# R=float(input("enter Rate : "))
# T=float(input("enter Time : "))
# SI=(P*R*T)/100
# print("SI:",SI)

#Q10
num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part:", integer_part)
print("Fractional part:", round(fractional_part, 2))