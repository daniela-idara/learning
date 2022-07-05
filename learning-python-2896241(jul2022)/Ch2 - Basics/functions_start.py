#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

#func1() # prints "I am a function"
#print(func1()) # prints "I am a function"
#print(func1) # prints None

# TODO: function that takes arguments

def func2(arg1, arg2):
  print(arg1, " ", arg2)

func2(10,20) # prints 10 20
print(func2(10,20)) # prints 10 20

# TODO: function that returns a value

def cube(x):
  return x * x * x

print(cube(3)) # prints 27 - 3 x 3 x 3

# TODO: function with default value for an argument
def power(num, x=1): # takes argument num and defined argument for x
    result = 1;
    for i in range(x):
        result = result * num
    return result

print(power(2)) # prints 2 - this is 2 x 1, then 2 to the power of number of items given = 2
print(power(2,3)) # prints 8 - this is 2 ^ 3. 
print(power(x=3, num=2)) # prints 8 - this is also 2 ^ 3. the arguments can be defined in the print, so order can be reversed



# TODO: function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(3,7,6,4)) # prints 20. adds all the arguments