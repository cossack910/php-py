def change(n):
    tmp = n[1]
    n[1] = n[0]
    n[0] = tmp

N = [1, 2]
change(N)
print(N)