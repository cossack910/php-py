def bubbleSort(CB, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if int(CB[j][1]) < int(CB[j-1][1]):
                tmp = CB[j]
                CB[j] = CB[j-1]
                CB[j-1] = tmp
                
def selectSort(CS, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(CS[j][1]) < int(CS[minj][1]):
                minj = j
        tmp = CS[i]
        CS[i] = CS[minj]
        CS[minj] = tmp

def stableCheck(arr, sort_arr):
    for i in range(len(arr) -1 ):
        if sort_arr[i][1] == sort_arr[i+1][1] and arr.index(sort_arr[i]) > arr.index(sort_arr[i+1]):
            return 'Not stable'
    return 'Stable'
            

num = int(input())
input_arr = input().split(' ')
bubble = input_arr[:]
select = input_arr[:]

bubbleSort(bubble, num)
print(' '.join(bubble))
print(stableCheck(input_arr, bubble))

selectSort(select, num)
print(' '.join(select))
print(stableCheck(input_arr, select))