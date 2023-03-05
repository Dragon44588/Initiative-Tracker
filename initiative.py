import random as ran


###defines the class to hold the name, initiative, and the modifier of players of monsters
class Creature:
    def __init__(self, name, modifier):
        self.name = name
        self.ini = 0
        self.mod = modifier

    ##defines how the class will be represented
    def __repr__(self):
        return("{}:{}, {}".format(self.name, self.mod, self.ini))

    ##defines how the class will update initiative    
    def updateIni(self, initiative):
        self.ini = initiative

    ##defines how the class will update modifier
    def updateMod(self, modifier):
        self.mod = modifier


        
###sorts the list of "Creatures" to display the order of attack
def sort_list(plays):
    length = len(plays) - 1
    sorted_list = []
    biggest_num = 0
    pos = 0

    while pos < length:
        first = plays[pos]
        second = plays[pos + 1]
        print("{} vs {}".format(first, second))

        if first.ini > second.ini:
            print("first is biggest")
        elif second.ini > first.ini:
            print("second is biggest")
        else:
            print("they are equal, so checking mod")

            if first.mod > second.mod:
                print("first is biggest")
            elif second.mod > first.mod:
                print("second is biggest")
            else:
                print("mods are equal")
        pos += 1
        
    #step 1: check ini value of first in list 
    #step 2: if ini is lower than next, continue
    #step 3: if ini is higher than next, replace
    #step 4: if ini is equal to next then sort by modifier
    #step 5: if mod is equal to next then roll 2 dice and sort by dice


    return sorted_list


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
                initiative = input("Enter {}'s initiative (write 'crit if nat 20'): ".format(player.name))
                if initiative == "crit":
                    break
                else:
                    initiative = int(initiative)
                    break

            except ValueError:
                print("initiative must be 'crit' or a number")
        if initiative == "crit":
            player.updateIni(999)
        else:
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