import math
#homework 1

def multiply(x, y):
    return x*y

answer=multiply(7, 5)         
print(answer)   

#homework 2

def calculate_cylinder_volume(r,h):
    return math.pi*r**2*h

print(f"the volume is {round(calculate_cylinder_volume(10,15),2)}")

#homework 3
    
def print_triangle(c, h):
    t=1
    while h>0:
        print(f"{t*c}")
        h=h-1
        t=t+1

print_triangle("x",10)

#homework 4

def say_hello(name):
    print(f"Hello {name}")
say_hello("Grayson")

#homework 5 

def calculate_circle_area(r):
    z2 = math.pi*r**2
    print(f"{z2}")
    
q = calculate_circle_area(4)
print(f"{q}")

#homework 6
def print_square(t,d):
    t = str(t)
    g=d
    while g>0:
        print(f"{t*d}")
        g = g-1
print_square("3",14)

#homework 7

def calculate_power(num,p):
    answer = num**p
    print(f"{answer}")

d = calculate_power(4,2)
print(f"{d}")

#homework 8

def calculate_triangle_area(b,h):
    z = b*h/2
    print(f"{z}")

a2 = calculate_triangle_area(10,2)
print(f"{a2}")

  