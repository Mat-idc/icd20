#This imports a library and states the global variables
import random
score = 0
game_running = True
current_health = 100 

#Task 1 choose superhero returns the number of the superhero selected by the player 
def choose_superhero():
    print("Iron Man: 1")
    print("Thor: 2")
    print("Spiderman: 3")
    player_name = input("which character do you want to be. (Enter: 1,2,3)? ")        
    return player_name

#Task 2 introduces the player to their superhero
def game_intro(player_superhero):
    if player_superhero=="1":
        print(f"Welcome Iron Man, to the city of New York! You will be tasked with defeating Thanos")
    elif player_superhero=="2":
        print(f"Welcome Thor, to the city of New York! You will be tasked with defeating Thanos")
    else:
        print(f"Welcome Spiderman, to the city of New York! You will be tasked with defeating Thanos")

#Task 3 allows the user to choose whether to faceoff alone or get backup to fight Thanos
def make_decision():
    while True:
            print("Thanos is destroying central park! Do you go to stop him, or seek help from the sourcerer, Dr. Strange")  
            decision = input("1 to face him, 2 to get help:")  
            if decision=="1" or decision=="2":
                return decision
            else:
                print("invalid input")
                print()

#Task 4 responds to whether the user chose to get backup or to faceoff Thanos alone it also gives options for attacks if they chose to faceoff alone
def superhero_mission(action, player_superhero):     
    if action=="1":
        current_health = health_managment()
        if player_superhero=="1" or "2" or "3": 
            print("You find Thanos armed and ready for your attack. Prepare to fight.")
            running = True
            while running:
                attack = input("What attack would you like to do? 1 for stroke, 2 for punch, 3 for swing.")
                if attack=="1":
                    if random.randint(0,100)<70:
                        print(f"Your stroke finishes Thanos off. You return home victorious with {current_health} health left.")                        
                        return "20"
                    else:
                        print("Your attack failed, leaving you vunerable to a counterattack. You don't return home.")
                        return "0 and your health is 0"                   
                    running = False
                elif attack=="2" or attack=="3":
                    if random.randint(0,100)<60:
                        #current_health = health_managment()
                        print(f"your punch connects and finishes Thanos off. You return home victorious with {current_health} health left.")
                        return "10"
                    else:                        
                        print("Your attack failed, leaving you vunerable to a counterattack. You don't return home.")
                        return "0 and your health is 0"
                    running = False                    
                else:
                    print("invalid input")
                    
    elif action=="2":
        current_health = health_managment()
        if player_superhero=="1":
            print(f"You and Dr.Strange team up with the Gaurdians of the Galaxy. You suprise attack Thanos and he is out numbered. You have {current_health} health left!")
            return "20"
        else:
            print("Thanos brings backup. Your attack failed and Dr. Strange is knocked out. You don't return home.")
    return "0 and your health is 0"

#Task 5 determines health of superhero
def health_managment():
    damage_taken = random.randint(0,100)
    return current_health-damage_taken

#This is the main code
print(f"You start with {current_health} health")
player_name = choose_superhero()
game_intro(player_name)
decision = make_decision()
score = superhero_mission(decision, player_name)
print(f"Your Final Score Was {score}!")



    