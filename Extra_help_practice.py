#test question 1 answer
import random

num = random.randint(1,10)
ans = int(input("Enter 1-10"))
while num != ans:
    if ans == num:
        print(num)

    elif ans != num:
        if num > ans:
            print("Your guess is  too low")
           
        if num < ans:
            print("Your answer is too high")
        ans = int(input("Enter 1-10"))

