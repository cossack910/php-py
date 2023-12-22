n = int(input())
A = list(map(int, input().split(' ')))

q = int(input())
M = list(map(int, input().split(' ')))

for i in range(q):
    tmp = [[False for i in range(M[i] + 1)] for j in range(n)]
    for y in range(n):
        for x in range(M[i] + 1):
            if y > 0  and tmp[y-1][x] == True: 
                tmp[y][x] = True
                
            if y > 0  and tmp[y-1][x] == True and x + A[y] <= M[i]: 
                tmp[y][x + A[y]] = True
                
            if A[y] <= M[i]:
                tmp[y][A[y]] = True
                
    if tmp[n - 1][M[i]] == True : 
        print('yes')
    else:
        print('no')        