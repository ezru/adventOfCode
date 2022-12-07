#rock > scisors; scisors > paper; paper > rock
# rock A-X, paper B-Y, scisors C-Z

points = {'X':1, 'Y':2, 'Z':3, 'A':1, 'B':2, 'C':3}
with open("input") as f:
    vals = f.readlines()

score = 0

for game in vals:
    playerA = game[0]
    playerB = game[2]
    
    if playerB == 'X':
        if playerA == "A":
            score = score + points['Z']
        elif playerA == "B":
            score = score + points['X']
        else:
            score = score + points['Y']
    elif playerB == 'Y':
        score = score + 3 + points[playerA]
    else:
        if playerA == "A":
            score = score + 6 + points['Y']
        elif playerA == "B":
            score = score + 6 + points['Z']
        else:
            score = score + 6 + points['X']        
        
print("Player A points: ", score)


