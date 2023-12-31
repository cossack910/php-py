n = int(input())
A = list(map(int, input().split(' ')))

sum = 0
for i in range(n):
    mx = 10**4 + 1
    idx = -1
    if i + 1 == n:
        break
    for j in range(i+1, n):
        if A[j] < mx and A[j] < A[i]:
            mx = A[j]
            idx = j
    print(A)
    if idx != -1:
        A[i], A[idx] = A[idx], A[i]
        sum += A[i] + A[idx]
    print(sum)
        
print(sum)