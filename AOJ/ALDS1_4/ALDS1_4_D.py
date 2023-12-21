n, k = list(map(int, input().split(' ')))
W = []
for _ in range(n):
    W.append(int(input()))
    
def check(p: int):
    idx = 0
    for _ in range(k):
        sum = 0
        while W[idx] + sum <= p:
           sum += W[idx]
           idx += 1
           if idx == n:
               return True
    return False 

#２分探索
left = 0
rigth = 10**10 #最大積載 (n*k)
while rigth - left > 1:
    mid = (left+rigth)//2
    if True == check(mid):
        rigth = mid
    else:
        left = mid
print(rigth)