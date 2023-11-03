# 1 

def middle_3(s):
    if isinstance (s, str):
        return s[1:4]
    
s = "apple"

print(f"{middle_3(s)}")

# 2

def strings_2(a,b):
    if isinstance (a, str) and (b, str): 
        c = len(b)
        return (a[0:1] + b[c-1:c]) 
a = "apple"
b = "bag"  

print(f"{strings_2(a,b)}")
    

# 3 

def swapped_2(c):
    if isinstance (c, str):
        b = len(c)
    return (c[0:b-2] + c[b-1:b] + c[b-2:b-1])
 
c = "hello"

print(swapped_2(c))



#4 

def copies_3(h,b):
    if isinstance (h, str) and (b, str):
        return (h[0:2] + h[0:2] + h[0:2]) + (b[0:2] + b[0:2] + b[0:2])
    
h = "hello"
b = "bye"

print(f"{copies_3(h,b)}")