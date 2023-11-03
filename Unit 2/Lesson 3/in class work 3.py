#practicing returns #1

'''def sleep_in(weekday, vacation):
    if(vacation):
        return True
    elif(weekday is False):
        return True
    else:
        return False
    

# #2 

def hello_name(name):
    return ("Hello " + name + "!")


#this will cut of the string after 3 chracters/letters
x = input("string: ")
b = x[0:3]
print(b)'''

def string_a(s):
    if isinstance(s, (str)):
        return s[0:3]

s = "cash"
print(f"{string_a(s)}")
       




def string_b(s,n):
    if isinstance (s, str) and isinstance (n, (int, float)):
        return s[0:n]

n = int(input("please enter number:"))
s = input("please enter string:")
print(f"{string_b(s,n)}")













