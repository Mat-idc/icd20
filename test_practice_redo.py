#Repetition Unit Test 

#Section 1 While Loops

'''#1
num = int(input("Please Enter a Positive Integer:"))

while num < 0:
    print("Please Input a Positive Integer!")
    num = int(input("Please Enter a Positive Integer:"))

print(num)

#2
import random

num2 = int(input("Please Enter a Number:"))
rando = random.randint(1,10)

while num2 != rando:
    if num2 > rando:
        print("Guess is too High!")
        num2 = int(input("Please Enter another Number:"))
    if num2 < rando:
        print("Guess is too Low!")
        num2 = int(input("Please Enter another Number:"))
print(num2)

#3
num = 2
sum_e = 0

# Use a while loop to iterate through even numbers from 2 to 10
while num <= 10:
    sum_e = sum_e + num
    num = num + 2 #increase num each time

    print(sum_e)

#Section 2 For Loops

#4

total = 0
for num in range(0,21,2):
    total = total + num
    print(total)


#5

char = (input("Please Input a Character:"))
i = int(input("Please Enter the number of times you want to repeat this character:"))

for y in range (0,i):
    y = char*i

print(y)

#6

for i in range(8,0,-1):
    print(i)

#Section 3 Functions with Both Loops

#7

str1 = input("Please enter a sentance: ")

def count_vowels(str1):
    vowels = "aeiouAEIOU"

    count = 0

    for x in str1:
        if x in vowels:
            count += 1
        print(count)

count_vowels(str1)


#8

def reverse_strings(s):
    
    reversed_s=""

    for x in range(len(s) -1, -1,-1):
        reversed_s += s[x]
    return reversed_s

str2 = input("Howdy, Please Enter a word: ")
print(reverse_strings(str2))'''


#9

def remove_vowels(s):
    result = ""
    vowels = "aeiouAEIOU"
    for char in s:
        if char not in vowels: #not in, is a boolean function that determines True or False based on whether char is in vowels
            result += char
    return(result)

print(remove_vowels("happy"))





