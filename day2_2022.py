#rock > scisors; scisors > paper; paper > rock
# rock A-X, paper B-Y, scisors C-Z

points = {'X':1, 'Y':2, 'Z':3}
with open("input") as f:
    vals = f.readlines()

score = 0

for game in vals:
    playerA = game[0]
    playerB = game[2]
    
    if playerA == "C" and playerB == "X":
        score = score + 6 + points[playerB]
    elif playerA == "A" and playerB == "Y":
        score = score + 6 + points[playerB]
    elif playerA == "B" and playerB == "Z":
        score = score + 6 + points[playerB]
        
    elif playerA == "A" and playerB == "X":
        score = score + 3 + points[playerB]
    elif playerA == "B" and playerB == "Y":
        score = score + 3 + points[playerB]
    elif playerA == "C" and playerB == "Z":
        score = score + 3 + points[playerB]
    else:
        score += points[playerB]
        
print("Player A points: ", score)


