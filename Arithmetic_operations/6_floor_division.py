'''
next we have the floor_division ( // ) operator
it works on two operants and return the integral part of the division.

Eg- suppose you have a division 10/3,then what's the quotient
    your right it would be 3.333333333333..

    but if we do floor division then
    10//3 will be equal to 3 
    (it only return the integral value)
'''

# let's have a hand on demo

print(10//3)

x=int(input("Enter 1st number : ")) # taking integer input from user
y=int(input("Enter 2nd number : ")) # taking integer input fro  user

int_div = x//y # assigning int_div the floor division of x // y

print(int_div) # printing the value

