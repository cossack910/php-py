cnt = 0

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
        
def shellSort(A, n):
    m = n//2
    h = 1
    G = []
    while h < n:
        G.append(h)
        h = 3*h + 1
    #逆順
    G = G[::-1]
    print(m)
    print(' '.join(map(str, G)))
    
    for i in range(m):
        insertionSort(A, n, G[i])
    
num = int(input())

arr = []
for i in range(num):
    arr.append(int(input()))
    
shellSort(arr, num)
print(cnt)
for i in arr:
    print(i)