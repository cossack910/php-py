def binarySearch(n, S, key):
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if S[mid] == key:
            return True
        elif key < S[mid]:
            right = mid
        else:
            left = mid + 1

n = int(input())
S = list(map(int, input().split(' ')))

q = int(input())
T = list(map(int, input().split(' ')))

cnt = 0
for t in T:
    if True == binarySearch(n, S, t):
        cnt += 1
print(cnt)