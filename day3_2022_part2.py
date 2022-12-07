with open("input_day3") as h:
    data = h.readlines()

count = 0
group = []
badge = []
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = 0
for items in data:
    count += 1
    items = items.strip()
    group.append(items)
    
    if count % 3 == 0:
        counter +=1
        #print(group)
        for item in group[0]:
            if item in group[1]:
                if item in group[2]:
                    print("Group",counter,": ", item)
                    badge.append(item)
                    break
        #print(badge)
        
        group.clear()

print(len(data))        
print(len(badge))
tots = 0
for item in badge:
    tots += priority.find(item) + 1
print(tots)