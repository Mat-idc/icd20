def read_baseball_data(file_path):
    names, hits, runs, rbis = [],[],[],[]
    try: #tries to catch errors
        with open(file_path, "r") as file:
            #skip the header line
            next(file)
            for line in file:
                data = line.strip().split(',')
                names.append(data[0])
                hits.append(int(data[1]))
                runs.append(int(data[2]))
                rbis.append(int(data[3]))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return names, hits, runs, rbis

def display_all_baseball_stats(names, hits, runs, rbis):
    for index in range (len(names)):
       print(f"|{names[index]:<25}|{hits[index]:>6}|{runs[index]:>6}|{rbis[index]:>6}") 

def calculate_and_display_average(hits,runs,rbis):
    print(f"Average Hits: {(sum(hits)/len(hits))}")
    print(f"Average Runs: {sum(runs)/len(runs)}")
    print(f"Average RBIs: {sum(rbis)/len(rbis)}")

def stat_leader(list, word, names):
    i = max(list)
    index = list.index(i)
    name = names[index]
    print(f"This Baseball player {name} has the most {word} with {i}")
    
def get_highest_player(number, names_copy, category, list):
    i = list.index(max(list))
    print(f"the player that has the {number} most {category.lower()} is {names[i]} with {list[i]}")
    list.pop(i)
    names_copy.pop(i)
    return names_copy, list

def display_top_10_in_category(category, names,hits,runs,rbis): #ERROR | Display top 10 players in a category")
    if category == "hits":
        list = hits
        done = True
    elif category == "runs":
        list = runs
        done = True
    elif category == "rbis":
        list = rbis
        done = True 
    if done:
       names_copy = names
       names_copy, list = get_highest_player("1st", names_copy, category, list)
       names_copy, list = get_highest_player("2nd", names_copy, category, list)
       names_copy, list = get_highest_player("3rd", names_copy, category, list)
       names_copy, list = get_highest_player("4th", names_copy, category, list)
       names_copy, list = get_highest_player("5th", names_copy, category, list)
       names_copy, list = get_highest_player("6th", names_copy, category, list)
       names_copy, list = get_highest_player("7th", names_copy, category, list)
       names_copy, list = get_highest_player("8th", names_copy, category, list)
       names_copy, list = get_highest_player("9th", names_copy, category, list)
       names_copy, list = get_highest_player("10th", names_copy, category, list)
  
def add_new_player(names, hits, runs, rbis):
    name = input("what is your new player's name? ")
    names.append(name)
    hits.append(int(input(f"how many hits does {name} have?")))
    runs.append(int(input(f"how many runs does {name} have?")))
    rbis.append(int(input(f"how many rbis does {name} have?")))

if __name__ == "__main__":
    # Specify the file path
    file_path = "Baseball Program.py/baseball_stats.txt"
    # Read baseball data from the file
    names, hits, runs, rbis = read_baseball_data(file_path)
    # Display menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. Display all baseball player statistics")
        print("2. Calculate and display average baseball statistics")
        print("3. Identify player with the most hits")
        print("4. Identify player with the most RBIs")
        print("5. Display top 10 players in a category")
        print("6. Add a new baseball player")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            display_all_baseball_stats(names, hits, runs, rbis) 
        elif choice == "2":
            calculate_and_display_average(hits,runs,rbis)   
        elif choice == "3":
            stat_leader(hits, "Hits", names)  #create these functions
        elif choice == "4":
            stat_leader(rbis, "RBIs", names)
        elif choice == "5":
            category = input("Enter the category to display top 10 players")
            display_top_10_in_category(category, names, hits, runs, rbis)
        elif choice == "6":
            add_new_player(names, hits, runs, rbis)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")