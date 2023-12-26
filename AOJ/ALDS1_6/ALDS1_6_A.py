def CountingSort(k):
    C = [0 for _ in range(k)]
    
    for j in range(1, len(A)):
        C[A[j]] += 1
        
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
        
    for j in reversed(range(1, len(A))):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

k = int(input())
A = list(map(int, input().split(' ')))
B = ['*' for _ in range(k)]
CountingSort(k)
print(' '.join(list(map(str, B))))