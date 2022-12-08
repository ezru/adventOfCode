with open('input_day5') as f:
    data = f.readlines()
    
#print(data)
row = [[],[],[],[],[],[],[],[],[]]

for line in data:
    if line.startswith('\n'):
        break
    else:
        if line[1:2] != ' ':
            row[0].append(line[1:2])
        if line[5:6] != ' ':
            row[1].append(line[5:6])
        if line[9:10] != ' ':
            row[2].append(line[9:10])
        if line[13:14] != ' ':
            row[3].append(line[13:14])
        if line[17:18] != ' ':
            row[4].append(line[17:18])
        if line[21:22] != ' ':
            row[5].append(line[21:22])
        if line[25:26] != ' ':
            row[6].append(line[25:26])
        if line[29:30] != ' ':
            row[7].append(line[29:30])
        if line[33:34] != ' ':
            row[8].append(line[33:34])
print(row)

cmds = data[10:]
print(cmds)

# Parse the commands with command names being variables
for cmd in cmds:
    mvPos = cmd.find('move') + 5
    mvPosEnd = cmd.find(' ',mvPos)
    frmPos = cmd.find('from') + 5
    fromPosEnd = cmd.find(' ',frmPos)
    toPos = cmd.find('to')+3
    toPosEnd = cmd.find('\n')
    move = int(cmd[mvPos:mvPosEnd])
    frm = int(cmd[frmPos:fromPosEnd])-1
    to = int(cmd[toPos:toPosEnd])-1
    print(move, frm, to)
    stackFrm = row[frm]
    stackTo = row[to]
    for i in range(0,move):
        crate = stackFrm[0]
        stackFrm.pop(0)
        stackTo.insert(0,crate)

print(row)
topCrate = []
for stack in row:
    topCrate.append(stack[0])

print(topCrate)