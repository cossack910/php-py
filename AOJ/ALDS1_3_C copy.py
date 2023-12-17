n = int(input())

ans = []
for i in range(n):
    val = input()
    if val[6] == 'F':
        ans.pop(0)
        continue
            
    if val[6] == 'L':
        ans.pop()
        continue
        
    do, number = val.split(' ')
    if val[0] == 'i':
        ans.insert(0, number)
        continue
        
    if val[0] == 'd' and number in ans:
        ans.remove(number)
            
print(' '.join(ans))