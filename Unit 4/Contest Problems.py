#Problem J1

g1 = input("Please enter win or lose?")
g2 = input("Please enter win or lose?")
g3 = input("Please enter win or lose?")
g4 = input("Please enter win or lose?")
g5 = input("Please enter win or lose?")
g6 = input("Please enter win or lose?")

w = 0

if g1 == "w":
    w =+1

if g2 == "w":
    w=+1

if g1 == "w":
    w =+1

if g2 == "w":
    w=+1

if g1 == "w":
    w =+1

if g2 == "w":
    w=+1

if w >= 5:
    print("group 1")

elif w >= 3:
    print("group 2")

elif w >= 1:
    print("group 3") 

else:
    w = 0
    print("you are eliminated")

#Problem J2

import random


a = (random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000))
b = (random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000))
c = (random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000))
d = (random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000) + random.randint(1,10000))

if (a == a and b and c and d) and (b == a and b and c and d) and (c == a and b and c and d) and (d == a and b and c and d):
    print "magic"

else:
    print "not magic"

