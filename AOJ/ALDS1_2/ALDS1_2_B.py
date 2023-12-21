# 選択ソート

def selectionSort(A, N):
    exchange = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if A[i]  != A[minj]:
            exchange += 1
        tmp = A[i]
        A[i] = A[minj]
        A[minj] = tmp

    return {
        "arr" : A,
        "exchange" : exchange
    }

n = int(input())
a = list(map(int, input().split(' ')))

arr = selectionSort(a, n)
print(' '.join(list(map(str, arr["arr"]))))
print(arr["exchange"])