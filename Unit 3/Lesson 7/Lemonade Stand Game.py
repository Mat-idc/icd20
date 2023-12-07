#importing the random function
import random

#this will defined the weather
def weather(num):
    if num==1:
        return "rainy day"
    elif num==2:
        return "sunny day"
    elif num==3: 
        return "cloudy day"
    elif num==4: 
        return "thunderstorm"
    elif num==5: 
        return"hot and sunny day"

#this will get the user to input the price per cup and number of cups they want to make   
def pricing():
    while True:
        cups_lemonade = int(input("Please enter number of lemonade cups you want to make (between 3 and 50):"))
        cup_price = int(input("Please enter the price you want to charge per cup of lemonade in cents:"))
        if cups_lemonade>50 or cups_lemonade<3:
            print("invalid input, please try again")
        elif cup_price>100 or cup_price<3:
            print("be reasonable")
        else:
            return cups_lemonade,cup_price

#based on the weather this will determine the number of customers
def customer_amount():
        if weather(num) == "rainy day":
            return random.randint(10,15)
        elif weather(num) == "sunny day":
            return random.randint(30,40)
        elif weather(num) == "thunderstorm":
            return random.randint(0,5)
        elif weather(num) == "hot and sunny day":
            return random.randint(30,50)
        else:
            weather(num) == "cloudy day"
            return random.randint(10,20)

#200 cents is the total profit you start with
total_profit = 200
day = 0

#These are all the outputs to the user put into a loop
while True:
    num = random.randint(1,5)
    print(f"The weather is: {weather(num)}")
    cups_lemonade, cup_price = pricing()
    num_of_customers = customer_amount()

    #3 cents is the cost to make a cup of lemonade    
    if cups_lemonade>num_of_customers: profit = ((num_of_customers)*cup_price-(cups_lemonade*3))
    else: profit = ((cups_lemonade)*cup_price-(cups_lemonade*3))
    
    day +=1
    print(f"Day: {day}")

    print(f"Your profit was: {profit} cents")
    print(f"The number of customers was: {customer_amount()}")

    total_profit = total_profit+profit
    print(f"Your total profit was: {total_profit} cents")

    #this asks the user if they want to continue or stop
    yes_or_no = input("Please enter yes or no if you want to continue:")
    if yes_or_no == "no":
        break #this breaks out of the loop
    else:
        pass #this returns you back to the top of the loop (it's a placeholder)

#Brief Report:
#For my lemonade stand game I used logic to decide how weather effects customers. 
#I created it so on sunny, nice weather days, there are more potential customers and on rainy, -
#bad weather days, there are less potential customers. 
#My pricing strategy was that more customer on nice weather days results - 
#in a higher profit versus less customers on bad weather days which results in a lower profit, - 
#since there are less people buying lemonade. If I could improve one thing in my program, -
#I would make a function that can deter customers from buying lemonade when charged at higher prices, -
#and make more customers buy lemonade when charged at lower prices.



