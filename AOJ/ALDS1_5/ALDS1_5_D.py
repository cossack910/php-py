import math

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left + i] for i in range(n1)]
    R = [A[mid + i] for i in range(n2)]
    L.append(math.inf)
    R.append(math.inf)
    
    i = 0
    j = 0
    cnt = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            cnt += mid - left - i
    return cnt
            
def mergeSort(A, left, right):
    cnt = 0
    if left + 1 < right:
        mid = (left + right) // 2
        cnt += mergeSort(A,left, mid)
        cnt += mergeSort(A, mid, right)
        cnt += merge(A,left, mid, right)
    return cnt
        
n = int(input())
A = list(map(int, input().split(' ')))

cnt = mergeSort(A, 0, n)
print(cnt)