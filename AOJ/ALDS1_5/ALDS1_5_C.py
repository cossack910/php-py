import math

n = int(input())

def kock(n, p1, p2):
    if n == 0:
        return
    
    sx = (2 * p1[0] + 1 * p2[0]) / 3
    sy = (2 * p1[1] + 1 * p2[1]) / 3
    tx = (1 * p1[0] + 2 * p2[0]) / 3
    ty = (1 * p1[1] + 2 * p2[1]) / 3
    ux = (tx - sx) * math.cos(math.radians(60)) - (ty - sy) * math.sin(math.radians(60)) + sx
    uy = (tx - sx) * math.sin(math.radians(60)) + (ty - sy) * math.cos(math.radians(60)) + sy
    s = [sx, sy]
    t = [tx, ty]
    u = [ux, uy]
    
    kock(n - 1, p1, s)
    print(' '.join(list(map(str, s))))
    kock(n - 1, s, u)
    print(' '.join(list(map(str, u))))
    kock(n - 1, u, t)
    print(' '.join(list(map(str, t))))
    kock(n - 1, t, p2)
    
p1 = [0, 0]
p2 = [100, 0]

print(' '.join(list(map(str, p1))))
kock(n, p1, p2)
print(' '.join(list(map(str, p2))))