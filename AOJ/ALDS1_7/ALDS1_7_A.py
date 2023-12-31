n = int(input())

tree = []
for i in range(n):
    A = list(map(int, input().split(' ')))
    tmp = [A[0]]
    for i in range(2, 2 + A[1]):
        tmp.append(A[i])
    tree.append(tmp)

def parentCheck(node):
    for t in range(len(tree)):
        if tree[t][0] == node:
            for i in range(len(tree)):
                if t != i:
                    for j in range(len(tree[i])):
                        if tree[i][j] == node:
                            return tree[i][0]
            return -1

def depthCheck(node):
    depth = 0
    for t in range(len(tree)):
        flg = node
        while True:
            flg = parentCheck(flg)
            if flg == -1:
                return depth
            depth += 1

def typeCheck(node):
    for t in range(len(tree)):
        if tree[t][0] == node:       
            if depthCheck(node) == 0:
                return ', root, [' + ', '.join(list(map(str, [tree[t][i] for i in range(1, len(tree[t]))]))) +']'
            if len(tree[t]) == 1:
                return ', leaf, []'
            return ', internal node, [' + ', '.join(list(map(str, [tree[t][i] for i in range(1, len(tree[t]))]))) +']'

for i in range(n):
    print('node ' + str(i) + ': parent = ' + str(parentCheck(i)) + ', depth = ' + str(depthCheck(i)) + typeCheck(i))