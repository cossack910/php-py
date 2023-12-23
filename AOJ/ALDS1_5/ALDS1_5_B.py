import math

def merge(A, left, mid, right):
    global cnt
    n1 = mid - left
    n2 = right - mid
    L = [A[left + i] for i in range(n1)]
    R = [A[mid + i] for i in range(n2)]
    L.append(math.inf)
    R.append(math.inf)
    
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        cnt += 1
            
def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A,left, mid)
        mergeSort(A, mid, right)
        merge(A,left, mid, right)
    return A
        
n = int(input())
A = list(map(int, input().split(' ')))

cnt = 0
B = mergeSort(A, 0, n)
print(' '.join(list(map(str, A))))
print(cnt)