# 1. middle 3 

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
    

# 3 i don't understand

def swapped_2(c):
    if isinstance (c, str):
        
        return (a[c-1:c] + b[d-1:d])



#4 

def copies_3(h,b):
    if isinstance (h, str) and (b, str):
        return (h[0:2] + h[0:2] + h[0:2]) + (b[0:2] + b[0:2] + b[0:2])
    
h = "hello"
b = "bye"

print(f"{copies_3(h,b)}")