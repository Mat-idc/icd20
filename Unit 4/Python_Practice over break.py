#basic printing and equations

#a = float(input("Please Enter Number 1:"))
#b = float(input("Please Enter Number 2:"))

#print("The Sum is" ,a+b, "")

'''#loops
n = int(input("Please Enter a NUMBER, Thank you: "))
a=1

while a<=10:
    print(n*a)
    a=a+1

def multiples_of_n(n):
    for i in range(n,n*10+1,n):
        print(i)

multiples_of_n(3)'''
#n = int(input("Please Enter a number between 1 and 6:"))
#a = len(n)

#for n in range(n,n*1,000,000,1):
    #print(n)
    #n += 1
  


n = int(input("Please provide number between 1-1000:"))
 
#print(f"{num!}")


'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(n))'''

import random

def random_nums(len):
    string=""
    for i in range(len):
        string+=str(random.randint(1,10))
    print(string)

random_nums(len)

