#Code 1:

score = 0
collisons = input("Please Enter The Number of Obstacles your Robot hit:")
deliveries = input("Please Enter the Number of Packages Your Robot delivered:")
score = (collisons*-10) + (deliveries*50)
if deliveries > collisons:
    score += 500
print(score)


