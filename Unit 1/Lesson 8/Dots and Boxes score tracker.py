#player's name
user_name = input("Please Enter Your Name:")

#points = number of boxes created: opoints = opponents points

#Game 1
name1 = input("Please Enter Opponent's Name for game 1:")
points1 = int(input("Please Enter Number of Boxes you Created:"))
opoints1 = int(input("Please Enter Number of Boxes your Opponent Created:"))

#Game 2
name2 = input("Please Enter Opponent's Name for game 2:")
points2 = int(input("Please Enter Number of Boxes you Created:"))
opoints2 = int(input("Please Enter Number of Boxes your Opponent Created:"))

#Game 3
name3 = input("Please Enter Opponent's Name for game 3:")
points3 = int(input("Please Enter Number of Boxes you Created:"))
opoints3 = int(input("Please Enter Number of Boxes your Opponent Created:"))

#Game 4
name4 = input("Please Enter Opponent's Name for game 4:")
points4 = int(input("Please Enter Number of Boxes you Created:"))
opoints4 = int(input("Please Enter Number of Boxes your Opponent Created:"))

#Game 5
name5 = input("Please Enter Opponent's Name for game 5:")
points5 = int(input("Please Enter Number of Boxes you Created:"))
opoints5 = int(input("Please Enter Number of Boxes your Opponent Created:"))

#yts = your total score and ots = opponents total score
yts = points1 + points2 + points3 + points4 + points5 
ots = opoints1 + opoints2 + opoints3 + opoints4 + opoints5

#box % for each game: g = game 
g1 = round(points1/49*100,2)
g2 = round(opoints2/49*100,2)
g3 = round(opoints3/49*100,2)
g4 = round(opoints4/49*100,2)
g5 = round(points5/49*100,2)

#percentage points recieved: totalp = total percentage
totalp = round((g1 + g2 + g3 + g4 + g5)/5,2)

print()
print(f"Player's Name: {user_name}")
print()
print(f"{'Opponents':<19} {'Your Points':>7} {'Opponent Points':>19} {'Box %':>14}")
print(f"==================================================================")
print(f"{name1:<15} {points1:>15} {opoints1:>19}{g1:>15.5}")
print(f"{name2:<15} {points2:>15} {opoints2:>19}{g2:>15.5}")
print(f"{name3:<15} {points3:>15} {opoints3:>19}{g3:>15.5}")
print(f"{name4:<15} {points4:>15} {opoints4:>19}{g4:>15.5}")
print(f"{name5:<15} {points5:>15} {opoints5:>19}{g5:>15.5}")
print(f"==================================================================")
print()
print(f"Summary:")
print(f"Total Points: {yts}")
print(f"Total Opponent Points: {ots}")
print(f"Percentage Points Recieved: {totalp}%")



