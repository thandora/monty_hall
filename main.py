# Monty Hall - Generalized

# 1 Show and open all doorsx
# 2 Shuffle doors
# 3 Ask player to choose doorx
# 4 From unchosen doors, open half of non-winning doors
# 5 Ask player to stay or switch
# 6 Revaeal all

import random


def gen_losers(losers_list: list, winner):
    """
    Returns a list of indices of losers. Losers are considered
    those that are not <winner>
    """
    losers = []
    for i, x in enumerate(losers_list):
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


def list_printer(list_to_print: list, shown_index=-1):
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
        for i, _ in enumerate(list_to_print):
            if i in shown_index:
                print(f"[{list_to_print[i]}]", end="")
            else:
                print("[?]", end="")
            if i != (len(list_to_print) - 1):
                print(", ", end="")
        else:
            print(" ]")

    # Shown_index == -1 (Expose nothing)
    else:
        print("[ ", end="")
        for i, _ in enumerate(list_to_print):
            print("[?]", end="")
            if i != (len(list_to_print) - 1):
                print(", ", end="")
        else:
            print(" ]")


def print_indicator(list_to_format: list, position: int):
    n = 0
    for n, _ in enumerate(list_to_format):
        if n == 0:
            print("   ", end="")

        if n == position:
            print("^ Your door", end="")
            break
        else:
            print("     ", end="")
    print("")


# Initialize initial parameters.
loser_element = 0
winner_element = 1
n_doors = 3  # Original monty hall is 3 doors.
doors = []
for _ in range(n_doors - 1):
    doors.append(loser_element)
else:
    doors.append(winner_element)
    random.shuffle(doors)

# 1 Show all doors
list_printer(doors, range(n_doors))

# 2 Shuffle doors
print("Shuffling doors...")
random.shuffle(doors)
winner_index = doors.index(winner_element)
list_printer(doors)


# 3 Ask player to choose a door
user_door_choice = None
while user_door_choice not in range(1, n_doors + 1):
    try:
        user_door_choice = int(input("Choose a door number: "))
    except:
        print(f"Input must be a number! (1 to {n_doors})")

print(f"\n\nYou chose door {user_door_choice}")
user_door_choice -= 1  # Translate to python index

# 4 From unchosen doors, open half of non-winning doors
losers = gen_losers(doors, winner_element)
decoys = gen_decoys(doors, losers, user_door_choice, winner_element)
print(f"You chose door number {user_door_choice + 1}. Opening some doors...")
list_printer(doors, decoys)
print_indicator(doors, user_door_choice)

# 6 Let player choose to switch or stay.
unopened_doors = set(range(len(doors))) - set(decoys) - set([user_door_choice])

switch_choice = ""
while switch_choice not in ["s", "w"]:
    try:
        switch_choice = input("Stay or switch door? (S / W): ").lower()
    except:
        print("Input valid choice! S to stay or choose a door number")

# Format unopened_doors for UX
f_unopened_doors = []
for element in unopened_doors:
    f_unopened_doors.append(element + 1)

if switch_choice == "w":
    user_door_choice = ""
    while user_door_choice not in f_unopened_doors:
        try:
            user_door_choice = int(
                input(f"Choose an unopened door number {f_unopened_doors}: ")
            )
        except:
            print("Enter a valid door number.")

    user_door_choice -= 1  # Convert to index form

list_printer(doors, range(len(doors)))
print_indicator(doors, user_door_choice)

if user_door_choice == winner_index:
    print("You found the car! You win")
else:
    print("You found a cow, you lose. :(")
