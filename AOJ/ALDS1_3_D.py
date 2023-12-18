mizu = input()

area = []

top =0
x = 0
y = 0
for m in range(len(mizu)):
    if mizu[m] == "_":
        x += 1
        
    if mizu[m] == "\\":
        x += 1
        y -= 1
        
    if mizu[m] == "/":
        x += 1
        y += 1