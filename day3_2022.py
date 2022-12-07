with open("input_day3_test") as h:
    data = h.readlines()
    
ruckSack = set()
luggage = []
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for items in data:
    ruckSack.clear()
    items = items.strip()
    mid = int(len(items)/2)
    comp1 = items[:mid]
    comp2 = items[mid:]
    for item in comp1:
        if item in comp2:
            ruckSack.add(item)
    for i in ruckSack:
        luggage.append(i)
tots = 0
for item in luggage:
    tots += priority.find(item) + 1

print(tots)
