mizu = input()

area = 0
mizu_arr = []

x = 0
y = 0
map = [[y, x]]
for m in range(len(mizu)):
    if mizu[m] == "_":
        x += 1
        
    if mizu[m] == "\\":
        x += 1
        y -= 1
        
    if mizu[m] == "/":
        x += 1
        y += 1
        
    map.append([y, x])
print(map)