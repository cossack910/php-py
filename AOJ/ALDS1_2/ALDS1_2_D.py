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
    h = 1
    G = []
    while h <= n:
        G.append(h)
        # シェルソートの間隔決める n**1.25
        h = 3*h + 1
    #逆順
    G = G[::-1]
    m  = len(G)
    print(m)
    print(' '.join(map(str, G)))
    
    for i in range(m):
        insertionSort(A, n, G[i])
    
num = int(input())

arr = [int(input()) for i in range(num)]
shellSort(arr, num)
print(cnt)
for i in arr:
    print(i)
    
# シェルソートの間隔値と計算量について参考
# https://web.archive.org/web/20170212072405/http://www.programming-magic.com/20100507074241/
# https://algoful.com/Archive/Algorithm/ShellSort