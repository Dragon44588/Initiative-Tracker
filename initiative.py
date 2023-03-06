import random as ran
from datetime import datetime as dtime


###defines the class to hold the name, initiative, and the modifier of players of monsters
class Creature:
    def __init__(self, name, modifier):
        self.name = name
        self.ini = 0
        self.mod = modifier

    ##defines how the class will be represented
    def __repr__(self):
        return("Name: {}, Modifier: {}, Initiative:{}".format(self.name, self.mod, self.ini))

    ##defines how the class will update initiative    
    def updateIni(self, initiative):
        self.ini = initiative

    ##defines how the class will update modifier
    def updateMod(self, modifier):
        self.mod = modifier


        
###sorts the list of "Creatures" to display the order of attack
def sort_list(plays):
    length = len(plays) - 1
    increment = 0
    pos = 0

    while increment <= length:
        print()
        origin = plays[increment]
        while pos < length:
            if increment != pos:
                check = plays[pos]
                
                if origin.ini > check.ini:
                    temp = plays[increment]
                    plays[increment] = plays[pos]
                    plays[pos] = temp

                elif origin.ini == check.ini:

                    if origin.mod > check.mod:
                        temp = plays[increment]
                        plays[increment] = plays[pos]
                        plays[pos] = temp
                    
                    elif origin.mod == check.mod:
                        r1 = 0
                        r2 = 0
                        while r1 == r2:
                            r1 = ran.randint(1,20)
                            r2 = ran.randint(1,20)

                        if r2 > r1:
                            print("if {} won with a roll of {} vs {}".format(origin, r2, r1))
                            temp = plays[pos]
                            plays[pos] = plays[increment]
                            plays[increment] = temp
                        
                        else:
                            print("if {} won with a roll of {} vs {}".format(check, r1, r2))
                            temp = plays[increment]
                            plays[increment] = plays[pos]
                            plays[pos] = temp                            
    
                pos +=1
            
            else:
                pos +=1
                
        increment += 1
        pos = 0


    return plays


###collects the players names and their dexterity modifier
def collect_players():
    players = []
    playerloop = True
    while playerloop:
        name = input("Enter player name or 'n' if no more: ")
        if name.upper() == "N":
            playerloop = False
        else:
            while True:
                try:
                    modifier = int(input("Enter the player modifier value: "))
                    player = Creature(name, modifier)
                    players.append(player)
                    break
                except:
                    print("Modifier needs to be a positive or negative integer")

    return players


###collects the monsters names and their dexterity modifer           
def collect_monsters():
    monsters = []
    monsterloop = True
    while monsterloop:
        name = input("Enter Monsters name or 'n' if no more: ")
        if name.upper() == "N":
            monsterloop = False
        else:
            while True:
                try:
                    modifier = int(input("Enter the Monsters modifier value: "))
                    monster = Creature(name, modifier)
                    monsters.append(monster)
                    break
                except:
                    print("Modifier needs to be a positive or negative integer")

    return monsters


###collects the list of creatures and collects their intiative
def collect_initiative(players):
    for player in players:
        while True:
            try:
                initiative = input("Enter {}'s initiative: ".format(player.name))
                initiative = int(initiative)
                break

            except ValueError:
                print("initiative must be a number")

        player.updateIni(initiative)         
    return players



first = True
gameRunning = True
players = []
enemies = []

print("="*50 + "\n{0:^50}\n".format("Initiative") + "="*50)


while gameRunning: 
    #collects players and monsters and combines the lists
    if first:
        players = collect_players()
    enemies = collect_monsters()
    combined = players + enemies
    #sets this bool to false so that the players arent collected every time
    first = False
    combined = collect_initiative(combined)
    #sorts the list
    sorted_list = sort_list(combined)


    #prints the order of initiative

    print("Initiative Order")
    for i in sorted_list:
        print("{}".format(repr(i)))
    
    
    round = input("new round? Y/N: ")
    if round.upper() == "N":
        gameRunning = False
    else:
        enemies.clear()