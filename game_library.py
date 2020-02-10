#!/usr/bin/python3
#Daisy Arnold
#1/27/2019
import pickle
#Data initializaton
datafile = open("game_lib.pickle" , "rb")
library_database = pickle.load(datafile)
datafile.close()
maxkey = max(list(library_database.keys()))
#constants
MENU_MESSAGE= """
What would you like to do:

1) Add/Edit Games
2) Print All Games
3) Search By Info
4) Remove a Game
5) Save Database
6) Quit
"""
INFO = ['Genre', 'Title',  'Developer', 'Publisher', 'System', 'Rating' , 'release date', 'single/multi?', 'price', 'completion status', 'purchase date', 'notes']
def add_edit_game():
    global maxkey
    
    user_input = input("Would you like to add(1) or edit(2)?: ")
    user_info = []
    if user_input == "1":
        is_valid = False
        while not is_valid:
            for i in range(len(INFO)):
                print('what is the ', INFO[i], ' of the game to add?: ')
                user_info.append(input())
            for i in range(len(INFO)):
                print(INFO[i] , ': ', user_info[i])
            user_input = input("is this right?")
            if user_input.lower() in ("y", "yes"):
                is_valid = True                
            maxkey+= 1 
        library_database[str(maxkey)] = user_info 
        #print("running add_game()")
    elif user_input == "2":
        for key in library_database.keys():
            print(key, "-", library_database[key][1])
        user_key = int(input("which game would you like to change"))
        is_valid = False
        while not is_valid:
            for i in range(len(INFO)):
                print('what is the new', INFO[i], ' of the game?: ')
                user_info.append(input(""))
            for i in range(len(INFO)):
                print(INFO[i] , ': ', user_info[i])
            user_input = input("is this right?")
            if user_input.lower() in ("y", "yes"):
                is_valid = True
            library_database[user_key] = user_info
            
def print_all_games():
    #TODO: if the data is not in the library, ask to enter the data
    game_keys = list(library_database.keys())
    for game_key in game_keys:
        for j in range(len(INFO)):
            print(INFO[j] , ': ', library_database[game_key][j])
    print("---------------------------------------")       
    print("running print_all_games()")

def search_by_info(is_return=False):
    if is_return == False: 
        category = None
        while category == None:
            number_found = 0
            print("What info would you like to search for? ")
           
            for i in range(len(INFO)):
                if i == len(INFO)-2:
                    print(INFO[i],", or, " , end=" ")
                elif i == len(INFO)-1:
                    print(INFO[i])
                else:
                    print(INFO[i], end=", ")
                    
                    
            user_category = input("") 
            for i in range(len(INFO)):
                if user_category == INFO[i]:
                    category= i 
            if category == None:
                print("invalid category, try again: ")
                
    else:
        category = 1
    print("what is the ", INFO[category], " of the game to search: ")
    user_data = input()
    if is_return==False:
        for game_key in library_database.keys():
            
            if user_data in library_database[game_key][category]:
                number_found+=1
                
                for j in range(len(INFO)):
                    print(INFO[j] , ': ', library_database[game_key][j])            
                print("----------------------") 
    else:
        for game_key in library_database.keys():
            if user_data == library_database[game_key][category]:
                return game_key
                 
    if number_found == 0:
        print("*** NO MATCHES FOUND!***\n")
    else:
        print('we found ', number_found, ' matches') 
    
    print("running search_by_title()")
def remove_a_game():
    key = search_by_info(is_return=True)
    library_database.pop[key]
    print("running remove_a_game()")
def save_database():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(library_database, datafile)
    datafile.close()
def quit():
    choice = input('would you like to save?\n(Y/N): ')
    if choice.lower() == 'y':
        datafile = open("game_lib.pickle", "wb")
        pickle.dump(library_database, datafile)
        datafile.close()        
    
    exit()
while True:
    choice = input(MENU_MESSAGE)
    if choice == "1":
        add_edit_game()
    elif choice == "2":
        print_all_games()
    elif choice == "3":
        search_by_info()
    elif choice == "4":
        remove_a_game()
    elif choice == "5":
        save_database()
    elif choice == "6":
            quit()