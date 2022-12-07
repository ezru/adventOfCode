with open('input_day1') as f:
    data = f.readlines()

print(data)

cummulative = 0
tempData = 0

for line in data:
    
    if line != '\n':
        line = line.strip()
        tempData = tempData + int(line)
    else:
        if tempData > cummulative:
            cummulative = tempData
            tempData = 0
        else:
            tempData=0

print(cummulative)