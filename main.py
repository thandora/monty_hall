#Monty Hall - Generalized

#1 Show and open all doorsx
#2 Shuffle doorsx
#3 Ask player to choose doorx
#4 From unchosen doors, open half of non-winning doors 
#5 Ask player to stay or switch
#6 Revaeal all

import random

def gen_losers(l: list, winner):
    """
    Returns a list of indices of losers. Losers are considered 
    those that are not <winner>
    """
    losers = []
    for i, x  in enumerate(l):
        if x != winner:
            losers.append(i)

    return losers

def gen_decoys(all_choices, losers, choice_index, winner, n: int = -1):
    """
    Returns a list of indices of decoys. Decoys are those that are not
    user choice indicated by <choice_index>, and not the winner.
    """
    if n == -1:
        n = len(losers) // 2

        if n == 0:
            n = 1

    elif n == 0:
        n = 0

    decoys = []
    for i, element in enumerate(all_choices):
        if not i == choice_index and element != winner:
            decoys.append(i)

    decoys = random.sample(decoys, k=n)
    return decoys

def list_printer(l: list, shown_index = -1):
    """
    Print formatted list. Indices in <shown_index> will be exposed.
    <shown_index> can be an integer, or a list of indices.
    Prints unrevealed elements if <shown_index> not provided.
    """
    if isinstance(shown_index, int) and shown_index != -1:
        temp_list = []
        temp_list.append(shown_index)
        shown_index = temp_list

    if shown_index != -1:
        print("[ ", end="")
        for i, _ in enumerate(l):
            if i in shown_index:
                print(f"[{l[i]}]", end="")
            else:
                print(f"[?]", end="")
            if i != (len(l) - 1):
                print(", ", end="")
        else:
            print(" ]")

    #Shown_index == -1 (Expose nothing)       
    else:
        print("[ ", end="")
        for i, _ in enumerate(l):
            print(f"[?]", end="")
            if i != (len(l) - 1):
                print(", ", end="")
        else:
            print(" ]")

def print_indicator(l: list, position: int):
    n = 0
    n_end = len(l)
    for n, _ in enumerate(l):
        if n == 0:
            print("   ", end="")

        if n == position:
            print("^ Your door", end="")
            break
        else:
            print("     ", end="")
    print("")

#Initialize initial parameters.
loser_element = 0
winner_element = 1
n_doors = 3
doors = []
for _ in range(n_doors - 1):
    doors.append(loser_element)
else:
    doors.append(winner_element)
    random.shuffle(doors)
winner_index = doors.index(winner_element)
# print(doors) #Test case


n_tests = 10000
current_test = 0
switch_choice = "s" #(s or w)
wins = 0
loses = 0
for _ in range(n_tests):


    #Randomly choose a door
    user_door_choice = random.choice(range(n_doors))

    #Make unopened doors list.
    losers = gen_losers(doors, 1)
    decoys = gen_decoys(doors, losers, user_door_choice, 1)
    unopened_doors = set(range(len(doors))) - set(decoys) - set([user_door_choice])

    #Choose to switch or stay.
    if switch_choice == "w":
        #Randomly choose from 1 of the unopened doors.
        user_door_choice = random.choice(list(unopened_doors))

    #Log
    if user_door_choice == winner_index:
        wins += 1
    else:
        loses += 1

if switch_choice == "w":
    print(f"You chose to switch")
else:
    print(f"You chose to stay.")
print(f"wins: {wins}")
print(f"loses: {loses}")
print(f"Win rate: {wins / (wins+loses)}")
#TODO let print_indicator() dynamically resize according to elements in list.