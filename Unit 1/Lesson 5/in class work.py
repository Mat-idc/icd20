#problem 1

c = float(input("Please enter a dollar amount: $" ))

t=c//2
y=c%2

l=y//1
p=y%1

q=p//0.25
g=p%0.25

n=g//0.05
h=g%0.05


print(f"toonies is {t}, loonies is {l}, quarters is {q}, nickels is {n}.")