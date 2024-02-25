#try all Loops in For Loops Then in While Loops
#For Loops set up: def you_choose_name():
 #                      for count in range (1,6): #the number you start with goes in spot 1 (1) and the number you end with goes in spot 2 (6)
   #                       print(count)
                        
#For Loop 1
def for_loop1():
    for counter in range(1,101): #it counts from 0 up so you need to included 101 if you want it to include 100
        print(counter)

for_loop1()

#For Loop 2
def for_loop2():
    for even_count in range(2,501,2):
        print(even_count)

# for_loop2()

#For Loop 3
def for_loop3():
    for odd_count in range(1,501,2):
        print(odd_count)

# for_loop3()

#For Loop 4
def for_loop4():
    for backward_count in range(100,0,-1):
        print(backward_count)

#for_loop4()

#For Loop 5
def for_loop5():
    for backward_count_even in range(500,0,-2): #the -1 prints it bacwards the 500 and 0 are the in the range
        print(backward_count_even)

#for_loop5()

#For Loop 6
def for_loop6():
    for backward_count_odd in range(499,0,-2): #the -1 prints it bacwards the 500 and 0 are the in the range
        print(backward_count_odd)

#for_loop6()

def for_loop7():
    total = 0
    for int in range(1,100,2):
        total += int #+= means total=total+int
    print(total)    

# for_loop7()

#For Loop 8
def for_loop8(str):
    word = ""
    for e in range(len(str)-1,-1,-1):
        word += str[e] #this gets the index position  #word=word+str
    print(word)

# for_loop8("coding")

#For Loop 9
def for_loop9():
    x=int(input("Please Enter a Nubmer?"))
    total=1
    for int in range(x,0,-1):
        total *= int #*= means total=totalxint
        print(total)
    print(total)

# for_loop9()

#While Loop 1
def while_loop1():
    i = 1
    while i<=100:
        print(i)
        i +=1

#while_loop1()

#While loop 2
def while_loop2():
    a = 2
    while a<=500:
        print(a)
        a +=2

#while_loop2()

#While Loop 3

def while_loop3():
    i = 1
    while i<=500:
        print(i)
        i += 2

#while_loop3()


#While loop 4

def while_loop4():
    i = 100
    while i>=1:        
        print(i)
        i -=1

#while_loop4()

#While loop 5

def while_loop5():
    i = 500
    while i>=1:
        print(i)
        i -=2

#while_loop5()

#While loop 6
    
def while_loop6():
    i = 499
    while i>=1:
        print(i)
        i -=2   

#while_loop6()

#While loop 7

def while_loop7():    
    i = 1
    total = 0
    while i<=100:
        total+=i
        i+=1
        print(total)
    print(total)

#while_loop7()


#While Loop 8
def while_loop8(name):
    i = len(name)
    while i > 0:
        print(name[i], )
        i = i-1

while_loop8("cat")



