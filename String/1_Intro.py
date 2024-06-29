'''
    Strings can be a name,address,or para ,etc that is enclosed with single('statement') 
    or double (" Statement ") or even triple(written above) quotation
''' 
 # lets take an example

name="Python" # here 'name' variable is a string variable

# one can checck the data/class type of a variable using keyword 'type'

print(type(name)) # will print the class of name i.e str (means string)

'''
    NOTE:
    --> By default the input function takes a string input from the user 
        which is then typecasted to te desired data type(int,float,bool)
'''

# eg :

age=input("Enter age : ")

print(type(age)) # see the output will be of class str

# But if the input was like

age_new=int(input("Enter age : "))

print(type(age_new)) # the output will be class int because we type-casted the input to int data/class type
 
