#shopping list total

x = float(input("Price of item 1: "))
y = float(input("Price of item 2: "))
z = float(input("Price of item 3: "))

x = x*1.08
y = y + y*0.08
z = z*1.08

c = x + y + z

print("Total Cost: $" + str(c))

