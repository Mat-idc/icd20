#school resources project

f = int(input("Enter number of fountains:"))
w = int(input("Enter number of restrooms:"))
r = int(input("Enter number of rooms:"))
c = int(input("Enter number of aditional resources (common areas):"))
g = int(input("Enter number of aditional resources (gym/fitness rooms):"))

#Data collected

print("Water Fountains:")
print(f"Number of Water Fountains: {f} ")
print(f"Location: floor 1: 2, floor 2: 3, floor 3: 3")
print(f"Cleaniness of Water fountains: Clean and well maintained")

print()

print("Restrooms:")
print(f"Number of restrooms: {w}")
print(f"Location: floor 1: 4, floor 2: 6, floor 3: 8, floor 4: 4")
print(f"Cleaniness of restrooms: All clean and well maintained")

print("Rooms:")
print(f"Number of rooms: {r}")
print(f"Location: floor 1: 11, floor 2: 19, floor 3: 27, floor 4: 13")
print(f"Cleaniness of rooms: All clean and well maintained")

print()

print("Common Areas:")
print(f"Number of common areas: {c}")
print(f"Location: floor 1: 1, floor 2: 1, floor 3: 1, floor 4: 0")
print(f"Cleaniness of common area: All clean")

print()

print("Gym/fitness rooms:")
print(f"Number of gym/fitness rooms: {c}")
print(f"Location: floor 1: 1, floor 2: 1, floor 3: 0, floor 4: 0")
print(f"Cleaniness of gym/fitness rooms: All clean and well maintained")

print()

density_fountains = round(f/r,2)
density_restrooms = round(w/r,2)
density_common_areas = round(c/r,2)
density_gym = round(g/r,2)

print()

print(f"The fountain density is {density_fountains}, the restroom density is {density_restrooms}, the density of the common areas is {density_common_areas}, the density of the gyms/fitness rooms is {density_gym}.")