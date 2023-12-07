'''def close_far(a, b, c):
 if abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2:
   return True
 elif abs(a-c)<=1 and (abs(a-b)>=2) and (abs(b-c)>=2):
   return True
 else:
   return False
print(close_far(5,6,4))'''



def non_start(a, b):
  q = len(a) 
  z = len(b)
  c = a[1:q] 
  d = b[1:z]
  return c+d

print(non_start("Hi, ","Armaan"))
