#List String Problems

#problem 1 (Finds the Average Length of Words)

list = ["cow", 'dog', 'frog', 'pig']
total = 0
for element in list:
    total += len(element)    
average = total/len(list)
print(average)


#problem 2 (counts and prints Palindromic Words)

a = ['abccba', 'kayak', 'noon']

def function():
    count = 0
    for x in a:
        if x==x[::-1]: #this checks palindromes
            count +=1
    print(count)
    
function()


#problem 3 (Concatenates strings)

addstr = ["cow", "bat", "mango"]
print(addstr[0] + " " + addstr[1] + " " + addstr[2])


#problem 4 (counts the vowels in a list)

def vowel_count(l):
    vowel = "aeiou"
    dictionary = {}
    for x in l:
        count = 0 
        for y in range(len(x)):
            if x[y] in vowel:
                count+=1
            new_dic = {x: count}
            dictionary.update(new_dic)
    return dictionary

print(vowel_count(['hi', 'hii']))


#problem 5 (Alternate Uppercase) 

def alternate_upper(placeholder):
    for i in range(len(placeholder)):
        new_str = '' 
        for integer in range(len(placeholder[i])): 
            if integer%2==0:
                new_str+=placeholder[i][integer].upper()
            else:
                new_str+=placeholder[i][integer].lower()
        placeholder[i]=new_str 
    return placeholder

print(alternate_upper(['cow','bat','sat']))


#List Number Problems

#problem 1 (Seperates Positives and negatives in to two seperate lists) 
def pos_neg(x):
    pos_list = []
    neg_list = []
    for element in x:
        if element>0:
            pos_list.append(element) #why .append
        elif element<0:
            neg_list.append(element)
    return pos_list, neg_list


#problem 2 (checks if numbers in a list are in the fibonacci sequence)
def fibo_check(y):
    fibo = True
    for x in range(len(y)-2):
        if not y[x] + y[x+1] == y[x+2]:
            fibo = False
    return fibo
    
print(fibo_check([1,1,2,3,3]))

#problem 3 (Finds the squareroot of all numbers in a list and rounds them to the nearest integer)
import math

def sqrtnums (numsqrt): 
    new_list = []
    for i in range(len(numsqrt)):
        new_list.append(round(math.sqrt(numsqrt[i]),0))
    return new_list

print(sqrtnums([5,6,7,3]))

#problem 4 (runs the average of the numbers in a list) 
def avg(numavg):
    total = 0
    new_list = []
    for i in range(1,len(numavg)+1):
        total += numavg[i-1]
        new_list.append(total/i)        
        print(numavg[i-1])        
    return new_list
print(avg([6,4,8],)) 

#problem 5 (returns whether there is or isn't a consecutive pair with a difference of 1)
def con_check(z):
    for i in range(1,len(z)):
        if z[i] - z[i-1] == 1:
            return "there is a difference of 1"
    return "there is no difference of 1"

