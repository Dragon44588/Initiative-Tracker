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
    increment = 0
    pos = 0
    x = 0

    while increment <= length:
        print()
        origin = plays[increment]
        while pos < length:
            if increment != pos:
                check = plays[pos]
                print("checking {} against {}".format(origin, check))
                
                if origin.ini > check.ini:
                    print("{} is bigger than {} and needs to be swapped".format(origin, check))
                    temp = plays[increment]
                    plays[increment] = plays[pos]
                    plays[pos] = temp

                elif origin.ini == check.ini:
                    print("{} is equal to {}, the modifier needs to be checked".format(origin, check))

                    if origin.mod > check.mod:
                        print("{} is bigger than {} and needs to be swapped".format(origin, check))
                        temp = plays[increment]
                        plays[increment] = plays[pos]
                        plays[pos] = temp
                    
                    elif origin.mod == check.mod:
                        print("theyre equal >:(")
                pos +=1
            
            else:
                print("dont check current pos")
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