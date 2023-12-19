from collections import deque

mizu = input()

stack = deque()
stack2 = []

for m in range(len(mizu)):
    if mizu[m] == "\\":
        stack.append(m)
        
    if mizu[m] == "/":
        if 0 < len(stack):
            p = stack.pop()
            stack2.append(list(map(int, [p, m])))           

s_area = 0                
for s in stack2:
    s_area += s[1] - s[0]
print(s_area)