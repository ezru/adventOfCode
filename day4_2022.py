with open('input_day4') as h:
    data = h.readlines()

area_1 = set() 
area_2 = set()
count = 0
for sections in data:
    sections = sections.strip()
    sec_1 = sections.find('-')
    sep = sections.find(',')
    sec_2 = sections.find('-',sep)
    start_1 = int(sections[:sec_1])
    end_1 = int(sections[sec_1+1: sep])
    for i in range(start_1,end_1+1):
        area_1.add(i)        
    start_2 = int(sections[sep+1:sec_2])
    end_2 = int(sections[sec_2+1:])
    for i in range(start_2, end_2+1):
        area_2.add(i)
    if area_2.issubset(area_1) or area_1.issubset(area_2):
        count += 1
    area_1.clear()
    area_2.clear()
print(count)