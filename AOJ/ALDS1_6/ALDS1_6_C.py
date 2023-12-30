def partion(p, r):
    x = int(A[r][1])
    i = p-1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(p, r):
    if p < r:
        q = partion(p, r)
        quickSort(p, q-1)
        quickSort(q+1, r)


def stableCheck(n):
    for i in range(1, n):
        if A[i-1][1] == A[i][1] and S.index(A[i-1]) > S.index(A[i]):
            print('Not stable')
            return
    print('Stable')
            
n = int(input())
A = [input().split(' ') for _ in range(n)]
S = A[:]

quickSort(0, n-1)
stableCheck(n)
for a in A:
    print(' '.join(list(map(str, a))))