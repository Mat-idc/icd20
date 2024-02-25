#For Loops Practice:
#while loops run forever until something tells it to stop
#for loops run in a set range

#print the numbers from 1 to 5 
def example_one():
    for counter in range(1,6): #for every thing we are calling, the counter in the range of 1 to 5 (6 is outside of this range)
        print(counter)

example_one()

# print the numbers from 0 to 9
def example_one_a():
    for counter in range(10): #this counter says end right before 10 (it starts at 0)
        print(counter)

example_one_a()

#add numbers from start to finish and return the total
def example_two(start,finish):
    total = 0
    for i in range(start, finish+1):
        total += i
    return total

answer = example_two(1,1000) #keeps adding to the total going up using number 1 to 1000
print(answer)

#this prints numbers from 20 to 1 and goes down by 2s
def example_three():
    for i in range(20,0, -2): # the -1 (can be changed to any number and then will go down by that number) 
        print(i)

example_three()

def example_four(str):
    result =''
    #for i in range(starting index in the string we want to start (first -1), ending index in the string (middle -1 (this will now include 0)), step = how much it goes up or down by (last -1))
    for i in range(len(str)-1, -1, -1): #this will print whatever str is backwards: (start, end, step) starts at -1, ends str at -1 so it includes the 0 or t in this case, the third -1 starts at the back of the str
        result += str[i]
        print(result)
    print(result)

example_four("Toronto")

#grab substrings of length n (n is a number you choose) and prints them to the screen
def example_five(str,n):
    for i in range(0,len(str)-n+1):
        print(str[i:+n])

example_five("truck", 3)

#count how many times the second word appears in the first word
def example_six(str1, str2): #first (str1) and second(str2) word
    if len(str2)>len(str1):
        return 0
    result = 0

    for i in range(0,len(str1)-len(str2)+1):
        if str1[i:i+len(str2)] == str2:
            result += 1
    
    return result

print(example_six("hihellohihi","hi")) #prints number of times "hi" is found in "hihellohihi"

