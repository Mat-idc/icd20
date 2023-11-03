# simple multiplication funtion (this is returning a single value)

def multiply(x,y):
    return x*y

# x is 6 and y is 7

num = multiply(6,7)
print(num)

# or

print(multiply(6,7))


#global & local variables:

global_book = "Science Encyclopedia" # global_book declared outside of all functions, it exists everywhere in the program
def x():
    local_book = "Chemistry Handbook"
    return local_book

print(x)
x="hi"

#simple function

def simple_function():
    x=7
    y=8
    z=9
    return x, y, z

