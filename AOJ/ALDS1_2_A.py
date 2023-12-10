# バブルソート

def bubbleSort(A, N):
    flg = 1
    change = 0
    while flg == 1:
        flg = 0
        for j in reversed(range(1 ,N)):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flg = 1
                change += 1
    return {
        "arr" : A, 
        "excahnge" : change,
    }

n = int(input())
a =  [int(i) for i in input().split(' ')]

ans = bubbleSort(a, n)
print (' '.join([str(i) for i in ans['arr']]))
print(ans['excahnge'])