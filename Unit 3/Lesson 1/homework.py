#1
def caught_speeding(speed, is_birthday):
    if is_birthday == False:
        if speed <=60:
            return "no ticket"
        if speed >60 and speed <=80:
            return "small ticket"
        if speed >=81:
            return "big ticket"
    else:
        if speed <=65:
            return "no ticket"
        if speed >65 and speed <=85:
            return "small ticket"
        if speed >=86:
            return "big ticket"
    
print(f"{caught_speeding(65,True)}")
    
#2

def not_strings(s):
    if s[0:3] == "not":
        return s
    else:
        return "not" + s

s = input("Please enter a word:")  
print(f"{not_strings(s)}")

#3

def squirrel_play(temp, is_summer):
  if is_summer == True:
    if temp >= 60 and temp <=100:
      return True
    else:
      return False
  if is_summer == False:
    if temp >= 60 and temp <=90:
      return True
    else:
      return False
    
print(f"{squirrel_play(60, True)}")

      

#4 

def in1020(a, b):
    if a >= 10 and a <= 20 or b >= 10 and b <= 20 : 
       return True
    else:
       return False

a = 5
b = 5
print(f"{in1020(a, b)}")

#5

def length_string(s,d):
   if len(s) == 0:
     return "Empty"
   if d == True:
      return s[0:1]
   if d == False: 
    a = len(s)
    return s[4-a:a]
   
s = ""
print(f"{length_string(s,True)}")
