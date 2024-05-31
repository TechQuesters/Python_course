'''
power operator (**) or double asterisk is used to raise a number
to the power of another number

Eg-  2**4 = 2*2*2*2 (2 raised to the power 4)

'''
# Taking values from user
base=int(input("Enter the base : ")) # taking base from user
power=int(input("Enter power/exponent : ")) # taking power from user

ans=base**power # raises base to the exponent power
print(ans)

'''
QUIZ:
 you can try out for floating number by changing the input data type to float

 HINT- base=float(input(your_message))
        do the same for power
'''