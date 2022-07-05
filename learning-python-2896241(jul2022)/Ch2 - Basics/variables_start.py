# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)

# to access a member of a sequence type, use []
print(mylist[-1])
print(mytuple[-1])


# use slices to get parts of a sequence
print(mylist[1:3])


# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["one"])

# ERROR: variables of different types cannot be combined

## print("String type" + 123)
## cannot combine types - error: bash: syntax error near unexpected token `"String type"'

### the numbers can be converted to string to make these combine
print("string type" + str(123))

# Global vs. local variables in functions

mystr = "This is a string"

def someFunction():
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)
mystr = someFunction()

del mystr
print(mystr)