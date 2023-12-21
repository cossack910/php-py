from collections import deque

n = int(input())

ans = deque()
for i in range(n):
    val = input()
    if val[6] == 'F':
        ans.popleft()
        continue
            
    if val[6] == 'L':
        ans.pop()
        continue
        
    do, number = val.split(' ')
    if val[0] == 'i':
        ans.appendleft(number)
        continue
        
    if val[0] == 'd' and number in ans:
        try:
            ans.remove(number)
        except:
            pass
            
print(' '.join(ans))