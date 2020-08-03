nums=[4,1,2,1,2]
map = {}
for item in nums:
    if item in map:
        map[item] += 1
        continue
    map[item] = 1
    
for k, v in map.items():
    if v == 1:
        print(k)