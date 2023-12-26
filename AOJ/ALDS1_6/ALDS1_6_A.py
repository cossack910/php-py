def CountingSort():
    C = [0 for _ in range(max(A) + 1)]
    
    for j in range(len(A)):
        C[A[j]] += 1
        
    for i in range(1, max(A) + 1):
        C[i] = C[i] + C[i - 1]
        
    for j in reversed(range(len(A))):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    
k = int(input())
A = list(map(int, input().split(' ')))
B = ['*' for _ in range(k+1)]
CountingSort()
print(' '.join(list(map(str, B[1:]))))