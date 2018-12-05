# Author: Jordan Robitaille
#SE116.21
#lab7
# Date: 12/03/2018


import random


ans = "y"
add2Party = "0"



#Character Base Stuff
#functions
def nameGen():
    fName = ['Grix ', 'Zarmac ' , 'Ezreal ' , 'Pog ' , 'Krimly ', 'Hob Hob ' , 'Chadsworth ' , 'Billiam ', 'Slim ' , 'Boz ' , 'Glime ' , 'Greg ' , 'Richard ']
    
    lName = ['Mibby ' , 'Smith ', "Ag'Mop " , 'Hoaish ' , 'Glorp ' , 'Termis ' , 'Richard ' ,'Blythe ' , 'Smooth ' , 'Mok ', 'Pinkerton', 'Shady' ]


    first = fName[random.randint(0,12)]
    last = lName[random.randint(0,11)]

    name = first + " " + last
    return name

def baseGen():
    alignment = ['Lawful Good ', 'Neutral Good ' , 'Chaotic Good ' , 'Lawful Neutral ', 'Neutral ', 'Chaotic Neutral ', 'Lawful Evil ', 'Neutral Evil ' , 'Chaotic Evil ']

    race = ['Gnome ', 'Dwarf ', 'Human ', 'Dragonborn ', 'Elf ' , 'Drow ', 'Halfling ' , 'Half-Orc ' , 'Tiefling ' , 'Half-Elf ' , 'Half-Drow ', 'Goblin ' , 'Genasi ' , 'Goliath ']


    align = alignment[random.randint(0,8)]
    racial = race[random.randint(0,13)]
    
    
    base = align + " " + racial
    return base

def roleRandom():
    type = ['Wizard ', 'Fighter ', 'Ranger ', 'Sorcerer ', 'Barbarian ', 'Bard ', 'Warlock ' , 'Cleric ' , 'Druid ' , 'Monk ' , 'Paladin ' , 'Rogue ' , ]

    role = type[random.randint(0,11)]

    return role



   

def greeting():
    ans = input("Would you like to run Random Character Creator? ['y' for yes] \n\t:")
    while(ans == "y"):

        #ask if want to use random name or user created
        name = nameGen()

        #ask if random or user picked
        base = baseGen()

        #ask if random or user picked
        role = roleRandom()

        print("--------------------------------------")
        print("Hello Adventurer! I am " + name + "\nI'm a " + base + role)
        print()

        if(role == 'Wizard '):#wizard
            print("I pledge to you, My Staff and Wisdom.")

        elif(role == 'Fighter '):#fighter
            print("I pledge to you, My Sword.")

        elif(role == 'Ranger '):#ranger
            print("I pledge to you, My Bow.")

        elif(role == 'Sorcerer '):#sorcerer
            print("I pledge to you, My Arcane Blood.")

        elif(role == 'Barbarian '):#Barbarian
            print("I pledge to you, My Axe.")

        elif(role == 'Bard '):#Bard
            print("I pledge to you, My Voice.")

        elif(role == 'Warlock '):#Warlock
            print("I pledge to you, My Dark Magic.")

        elif(role == 'Cleric '):#Cleric
            print("I pledge to you, My Righteuos Garbage.")

        elif(role == 'Druid '):#Druid
            print("I pledge to you, My Attunement of Nature.")

        elif(role == 'Monk '):#Monk
            print("I pledge to you, My Fists.")

        elif(role == 'Paladin '):#Paladin
            print("I pledge to you, My Shield.")

        elif(role == 'Rogue '):#Rogue
            print("I pledge to you, My Dagger.")


        print("--------------------------------------")
        print()
        #add2Party = input("Would you like to add this character to your party?  \n\t:")
        ans = input("Don't like this one? ['y' to run again] \n\t:")
        print()





#Main (for now)
greeting()




print("Happy Travels!")
