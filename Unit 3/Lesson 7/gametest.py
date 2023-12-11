#this code is practice code for the superhero adventure assignment:
#choose superhero returns the number of the superhero selected by the player (task 1)
def choose_superhero():
    while True: 
        print("Iron Man: 1")
        print("Thor: 2")
        print("Spiderman: 3")
        player_name = input("Which character would you like to be: (1,2,3)")
        if player_name == "1" or player_name == "2" or player_name == "3":
            break  
        else:
            print("Please try again")            
    return player_name


#introduces the player to their superhero (task 2)
def game_intro(player_superhero):
        if player_superhero=="1":
            print(f"Welcome Iron Man, to the city of New York! You will be tasked with defeating Thanos!")
        elif player_superhero=="2":
            print(f"Welcome Thor, to the city of New York! You will be tasked with defeating Thanos!")
        elif player_superhero=="3":
            print(f"Welcome Spiderman, to the city of New York! You will be tasked with defeating Thanos!")
        else:
            print("user error")
            
#(task 3)
def make_decision():
    while True:
        print("Thanos is destroying central park! Do you go to stop him, or seek help from the sourcerer, Dr. Strange")
        action = input("Enter 1 to stop him or 2 to call Dr. Strange:")
        if action == "1" or action == "2":
            return action 
        else:
            print("Invalid input")

def superhero_mission(action, player_superhero):
    if action == "1":             
        print("You find Thanos armed and ready for your attack. Prepare to fight")
        running = True
        while running:
            if player_superhero == "1":
                print("You blast Thanos and you're able to steal his Infinity Gauntlet and return victorious")  
            elif player_superhero == "2":
                print("You throw your hammer at Thanos and you're able to steal his Infinity Gauntlet and return victorious")  
            elif player_superhero == "3":
                print("You shoot webs at Thanos and you're able to steal his Infinity Gauntlet and return victorious")  
                attack = input("What attack would you like to do? 1 for stroke, 2 for punch, 3 for swing")
                if attack=="1":
                    if random.randint(0,100)<90:
                        print("your stroke finishes Thanos off. You return home victorious")
                        function_score +=20
                    else:
                        print("Your attack failed, leaving you vunerable to a counterattack. You don't return home")
                        function_score-=20
                    running = False
                elif attack=="2" or attack=="3":
                    if random.randint(0,100)<50:
                        print("your punch connects and finishes Thanos off. You return home victorious")
                        function_score+=30
                    else:
                        print("Your attack failed, leaving you vunerable to a counterattack. You don't return home")
                        function_score-=10
                    running = False
                else:
                    print("invalid input")


    elif action == "2":
        print("You and Dr.Strange team up with the Gaurdians of the Galaxy. You suprise attack Thanos and he is out numbered. You all return home victorious!")
#main code
player_superhero = choose_superhero()
game_intro(player_superhero)
action = make_decision()
