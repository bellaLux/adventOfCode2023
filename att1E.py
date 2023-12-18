
data = []
with open('adventOfCode\\dia4\\data.txt', 'r') as file:
    data = [line.split(':')[1].strip() for line in file.readlines()]

scoreD = {i :[0, 1] for i in range(1, 209 + 1)}


for i in range(len(data)):
    line = data[i]
    scoreLine = scoreD[i + 1]
    games = [item.strip() for item in line.split('|')]
    game0 = [int(item) for item in games[0].replace(' ', '.').replace('..', '.').split('.')]
    game1 = [int(item) for item in games[1].replace(' ', '.').replace('..', '.').split('.')]

    for item in game0:
        if item in game1:
            scoreLine[0] += 1
    
    for c in range(1, 1 + (scoreLine[0] * scoreLine[1])):

        try:
            scoreD[i + c][1] += 1

        except:
            pass

    print(f""" LINHA: {line}
CHAVE: {scoreLine}
CÓPIAS: {scoreLine[1]}
""")
cards = 0
for c in range(len(scoreD)):
    cards += scoreD[c + 1][1]
#print(scoreD)
print(cards)
    
