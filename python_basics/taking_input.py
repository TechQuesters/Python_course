'''
Now we'll learn to take basic inputs from user 
syntax :
    variable_name = data_type(input("Your_message to diplay while taking input"))

    note:
    -> If no data_type is assigned while taking input
       it takes it as a string variable by default
'''

# for integer(eg- 1,100,-30,56,99,102456,etc) input we have the syntax:
age = int(input("Enter your age : ")) # here the age is a variable that stores integer value
print(age) # prints the entered age 

# taking float/Real numbers as input eg-(1.23,3.56,-13596.3465,etc)

salary=float(input("Enter your salary : ")) # here the salary is a variable that stores float value
print(salary) # prints the value of the salary variable

# taking string value

name=str(input("Enter your name : ")) # name holds a string value
# or
# name=input("Enter your name : ") #name holds a string value
print("Hello",name)

