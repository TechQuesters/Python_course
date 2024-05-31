'''
next we have the division operator
same as multiplication but it return the division of two operants

NOTE :
    1.In python the divsion of two integers can result in a floating value 
    unlike C/C++..
    2. Division by 0 is not allowed, keep in mind or it will throw an error
    DivisionByZero error
'''

a=5
b=10

print(a/b) # prints 5/10 = 0.5
# or
print(5/10)
# or
div = a / b # product variable holds the value of a/b ie 0.5
print(div)

# Taking values from user
num1=int(input("Enter a 1st number : ")) # taking 1st number from user
num2=int(input("Enter a 1st number : ")) # taking 2nd number from user

div=num1/num2 # dividing the numbers and getting the output

print(div)
