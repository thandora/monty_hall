# Monty Hall Problem - Simulation of n trials
# Change control variables to vary tests.
# Default monty hall problem:
# N_TO_OPEN = 1
# N_DOORS = 3

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
    user choice indicated by <choice_index>, and not the winner. n set to
    -1 is default, and will return half of the number of losers, rounded down.
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


# CONTROL VARIABLES ###################################
# Control variables.
N_TESTS = 10000  # Number of trials
# n_to_unopen represents how many doors are left
# unopened when the host opens the decoy doors.
N_TO_UNOPEN = 1  # Number of doors not to open. Default is 1
N_DOORS = 10
# s for stay, w for switch
SWITCH_CHOICE = "w"
#######################################################

# Initialize initial parameters.
loser_element = 0
winner_element = 1
doors = []

for _ in range(N_DOORS - 1):
    doors.append(loser_element)
else:
    doors.append(winner_element)
    random.shuffle(doors)
winner_index = doors.index(winner_element)

losers = gen_losers(doors, winner_element)

wins = 0
loses = 0
for _ in range(N_TESTS):

    # Randomly choose a door
    user_door_choice = random.choice(range(N_DOORS))

    # Make unopened doors list.
    losers = gen_losers(doors, winner_element)
    decoys = gen_decoys(doors, losers, user_door_choice, winner_element, len(losers) - N_TO_UNOPEN)
    unopened_doors = set(range(len(doors))) - set(decoys) - set([user_door_choice])

    # Choose to switch or stay.
    if SWITCH_CHOICE == "w":
        # Randomly choose from 1 of the unopened doors.
        user_door_choice = random.choice(list(unopened_doors))

    # Log
    if user_door_choice == winner_index:
        wins += 1
    else:
        loses += 1

if SWITCH_CHOICE == "w":
    print("You chose to switch")
else:
    print("You chose to stay.")

print(f"wins: {wins}")
print(f"loses: {loses}")
print(f"Win rate: {wins / (wins+loses)}")
print(f"Expected: {(N_DOORS - 1) / N_DOORS}")
