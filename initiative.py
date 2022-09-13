import random as ran

class Player:
    def __init__(self, name):
        self.name = name
        self.ini = 0
        self.modifier = 0

    def __repr__(self):
        return("{}:{}, {}".format(self.name, self.modifier, self.ini))
        
    def updateIni(self, initiative):
        self.ini = initiative


        
    
def sort_list(plays):
    length = len(plays)
    sorted_list = []
    biggest_num = 0
    pos = 0
    while len(sorted_list) != length:
        for p in range(0 , len(plays)):
            if biggest_num < int(plays[p].ini):
                biggest_num = int(plays[p].ini)
                pos = p   
        sorted_list.append(plays[pos])
        plays.pop(pos)
        biggest_num = 0
    return sorted_list

def collect_players():
    players = []
    playerloop = True
    while playerloop:
        name = input("Enter player name or 'n' if no more: ")
        if name.upper() == "N":
            playerloop = False
        else:
            modifier = input("Enter the player modifier value: ")
            player = Player(name)
            players.append(player)

    return players

            
def collect_monsters():
    enemies = []
    enemyloop = True
    while enemyloop:
        name = input("Enter monsters name or 'n' if no more: ")
        if name.upper() == "N":
            enemyloop = False
        else:
            while True:
                modifier = input("Enter monsters initiative modifier: ")
                try:
                    modifier = int(modifier)
                    break
                except:
                    print("modifier has to be an integer")
                
            player = Player(name, modifier)
            enemies.append(player)

    return enemies

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
    #sets this bool to false so that the players arent asked every time
    first = False
    combined = collect_initiative(combined)
    #shuffles the list
    ran.shuffle(combined)
    #sorts the list
    sorted_list = sort_list(combined)


    
    print("Initiative Order")
    for i in sorted_list:
        print("{}".format(repr(i)))
    
    
    round = input("new round? Y/N: ")
    if round.upper() == "N":
        gameRunning = False
    else:
        enemies.clear()



