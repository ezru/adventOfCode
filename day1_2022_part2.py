with open('input_day1') as f:
    data = f.readlines()

print(data)

cummulative = []
tempData = 0

for line in data:
    
    if line != '\n':
        line = line.strip()
        tempData = tempData + int(line)
    else:
        cummulative.append(tempData)
        tempData = 0

cummulative.sort()
print(cummulative)
print(cummulative[-1], cummulative[-2], cummulative[-3])
tots = cummulative[-1]+cummulative[-2]+cummulative[-3]
print(tots)
