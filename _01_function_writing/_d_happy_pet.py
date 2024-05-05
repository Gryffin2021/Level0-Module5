"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk
happiness = 0

def feed(happiness, pet):
    messagebox.showinfo(title="Result", message="You fed your " + str(pet) + "...")
    if pet == "Duck":
        messagebox.showinfo(title="2 HP Lost", message="Your duck enjoys its food, but expects more and is overall ungrateful. Its never-ending hunger consumes its happiness.")
        happiness -= 2
    else:
        messagebox.showinfo(title="1 HP Gained", message="Your pet is overjoyed with the kind choice of food!")
        happiness += 1
    return happiness
def walk(happiness, pet):
    if pet == "Fish":
        messagebox.showinfo(title="Fishy Fudgin' Died", message="You took your fish for a walk. It was so sad and bored, that it died.")
        happiness = -1000
    elif pet == "Duck":
        messagebox.showinfo(title="No HP change", message="Your duck hates you, and doesn't want to go on a walk.")
    else:
        messagebox.showinfo(title="2 HP Gained",message="Your " + str(pet) + " is happy to spend time with you!")
        happiness += 2
    return happiness
def play(happiness, pet):
    if pet == "Duck":
        messagebox.showinfo(title="No HP change", message="Your duck hates you, and doesn't want to play.")
    else:
        messagebox.showinfo(title="2 HP Gained", message="Your " + str(pet) + " is happy to spend time with you and does some cute rolls!")
        happiness += 1
    return happiness
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pet = simpledialog.askstring(title="Pet Shop",prompt="What type of pet do you desire. (Cat) (Dog) (Duck) (Fish)")
    while happiness < 10 and happiness > -3:
        activity = simpledialog.askstring(title="Activity",prompt=str(pet) + " (Feed) (Walk) (Play)")
        if activity == "Feed":
            happiness = feed(happiness, pet)
        elif activity == "Walk":
            happiness = walk(happiness, pet)
        else:
           happiness = play(happiness, pet)
    if happiness < 10:
        messagebox.showinfo(title=":(",message="Your " + pet + " died!")
    else:
        messagebox.showinfo(title=":)",message="Your pet loves you!")
    pass
