'''def multiply(x,y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x*y

x = float(input("Enter number 1:"))
y = float(input("Enter number 2:"))

print(f"{multiply(x,y)}")'''

import math
'''def calculate_area_of_circle(r):
    if isinstance(r,(int, float)):
        a = math.pi*r**2
        return (a)
    
r = float(input("Enter a number:"))

print(f"{round(calculate_area_of_circle(r),2)}")
        

a = input("Please enter num 1:")
b = input("Please enter num2:")

def armaan_function(a,b):
    if isinstance(a, (int, float)) and (b, (int, float)):
        return a**b
    else: 
        print("invalid input because it is not a number")'''


#this is the function
def area_rectangle(l,w):
    if isinstance(l, (int, float)) and isinstance (w, (int, float)):
        return l*w

#this is the function in use
l = 1
w = 4  
print(f"{area_rectangle(l,w)}")





#function
def adding_letters(a,b,c,d):
   if isinstance (a, (int, float)) and isinstance (b, (int, float)) and isinstance (c, (int, float)) and isinstance (d, (int, float)):
       return(a+b+c+d)

#function in use   
a = 1
b = 4
c = 6
d = 8

print(f"{adding_letters(a,b,c,d)}")













# Create and use a function so I can input 3 numbers (base, depth, and height) and it outputs the volume of a triangular prism

import math   

def volume_cylinder(r,h):
    if isinstance (b, (int, float)) and (d, (int, float)) and (h, (int, float)):
        return math.pi*r**2*h
    else: 
        print("invalid syntax please import numbers")

r = 6
h = 5

print(f"{volume_cylinder(r,h)}")


#Counts Character:
def character_count(s):
    if isinstance (s, str):
        a = len(s)
        return  s[a-3:a]
    
s = "hello"

print(f"{character_count(s)}")


#adding strings
def not_string(s):
    if isinstance (s, str):
        return ("not " + s)
    else:
        print("invalid input")

s = "armaan"
print(f"{not_string(s)}")
    

#cutting of strings
def string_cut(s):
    if isinstance (s, str):
        return (s[0:4] + " cat")

s = "armaan"

print(f"{string_cut(s)}")
    
    
#determining variable type

def determine_variable(n):
    if isinstance (n, float):
        return float
    elif isinstance (n, int):
        return int
    elif isinstance (n, bool):
        return bool
    else: 
        return ("n is a string")

n = "armaan is bad"

print(f"{determine_variable(n)}")
    





























    
    

    
