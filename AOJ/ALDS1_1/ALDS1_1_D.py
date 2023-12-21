n = int(input())

min = 0
ans = - (10**9)

for i in range(n):
    num = int(input())

    if i == 0:
        min = num
        continue
    
    if num  - min > ans:
        ans = num - min
    
    if  num < min:
        min = num
print(ans)