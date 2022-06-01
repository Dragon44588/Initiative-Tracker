import random as ran

class Player:
    def __init__(self, name):
        self.name = name
        self.ini = 0

    def __repr__(self):
        return("{}: {}".format(self.name, self.ini))
        
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


players = []
enemies = []
eloop = True
ploop = True
gameRunning = True


print("="*50 + "\n{0:^50}\n".format("Initiative") + "="*50)


while gameRunning: 
    
    while ploop:
        name = input("Enter player name or 'n' if no more: ")
        if name.upper() == "N":
            ploop = False
        else:
            player = Player(name)
            players.append(player)
    
    while eloop:
        name = input("Enter monsters name or 'n' if no more: ")
        if name.upper() == "N":
            eloop = False
        else:
            player = Player(name)
            enemies.append(player)
    
    for player in players:
        initiative = input("Enter {}'s initiative (write 'crit if nat 20'): ".format(player.name))
        if initiative == "crit":
            player.updateIni(999)
        else:
            player.updateIni(initiative)

    for enemy in enemies:
        initiative = input("Enter {}'s initiative (write 'crit if nat 20'): ".format(enemy.name))
        if initiative == "crit":
            enemy.updateIni(999)
        else:
            enemy.updateIni(initiative)

    combined = players + enemies
    ran.shuffle(combined)

    print("combined, shuffled lists")
    for i in combined:
        print("{}: {}".format(i.name, i.ini))
    
    sorted_list = sort_list(combined)

    print()
    print("sorted list")
    for i in sorted_list:
        print("{}".format(repr(i)))
    
    
    round = input("new round? Y/N: ")
    if round.upper() == "N":
        gameRunning = False
    else:
        eloop = True
        enemies.clear()



