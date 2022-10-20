gamers = {}
hockey_players = []

for i in range (0,2):
    name = input("Enter youe name")
    sport = input("Enter your sport")
    gamers[name] = sport 
count = 0
for name,sports in gamers.items():
    if (sports.upper()) == ("HOCKEY"):
        count = count+1
        hockey_players.append(name)
print("The number of players who played hockey are %d and they are %s" % (count,hockey_players))
