def partion(p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i+1

n = int(input())
A = list(map(int, input().split(' ')))

pb = partion(0, n-1)
A = list(map(str, A))
A[pb] = '[' + A[pb] + ']'
print(' '.join(A))
